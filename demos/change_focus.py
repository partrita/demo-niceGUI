from nicegui import ui

# CSS 클래스 정의 (Tailwind CSS를 NiceGUI에서 사용하는 경우)
input_classes = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"


def on_key_down(e):
    key = e.key  # NiceGUI 이벤트 객체는 'key' 속성을 가집니다.
    sender = e.sender  # 이벤트를 발생시킨 컴포넌트

    if key == "Escape":
        sender.set_value("")  # 입력 필드 값 지우기
        sender.update()  # UI 업데이트
        return
    if key == "Enter":
        sender.blur()  # 현재 입력 필드의 포커스 해제

        # 다음 입력 필드로 포커스 이동 로직
        current_num = sender.num
        input_list = (
            sender.input_list
        )  # NiceGUI에서는 컴포넌트에 동적으로 속성을 추가할 수 있습니다.

        try:
            next_to_focus = input_list[current_num + 1]
        except IndexError:  # 마지막 필드인 경우 첫 번째 필드로 돌아갑니다.
            next_to_focus = input_list[0]

        next_to_focus.focus()  # 다음 입력 필드에 포커스 설정
        return
    # JustPy와 달리 NiceGUI에서는 True를 반환하여 페이지 업데이트를 막을 필요가 없습니다.
    # 이벤트 핸들러가 페이지를 직접 업데이트하지 않으면 기본적으로 업데이트되지 않습니다.


@ui.page("/")  # 웹 서버의 기본 경로에 페이지를 정의합니다.
def focus_test_page():
    with ui.column().classes("flex flex-col m-2").props('style="width: 600px"'):
        input_list = []
        number_of_fields = 5
        for i in range(1, number_of_fields + 1):
            # JustPy의 jp.Label(a=d, classes="m-2 p-2")에 해당
            # NiceGUI에서는 ui.label을 사용하여 텍스트 레이블을 만들고,
            # ui.input을 포함하여 레이블-입력 필드 쌍을 만듭니다.
            with ui.row().classes(
                "items-center m-2 p-2"
            ):  # 레이블과 입력 필드를 한 줄에 정렬
                ui.label(f"Field {i}")
                # JustPy의 jp.Input(...)에 해당
                in_field = (
                    ui.input(placeholder=f"{i} Type here")
                    .classes(input_classes)
                    .props('spellcheck="false"')
                )  # spellcheck 속성 추가

                # JustPy의 keydown=key_down, on("blur", my_blur)에 해당
                in_field.on("keydown", on_key_down)
                # blur 이벤트는 필요에 따라 추가할 수 있지만, 이 예제에서는 특별한 동작이 없으므로 생략합니다.
                # in_field.on('blur', on_blur)

                # JustPy에서처럼 input_list와 num을 동적으로 추가합니다.
                # NiceGUI에서는 컴포넌트 객체에 직접 속성을 추가하여 데이터를 연결할 수 있습니다.
                in_field.input_list = input_list
                in_field.num = i - 1
                input_list.append(in_field)


ui.run()  # NiceGUI 애플리케이션 시작
