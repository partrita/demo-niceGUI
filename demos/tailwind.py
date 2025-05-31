from nicegui import ui


@ui.page("/")  # NiceGUI 페이지를 정의합니다.
def hello_world_page():
    # 단락에 적용할 Tailwind CSS 클래스입니다.
    my_paragraph_design = (
        "w-64 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    )

    # 1부터 10까지 반복하며 "Hello World!" 텍스트를 가진 라벨을 생성하고 클래스를 적용합니다.
    for i in range(1, 11):
        ui.label(f"{i}) Hello World!").classes(my_paragraph_design)


ui.run()  # NiceGUI 애플리케이션을 시작합니다.
