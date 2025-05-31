from nicegui import ui

# CSS classes for styling
BUTTON_CLASSES = (
    "w-32 m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
)
INPUT_CLASSES = "m-2 bg-gray-200 appearance-none border-2 border-gray-200 rounded xtw-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
DIV_CLASSES = "m-2 p-2 h-32 text-xl border-2 overflow-auto"


@ui.page("/")
def input_demo_page():
    # NiceGUI manages reactive data typically through simple Python objects (like a dict here).
    # This 'data' dict will be our central source of truth for the bound elements.
    data = {"text": "Initial text"}

    # Reset button: Clicking it clears the 'text' in our data model.
    # When data['text'] changes, all bound elements will automatically update.
    ui.button("Reset", on_click=lambda: data.update(text="")).classes(BUTTON_CLASSES)

    ui.separator()  # Horizontal line, similar to JustPy's jp.Hr()

    # Create 5 input fields, all bound to the same 'text' key in our 'data' dict.
    # .bind_value(data, 'text') creates a two-way binding:
    # 1. Changing the input's value updates data['text'].
    # 2. Changing data['text'] (e.g., via the Reset button) updates the input's value.
    for _ in range(5):
        ui.input(placeholder="Please type here").classes(INPUT_CLASSES).bind_value(
            data, "text"
        )

    # Create 3 display divs (labels), all bound to the same 'text' key.
    # .bind_text_from(data, 'text') creates a one-way binding:
    # 1. Changing data['text'] updates the label's text.
    # (The label itself doesn't directly change data['text']).
    for _ in range(3):
        ui.label().classes(DIV_CLASSES).bind_text_from(data, "text")


ui.run()
