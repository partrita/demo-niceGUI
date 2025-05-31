from nicegui import ui


class Calculator:
    def __init__(self):
        # 계산기 컴포넌트들을 담을 컨테이너를 만듭니다.
        # JustPy의 Calculator(jp.Div) 클래스 자체에 해당합니다.
        # NiceGUI의 ui.card를 사용하여 테두리와 배경을 가진 깔끔한 컨테이너를 생성합니다.
        with ui.card().classes("m-1 inline-block").style("width: 250px"):
            # 입력 테이프 (사용자가 입력하는 식을 보여줍니다)
            # JustPy의 self.tape에 해당하며, 읽기 전용으로 설정합니다.
            self.tape_display = ui.input(
                value=" ",
                readonly=True,
                classes="block p-2 m-2 border text-right text-sm bg-gray-200",
            ).style("width: 90%")

            # 결과 표시 (계산 결과를 보여줍니다)
            # JustPy의 self.result에 해당하며, 역시 읽기 전용입니다.
            self.result_display = ui.input(
                value="0",
                readonly=True,
                classes="block p-2 m-2 border text-2xl text-right",
            ).style("width: 90%")

            # 버튼 컨테이너 (나중에 숫자 및 연산자 버튼들이 추가될 곳)
            # JustPy의 d = jp.Div(classes="flex w-auto m-2", a=self)에 해당합니다.
            with ui.row().classes("w-auto m-2"):
                # JustPy의 jp.Input(text="type", a=d)는 이 예제에서 직접적으로 사용되지 않습니다.
                # JustPy의 b1 = jp.Button(text="cal!", a=d, click=self.cal_click)에 해당합니다.
                # NiceGUI에서는 ui.button을 사용하고, on_click 이벤트에 람다 함수를 연결합니다.
                # 이 람다 함수는 calculate 메서드를 호출하며, 필요한 디스플레이 컴포넌트를 전달합니다.
                ui.button("cal!", on_click=self.calculate).classes("m-1")

    # 계산 로직을 수행하는 메서드입니다.
    # JustPy의 cal_click 정적 메서드에 해당합니다.
    def calculate(self):
        try:
            # 현재 테이프 디스플레이의 값을 가져와 eval()로 계산합니다.
            # eval()은 보안에 취약할 수 있으므로 실제 계산기에서는 파서 라이브러리를 사용해야 합니다.
            # 계산 결과에 2를 곱하는 것은 JustPy 코드의 로직을 따릅니다.
            calculated_value = eval(self.tape_display.value) * 2
            self.result_display.set_value(str(calculated_value))
        except Exception as e:
            self.result_display.set_value("Error")
            print(f"Calculation error: {e}")


# NiceGUI 애플리케이션의 메인 페이지를 정의합니다.
@ui.page("/")
def calculator_test_page():
    # Calculator 클래스의 인스턴스를 생성하면
    # __init__ 메서드에서 정의된 NiceGUI 컴포넌트들이 페이지에 추가됩니다.
    Calculator()


ui.run()  # NiceGUI 애플리케이션을 시작합니다.
