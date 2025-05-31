from nicegui import ui


@ui.page("/")  # 웹 서버의 기본 경로에 페이지를 정의합니다.
def joint_edit_page():
    # NiceGUI의 ui.editor는 Quasar QEditor 컴포넌트를 사용하며,
    # kitchen_sink 옵션은 'toolbar' props에 여러 기능을 지정하는 것으로 대체됩니다.
    # 높이는 'height' props로 설정합니다.
    ui.editor().props(
        'toolbar="bold italic underline strikethrough subscript superscript | '
        "align justify | outdent indent | "
        "undo redo | print fullscreen | "
        "token list ordered list quote hr | "
        "link image code | "
        "font-size font-family | "
        "v-icon v-img v-btn | "
        'textColor highlightColor"'
    ).props('height="94vh"')


ui.run()
