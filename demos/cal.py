from nicegui import ui

# CSS 클래스 정의 (Tailwind CSS)
INPUT_CLASSES = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
DISPLAY_CLASSES = "m-2 p-2 h-32 text-xl border-2"


# JustPy의 my_input 함수에 해당하는 NiceGUI 이벤트 핸들러
def on_input_change(e):
    # 이벤트 발생 컴포넌트(e.sender)의 'div_label' 속성으로 연결된 레이블의 텍스트를 업데이트합니다.
    e.sender.div_label.set_text(e.value)


@ui.page("/")  # NiceGUI에서 웹 페이지를 정의합니다.
def input_demo_page():
    ui.label("Input Demo").classes("text-2xl font-bold m-2")  # 제목 추가

    # 첫 번째 입력 필드: 숫자를 입력하고 결과를 실시간으로 표시합니다.
    in1 = ui.input(placeholder="숫자를 입력하세요", type="number").classes(
        INPUT_CLASSES
    )

    # 입력 내용이 표시될 레이블을 정의하고, in1에 연결합니다.
    in1.div_label = ui.label("여기에 입력하는 내용이 표시됩니다.").classes(
        DISPLAY_CLASSES
    )

    # in1의 'input' 이벤트에 핸들러를 연결하여 입력 시마다 `div_label`을 업데이트합니다.
    in1.on("input", on_input_change)

    ui.separator().classes("my-8")  # 시각적 구분을 위한 구분선

    # Calculator 클래스 인스턴스를 페이지에 추가합니다.
    Calculator()


# NiceGUI의 계산기 클래스 정의
class Calculator:
    BTN_CLASSES = (
        "w-1/4 text-xl font-bold p-2 m-1 border bg-gray-200 hover:bg-gray-700 shadow"
    )
    # 계산기 버튼 레이아웃
    LAYOUT_BUTTONS = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
    ]

    def __init__(self):
        # 계산기 UI를 위한 카드 컨테이너를 생성합니다.
        with ui.card().classes("w-96 p-4 m-4"):
            ui.label("Calculator").classes("text-2xl font-bold text-center w-full mb-4")

            # 입력 식을 보여주는 테이프 디스플레이
            self.tape = (
                ui.input(
                    readonly=True,
                    value=" ",
                )
                .classes("block p-2 m-2 border text-right text-sm bg-gray-200")
                .props('style="width: 90%"')
            )

            # 계산 결과를 보여주는 결과 디스플레이
            self.result = (
                ui.input(
                    readonly=True,
                    value="0",
                )
                .classes("block p-2 m-2 border text-2xl text-right")
                .props('style="width: 90%"')
            )

            # 버튼 레이아웃 생성
            for line in self.__class__.LAYOUT_BUTTONS:
                with ui.row().classes(
                    "w-full justify-around"
                ):  # 각 버튼 행은 ui.row로 감싸기
                    for b_text in line:
                        ui.button(
                            b_text,
                            on_click=self.on_button_click,  # 버튼 클릭 핸들러 연결
                        ).classes(self.__class__.BTN_CLASSES)

        # 계산기 상태 변수 초기화
        self.current_expression = ""
        self.last_value = 0.0  # 부동 소수점 연산을 위해 초기값을 float으로 변경
        self.operator = None

    def on_button_click(self, e):
        btn_text = e.sender.text  # 클릭된 버튼의 텍스트 가져오기

        if btn_text.isdigit() or btn_text == ".":
            self.current_expression += btn_text
            self.result.set_value(self.current_expression)
        elif btn_text in ["+", "-", "*", "/"]:
            if self.current_expression:  # 현재 숫자가 있을 경우에만 연산자 처리
                self.last_value = float(self.current_expression)
                self.operator = btn_text
                self.tape.set_value(f"{self.last_value} {self.operator}")
                self.current_expression = ""
            elif (
                self.last_value and self.operator
            ):  # 이전 계산값과 연산자가 있고 새 연산자가 들어온 경우
                self.operator = btn_text
                self.tape.set_value(f"{self.last_value} {self.operator}")
            else:  # 초기 상태에서 연산자 입력 방지
                pass
        elif btn_text == "=":
            if self.current_expression and self.operator:
                try:
                    second_value = float(self.current_expression)
                    if self.operator == "+":
                        self.last_value += second_value
                    elif self.operator == "-":
                        self.last_value -= second_value
                    elif self.operator == "*":
                        self.last_value *= second_value
                    elif self.operator == "/":
                        if second_value != 0:
                            self.last_value /= second_value
                        else:
                            self.result.set_value("Error: Div by zero")
                            self.reset_calculator_state()
                            return

                    # 결과는 소수점 이하 불필요한 0 제거
                    display_result = self.last_value
                    if display_result == int(display_result):
                        display_result = int(display_result)

                    self.result.set_value(str(display_result))
                    self.tape.set_value(
                        f"{self.tape.value} {second_value} = {display_result}"
                    )
                    self.current_expression = str(
                        display_result
                    )  # 다음 연산을 위해 결과값을 현재 표현식으로 설정
                    self.operator = None
                except ValueError:
                    self.result.set_value("Error: Invalid input")
                    self.reset_calculator_state()
            else:
                pass  # '=' 버튼이 의미 없는 경우 (예: 숫자 없이 바로 '=' 누름)
        # 'C' (Clear) 버튼 추가 (만약 레이아웃에 'C' 버튼이 있다면)
        # elif btn_text == 'C':
        #    self.reset_calculator_state()

    def reset_calculator_state(self):
        """계산기 상태를 초기화합니다."""
        self.current_expression = ""
        self.last_value = 0.0
        self.operator = None
        self.tape.set_value(" ")
        self.result.set_value("0")


ui.run()  # NiceGUI 애플리케이션을 시작합니다.
