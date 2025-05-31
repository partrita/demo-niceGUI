from nicegui import ui

# CSS 클래스 정의
INPUT_CLASSES = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
DISPLAY_CLASSES = "m-2 p-2 h-32 text-xl border-2"


class InputWithDiv:
    def __init__(self):
        # NiceGUI에서 컴포넌트들을 그룹화하려면 `with ui.column():` 또는 `with ui.row():`와 같은 컨테이너를 사용합니다.
        with ui.column():
            # 입력 필드 생성. JustPy의 self.in1 = jp.Input(...)에 해당합니다.
            # NiceGUI의 ui.input 컴포넌트를 사용하고 CSS 클래스를 적용합니다.
            text_input = ui.input(placeholder="여기에 입력하세요").classes(
                INPUT_CLASSES
            )

            # 입력 내용이 표시될 Div. JustPy의 self.in1.div = jp.Div(...)에 해당합니다.
            # NiceGUI에서는 ui.label을 사용하여 텍스트를 표시하고 클래스를 적용합니다.
            display_div = ui.label("여기에 입력하는 내용이 표시됩니다.").classes(
                DISPLAY_CLASSES
            )

            # 입력 필드와 표시 Div를 연결합니다.
            # JustPy의 in1.on("input", self.input_handler)에 해당합니다.
            # NiceGUI는 입력 필드의 'input' 이벤트가 발생할 때마다 람다 함수를 호출하고,
            # 이벤트 객체 `e`에서 현재 값(e.value)을 가져와 `display_div`의 텍스트를 업데이트합니다.
            text_input.on("input", lambda e: display_div.set_text(e.value))


@ui.page("/")  # 웹 페이지의 기본 경로를 정의합니다.
def input_demo_page():
    # 10개의 InputWithDiv 인스턴스를 생성합니다.
    # 각 인스턴스는 __init__ 메서드에서 NiceGUI 컴포넌트들을 생성하고 페이지에 추가합니다.
    for _ in range(10):
        InputWithDiv()


ui.run()  # NiceGUI 애플리케이션을 시작합니다.
