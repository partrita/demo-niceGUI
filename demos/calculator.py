from nicegui import ui


class Calculator:
    # Tailwind CSS 클래스 정의
    btn_classes = (
        "w-1/4 text-xl font-bold p-2 m-1 border bg-gray-200 hover:bg-gray-700 shadow"
    )
    # 버튼 레이아웃 정의
    layout_buttons = [
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["C", "0", ".", "="],
    ]

    def __init__(self):
        # 계산기 전체를 감싸는 카드 컴포넌트
        # JustPy의 Div(a=wp, classes="m-1 border inline-block", style="width: 250px")에 해당
        with ui.card().classes("m-1 border inline-block").props('style="width: 250px"'):
            # JustPy의 Input(readonly=True, ...)에 해당
            self.tape = (
                ui.input(
                    readonly=True,
                    value=" ",
                )
                .classes("block p-2 m-2 border text-right text-sm bg-gray-200")
                .props('style="width: 90%"')
            )

            # JustPy의 Input(readonly=True, ...)에 해당
            self.result = (
                ui.input(
                    readonly=True,
                    value="0",
                )
                .classes("block p-2 m-2 border text-2xl text-right")
                .props('style="width: 90%"')
            )

            # 버튼 레이아웃 생성
            for line in self.__class__.layout_buttons:
                # 각 버튼 행은 ui.row로 감싸서 유연한 레이아웃을 만듭니다.
                with ui.row().classes("flex w-auto m-2"):
                    for b_text in line:
                        # JustPy의 Button(click=self.calculator_click)에 해당
                        ui.button(
                            b_text,
                            on_click=self.on_button_click,  # NiceGUI는 클릭 이벤트를 on_click으로 처리
                        ).classes(self.__class__.btn_classes)
                        # JustPy의 b1.calc = self 와 같은 참조는 NiceGUI에서는 직접 이벤트 핸들러가
                        # 클래스 인스턴스에 접근하므로 필요 없습니다.

        # 계산 로직을 위한 내부 상태 변수
        self.current_expression = ""  # 현재 입력되고 있는 숫자나 연산식을 저장
        self.last_result = "0"  # 이전에 계산된 최종 결과
        self.operator = None  # 현재 선택된 연산자

    # JustPy의 @staticmethod calculator_click(self, msg)에 해당
    # NiceGUI에서는 클래스 메서드나 인스턴스 메서드로 이벤트를 처리할 수 있습니다.
    def on_button_click(self, e):
        btn_text = e.sender.text  # 클릭된 버튼의 텍스트 가져오기

        if btn_text == "C":  # Clear 버튼
            self.current_expression = ""
            self.last_result = "0"
            self.operator = None
            self.result.set_value("0")
            self.tape.set_value(" ")
        elif btn_text == "=":  # 등호 버튼
            try:
                # eval 함수를 사용하여 현재 테이프의 식을 계산합니다.
                # 보안상 주의해야 할 부분이지만, 이 예시에서는 단순 계산기 기능이므로 사용합니다.
                final_result = str(eval(self.tape.value))
                self.result.set_value(final_result)
                self.tape.set_value(final_result)  # 계산 결과를 테이프에 유지
                self.current_expression = (
                    final_result  # 다음 계산을 위해 현재 표현식 업데이트
                )
                self.last_result = final_result
                self.operator = None
            except Exception:  # 유효하지 않은 식에 대한 오류 처리
                self.result.set_value("Error")
                self.tape.set_value(" ")
                self.current_expression = ""
                self.last_result = "0"
                self.operator = None
        else:  # 숫자 또는 연산자 버튼
            current_tape_value = (
                self.tape.value.strip()
            )  # 현재 테이프 값 가져오기 (공백 제거)

            # 첫 입력이거나 마지막 문자가 연산자이고 새 입력도 연산자일 때
            # JustPy 코드의 calc.tape.value[-1] in "*+-/" or self.text in "*+-/" 조건에 해당
            if (
                current_tape_value
                and current_tape_value[-1] in "+-*/"
                and btn_text in "+-*/"
            ) or (not current_tape_value and btn_text in "+-*/"):
                # 이미 연산자가 있거나 첫 입력이 연산자면, 연산자만 업데이트 (예: '5 + *' -> '5 *')
                if current_tape_value and current_tape_value[-1] in "+-*/":
                    self.tape.set_value(current_tape_value[:-1] + btn_text)
                else:  # 테이프가 비어있는데 연산자를 누르면 현재 결과값을 사용
                    self.tape.set_value(self.last_result + " " + btn_text)
                    self.current_expression = ""  # 다음 숫자 입력을 위해 초기화
            else:
                if current_tape_value == " " or self.result.value == "Error":
                    self.tape.set_value(btn_text)
                else:
                    self.tape.set_value(current_tape_value + btn_text)

            self.current_expression += btn_text  # 현재 입력된 숫자나 연산자를 추가

            # 실시간으로 계산 결과 업데이트 시도 (에러 발생 시 무시)
            try:
                # eval을 사용하기 전에 공백을 제거하여 유효한 식을 만듭니다.
                display_value = str(eval(self.tape.value.replace(" ", "")))
                self.result.set_value(display_value)
                self.last_result = display_value
            except Exception:
                pass  # 유효하지 않은 식은 무시


# NiceGUI 앱을 시작할 때 Calculator 인스턴스를 생성합니다.
@ui.page("/")  # 기본 경로에 계산기 페이지를 만듭니다.
def show_calculator():
    Calculator()  # Calculator 클래스의 인스턴스를 생성하면 __init__ 메서드에서 UI가 구축됩니다.


ui.run()  # NiceGUI 애플리케이션 시작
