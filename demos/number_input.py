from nicegui import ui

# CSS 클래스 정의
input_classes = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
p_classes = "m-2 p-2 h-32 text-xl border-2"


@ui.page("/")  # 웹 페이지의 기본 경로를 설정합니다.
def input_demo_page():
    # 숫자 입력 필드를 생성합니다. (JustPy의 jp.Input(type="number")에 해당)
    # on_input 이벤트 핸들러를 연결하여 입력 값이 변경될 때마다 특정 동작을 수행합니다.
    number_input = ui.input(type="number", placeholder="여기에 입력하세요").classes(
        input_classes
    )

    # 입력된 내용이 표시될 영역을 생성합니다. (JustPy의 jp.Div에 해당)
    display_area = ui.label("여기에 입력하는 내용이 표시됩니다.").classes(p_classes)

    # 입력 필드와 표시 영역을 연결합니다. (JustPy의 in1.on("input", my_input)에 해당)
    # 입력 필드의 'input' 이벤트가 발생하면, 해당 이벤트의 값(e.value)을 가져와
    # display_area의 텍스트를 업데이트합니다.
    number_input.on("input", lambda e: display_area.set_text(e.value))


ui.run()  # NiceGUI 애플리케이션을 시작합니다.
