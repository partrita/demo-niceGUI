from nicegui import ui
from starlette.requests import Request  # To access request details like session_id

# CSS classes for buttons and inputs (NiceGUI uses Tailwind CSS out of the box)
button_classes = "bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded m-2"
input_classes = "border m-2 p-2"

# In a real application, you might use app.storage.user or a database for persistent session data.
session_data = {}


# Define the main form page
@ui.page("/fill_form")
def fill_form_page():
    ui.label("Fill out the Form").classes("text-2xl font-bold m-4")

    # A container for the form elements, mimicking JustPy's Form component
    with ui.card().classes("m-1 p-1 w-64"):  # JustPy's jp.Form converted to ui.card
        # User Name Input
        ui.label("User Name").classes(
            "block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
        )
        # To get input values easily, we'll bind them to a dictionary or use an on_change handler
        username_input = ui.input(placeholder="User Name").classes("form-input")

        # Password Input
        ui.label("Password").classes(
            "block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2 mt-2"
        )
        password_input = ui.input(
            placeholder="Password",
            password=True,
            validation={"This field is required": lambda value: len(value) > 0},
        ).classes("form-input")

        # Checkbox for "Send me stuff"
        with ui.row().classes(
            "text-sm items-center"
        ):  # Use ui.row for inline alignment
            send_stuff_checkbox = ui.checkbox("")  # Checkbox itself
            ui.label("Send me stuff").classes("ml-2")  # Label for the checkbox

        # Submit button
        # NiceGUI's ui.button acts as a submit button. We'll handle the form data in its click handler.
        ui.button(
            "Submit Form",
            on_click=lambda: submit_form_data(
                username_input.value, password_input.value, send_stuff_checkbox.value
            ),
        ).classes(button_classes)


# This function will be called when the form is submitted
async def submit_form_data(username, password, send_stuff):
    # Get the current session ID (NiceGUI provides this via app.storage.user)
    # Note: app.storage.user is bound to the current user's session.
    # We'll use a simple mock for now, but in a real app, this is how you'd store per-user data.
    current_session_id = str(
        ui.context.session.id
    )  # Unique ID for the current user's session

    # Store form data for this session
    session_data[current_session_id] = {
        "username": username,
        "password": password,  # In a real app, never store passwords directly!
        "send_stuff": send_stuff,
    }
    print(
        f"Form Data for session {current_session_id}: {session_data[current_session_id]}"
    )

    # Redirect to the thank you page
    ui.navigate("/form_submitted")


# Define the form submission confirmation page
@ui.page("/form_submitted")
async def form_submitted_page(
    request: Request,
):  # NiceGUI allows passing starlette.Request for advanced access
    ui.label("Thank you for submitting the form").classes("text-xl m-2 p-2")

    current_session_id = str(ui.context.session.id)  # Get current session ID
    user_form_data = session_data.get(current_session_id, {})

    if user_form_data.get("send_stuff"):
        ui.label("We will send you stuff").classes("text-lg m-1 p-1")

    # Optionally, display submitted data (excluding password)
    ui.label("Submitted Data:").classes("text-lg font-semibold mt-4")
    for key, value in user_form_data.items():
        if key != "password":  # Don't display password
            ui.label(f"{key.replace('_', ' ').title()}: {value}").classes("m-1 p-1")


# Run the NiceGUI application
ui.run()
