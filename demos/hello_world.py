from nicegui import ui


@ui.page("/")
def hello_world_page():
    ui.label("Hello World!")


ui.run()
