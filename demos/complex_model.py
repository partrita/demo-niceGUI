from nicegui import ui

# Tailwind CSS 클래스를 정의합니다.
INPUT_CLASSES = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"


class MyOutputDiv:
    def __init__(
        self, text_model_object, text_model_key, repeat: int, initial_text: str
    ):
        self.text_model_object = text_model_object
        self.text_model_key = text_model_key
        self.repeat = repeat
        self.initial_text = initial_text

        self.output_label = ui.label(self.initial_text)
        self.output_label.bind_text_from(self, "computed_text")

    @property
    def computed_text(self):
        raw_value = self.text_model_object.get(self.text_model_key)
        if raw_value and str(raw_value).isdigit():
            return str(int(raw_value) * self.repeat)
        return self.initial_text


@ui.page("/")
def model_demo_page():
    data_model = {"text": ""}

    with ui.column():
        repeat_factor = 2

        with ui.column():
            ui.label("Output:")
            MyOutputDiv(
                text_model_object=data_model,
                text_model_key="text",
                repeat=repeat_factor,
                initial_text="Yada Yada",
            )

        ui.input(placeholder="Type here").classes(INPUT_CLASSES).bind_value(
            data_model, "text"
        )


ui.run()
