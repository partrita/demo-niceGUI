from nicegui import ui


def check_test_page():
    # NiceGUI에서는 'reactive' 속성을 가진 객체를 바인딩할 수 있습니다.
    # 여기서는 간단한 dict를 사용하여 값을 저장하고 NiceGUI가 이를 감지하도록 합니다.
    data = {"checked": True}

    # NiceGUI에서는 레이블과 체크박스를 한 줄에 배치하기 위해 ui.row를 사용합니다.
    with ui.row().classes("m-2 p-2 items-center"):  # items-center로 세로 중앙 정렬
        # NiceGUI의 ui.checkbox는 'text' 인자로 레이블을 직접 받을 수 있습니다.
        # 'bind_value'를 사용하여 data['checked']와 체크박스의 상태를 양방향으로 바인딩합니다.
        ui.checkbox(
            "Click to get stuff",  # JustPy의 caption = jp.Span(...)에 해당
            value=data["checked"],  # 초기 값 설정
            on_change=lambda e: data.update(
                checked=e.value
            ),  # 값 변경 시 data 딕셔너리 업데이트
        ).classes("m-2 p-2 form-checkbox")

    # NiceGUI에서는 ui.input의 value를 data['checked']에 바인딩합니다.
    # 이렇게 하면 체크박스의 상태에 따라 입력 필드의 값이 자동으로 변경됩니다.
    ui.input(
        placeholder="Checkbox state",
        value=str(data["checked"]),  # 초기 값을 문자열로 설정 (True/False)
    ).classes("border block m-2 p-2").bind_value_from(data, "checked").bind_value_to(
        data, "checked"
    )
    # .bind_value_from()과 .bind_value_to()를 사용하여 양방향 바인딩을 명시적으로 설정합니다.
    # ui.input은 기본적으로 텍스트를 받으므로, boolean 값을 문자열로 변환하여 표시합니다.


@ui.page("/")  # 웹 서버의 기본 경로에 페이지를 정의합니다.
def main_page():
    check_test_page()


ui.run()  # NiceGUI 애플리케이션 시작
