from nicegui import ui

# CSS classes for the circular div (NiceGUI uses Tailwind CSS out of the box)
DIV_CLASSES = (
    "rounded-full bg-blue-500 text-white h-32 w-32 flex items-center justify-center"
)


# Event handler for click events
def on_click(e):
    # e.sender refers to the UI element that triggered the event (the div in this case)
    e.sender.set_text("I was clicked")
    e.sender.classes(replace="bg-blue-500")  # Change background color
    print(f"Event Type: {e.type}")  # Access event type (e.g., 'click')
    print(f"Event Data: {e.args}")  # Access raw event arguments
    # NiceGUI provides structured event objects, so directly accessing msg["event_type"] is less common.


# Event handler for mouseenter (mouse over) events
def on_mouseenter(e):
    e.sender.set_text("Mouse entered")
    e.sender.classes(replace="bg-red-500")  # Change background color


# Event handler for mouseleave (mouse out) events
def on_mouseleave(e):
    e.sender.set_text("Mouse left")
    e.sender.classes(replace="bg-teal-500")  # Change background color


@ui.page("/")  # Define the main page at the root URL
def event_demo_page():
    ui.label("Event Demo").classes("text-3xl font-bold m-4")

    # Create a ui.label which acts as the div
    # Attach event handlers using .on() method for various events
    ui.label(text="Not clicked yet").classes(DIV_CLASSES).on("click", on_click).on(
        "mouseenter", on_mouseenter
    ).on("mouseleave", on_mouseleave)


ui.run()  # Start the NiceGUI application
