from nicegui import ui
import random

# Raw HTML string for the toolbar (NiceGUI can embed this directly)
html_string = """
  <div class="q-pa-md q-gutter-y-sm">
    <q-toolbar class="text-primary">
      <q-btn flat round dense icon="menu" />
      <q-toolbar-title>
        Toolbar
      </q-toolbar-title>
      <q-btn flat round dense icon="more_vert" />
    </q-toolbar>
"""


# NiceGUI는 컴포넌트의 가시성/클래스/텍스트를 직접 제어합니다.
# msg.page.dark와 같은 전역 페이지 속성은 NiceGUI에서 ui.dark.toggle()로 직접 제어합니다.
def my_click(e):
    # 클릭된 버튼(e.sender)의 색상을 랜덤으로 변경합니다.
    chosen_color = random.choice(
        [
            "primary",
            "secondary",
            "accent",
            "dark",
            "positive",
            "negative",
            "info",
            "warning",
        ]
    )
    e.sender.props(f'color="{chosen_color}"')  # 버튼의 색상 속성 변경
    e.sender.text = chosen_color  # 버튼의 라벨 텍스트 변경

    # 페이지의 다크 모드를 토글합니다.
    ui.dark.toggle()


@ui.page("/")  # 웹 페이지의 기본 경로를 정의합니다.
def quasar_example_page():
    # NiceGUI는 기본적으로 Tailwinds CSS를 지원합니다.
    # JustPy의 wp.QuasarPage(dark=True)에 해당하며, NiceGUI는 ui.dark.enable()로 다크 모드를 활성화합니다.
    ui.dark.enable()

    # HTML 문자열을 페이지에 삽입합니다. (JustPy의 jp.parse_html에 해당)
    ui.html(html_string)

    # 버튼들을 위한 컨테이너 div를 생성합니다. (JustPy의 jp.Div에 해당)
    with ui.column().classes("q-pa-md q-gutter-sm"):
        # JustPy의 jp.QBtn은 NiceGUI의 ui.button으로 변환됩니다.
        # on_click 이벤트 핸들러를 my_click 함수로 연결합니다.
        ui.button(text="On Left", icon="mail", color="primary", on_click=my_click)
        ui.button(
            text="On Right", icon_right="mail", color="secondary", on_click=my_click
        )
        ui.button(
            text="On Left and Right",
            icon="mail",
            icon_right="send",
            color="red",
            on_click=my_click,
        )

        ui.separator()  # 수평선 추가 (JustPy의 jp.Br 대신 더 시각적인 구분)

        ui.button(
            text="Stacked", icon="phone", stack=True, color="purple", on_click=my_click
        )
        # JustPy의 glossy=True는 NiceGUI에서 Quasar props로 직접 전달할 수 있습니다.
        ui.button(
            text="Stacked Glossy",
            icon="phone",
            stack=True,
            glossy=True,
            color="purple",
            on_click=my_click,
        )


ui.run()  # NiceGUI 애플리케이션을 시작합니다.
