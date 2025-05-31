from nicegui import ui


def create_toolbar():
    with ui.header().classes("bg-grey-3"):
        with ui.button(flat=True, round=True, dense=True).props('icon="menu"'):
            with ui.menu().props('min-width="100px"'):
                ui.menu_item("About", on_click=lambda: ui.navigate("/about"))
                ui.separator()
                ui.menu_item("Help", on_click=lambda: ui.navigate("/tool"))
        ui.label("Toolbar").classes("q-toolbar__title")
        ui.button(flat=True, round=True, dense=True).props('icon="more_vert"')


# Define the main index page
@ui.page("/")
def index_page():
    # Tailwinds classes are supported by default in NiceGUI
    create_toolbar()
    ui.label("Index page").classes("text-5xl m-2")


# Define the about page
@ui.page("/about")
def about_page():
    create_toolbar()
    ui.label("Hello there!").classes("text-5xl m-2")


# Define a placeholder page for /tool (or help)
@ui.page("/tool")
def tool_page():
    create_toolbar()
    ui.label("Help page").classes("text-5xl m-2")


ui.run()
