from nicegui import ui


@ui.page("/")  # 웹 서버의 기본 경로에 페이지를 정의합니다.
def input_demo_page():
    # NiceGUI에서는 ui.label이나 ui.input 등 여러 컴포넌트에서 공유할
    # 반응형 데이터를 일반 Python 딕셔너리로 관리합니다.
    # 'result' 키는 이 예시에서는 사용되지 않으므로 생략했습니다.
    data = {"text": ""}

    # 입력 필드 CSS 클래스 정의
    input_classes = "m-2 bg-gray-200 border-2"

    # 입력 필드 생성 (JustPy의 jp.Input(...)에 해당)
    # NiceGUI의 ui.input 컴포넌트를 사용하고, bind_value 메서드로 'data' 딕셔너리의 'text' 키와 양방향 바인딩합니다.
    # 이렇게 하면 입력 필드에 텍스트를 입력하면 data['text']가 자동으로 업데이트됩니다.
    ui.input(placeholder="please type").classes(input_classes).bind_value(data, "text")

    # 입력 내용이 표시될 Div (JustPy의 jp.Div(model=[wp, "text"], ...)에 해당)
    # NiceGUI의 ui.label 컴포넌트를 사용하고, bind_text_from 메서드로 'data' 딕셔너리의 'text' 키와 단방향 바인딩합니다.
    # data['text']의 값이 변경되면 이 레이블의 텍스트가 자동으로 업데이트됩니다.
    ui.label().bind_text_from(data, "text")


ui.run()
