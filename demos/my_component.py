from nicegui import ui


class InputWithDiv:
    def __init__(self):
        with ui.column():
            # 첫 번째 입력 필드
            # on_input 이벤트 핸들러를 람다 함수로 직접 연결합니다.
            # 이 필드는 아래 display_div와 직접 연결되지 않으므로,
            # 입력 시 display_div의 텍스트가 변경되지 않습니다.
            self.in1 = ui.input(placeholder="type me")

            # 두 번째 입력 필드
            # 이 필드의 입력에 따라 display_div의 텍스트가 변경됩니다.
            self.in2 = ui.input(placeholder="type me2")

            # 입력 내용이 표시될 Div (NiceGUI에서는 ui.label로 대체)
            self.display_div = ui.label("What do you type?")

            # 두 번째 입력 필드(self.in2)의 on_input 이벤트에 핸들러 연결
            # 람다 함수를 사용하여 self.display_div의 텍스트를 self.in2.value로 업데이트합니다.
            self.in2.on("input", lambda e: self.display_div.set_text(e.value))


@ui.page("/")  # 웹 서버의 기본 경로에 페이지를 정의합니다.
def input_demo_page():
    # InputWithDiv 클래스의 인스턴스를 생성하면
    # __init__ 메서드에서 NiceGUI 컴포넌트들이 자동으로 페이지에 추가됩니다.
    InputWithDiv()


ui.run()
