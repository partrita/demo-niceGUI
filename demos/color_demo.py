from nicegui import ui


def on_color_change(e):
    # e.value는 Input 컴포넌트의 현재 값을 담고 있습니다 (여기서는 선택된 색상).
    # e.sender는 이벤트를 발생시킨 Input 컴포넌트 객체입니다.
    # NiceGUI 컴포넌트의 스타일을 변경하려면 .props()를 사용하거나,
    # ui.run_javascript를 통해 직접 CSS를 조작할 수 있습니다.
    # 여기서는 ui.label의 'style' 속성을 직접 업데이트하는 방식을 사용합니다.
    e.sender.linked_label.style(f"color:{e.value}")
    e.sender.linked_label.set_text(f"The color of this text is: {e.value}")


@ui.page("/")  # 웹 서버의 기본 경로에 페이지를 정의합니다.
def color_demo_page():
    # NiceGUI의 ui.input 컴포넌트를 사용하고 type="color"로 설정합니다.
    # on_change 이벤트 핸들러를 연결하여 값이 변경될 때마다 on_color_change 함수를 호출합니다.
    color_input = ui.input(type="color").on("change", on_color_change)

    # NiceGUI의 ui.label을 사용하여 텍스트를 표시할 Div를 만듭니다.
    # 이 label 컴포넌트를 color_input에 연결하여 이벤트 핸들러에서 접근할 수 있도록 합니다.
    text_label = ui.label("Click box above to change color")

    # color_input 컴포넌트에서 text_label에 접근할 수 있도록 연결합니다.
    color_input.linked_label = text_label


ui.run()  # NiceGUI 애플리케이션 시작
