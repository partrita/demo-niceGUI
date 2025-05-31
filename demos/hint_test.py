from nicegui import ui


@ui.page("/")
def hint_test_page():
    with ui.column().classes("q-pa-md q-gutter-lg").props("style='max-width: 300px'"):
        ui.input(label="My Field", hint="This is my hint.")

        ui.select(
            ["Google", "Facebook", "Twitter", "Apple", "Oracle"],  # options
            label="Select Company",
            color="orange",
            clearable=True,
            standout=True,
            bottom_slots=True,
            counter=True,
            hint="My hint",
        )


ui.run()
