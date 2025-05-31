from nicegui import ui


# '/'(루트) 경로를 처리하는 함수입니다.
@ui.page("/")
def html_comps_page():
    # 기울임꼴 텍스트를 표시합니다.
    ui.label("Text in italic").classes("italic")
    # 굵게 표시된 텍스트를 표시합니다.
    ui.label("Text in bold").classes("font-bold")
    # 굵게 표시된 한글 텍스트를 표시합니다.
    ui.label("한글 입력").classes("font-bold")


# '/bye' 경로를 처리하는 함수입니다.
@ui.page("/bye")
def bye_function_page():
    # "Goodbye!" 텍스트를 크게 표시합니다.
    ui.label("Goodbye!").classes("text-5xl m-2")


# '/hello' 경로를 처리하는 함수입니다.
@ui.page("/hello")
def hello_function_page():
    # "Hello there!" 텍스트를 크게 표시합니다.
    ui.label("Hello there!").classes("text-5xl m-2")


# NiceGUI 애플리케이션을 시작합니다.
ui.run()
