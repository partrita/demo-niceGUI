from nicegui import ui, app

# CSS 클래스 정의
input_classes = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
p_classes = "m-2 p-2 h-32 text-xl border-2"

# 앱 아이콘 설정 (JustPy의 wp.favicon에 해당)
app.favicon = "./favicon.ico"


@ui.page("/")  # 기본 경로에 페이지 정의 (JustPy의 wp = jp.WebPage()에 해당)
def input_demo_page():
    # 페이지 제목 설정 (JustPy의 wp.title에 해당)
    ui.page.title = "input demo"

    # JustPy의 debug = True는 NiceGUI에서 로깅 설정으로 대체될 수 있지만,
    # 일반적으로 개발 중에는 기본적으로 상세 로그가 출력됩니다.

    # 입력 필드 생성 (JustPy의 in2 = jp.Input(...)에 해당)
    # on_input 이벤트 핸들러를 연결합니다.
    text_input = ui.input(placeholder="Please type here").classes(input_classes)

    # 입력 내용이 표시될 Div (NiceGUI에서는 ui.label 또는 ui.html로 대체)
    # JustPy의 in2.div = jp.Div(...)에 해당
    display_div = ui.label(
        "What you type will show, 입력하는 것이 보여집니다."
    ).classes(p_classes)

    # 입력 필드와 Div를 연결 (JustPy의 in2.on("input", my_input)에 해당)
    # NiceGUI의 이벤트 핸들러는 이벤트 객체(e)를 받습니다.
    # e.value는 현재 입력 필드의 값이고, display_div.set_text()로 레이블을 업데이트합니다.
    text_input.on("input", lambda e: display_div.set_text(e.value))


ui.run()
