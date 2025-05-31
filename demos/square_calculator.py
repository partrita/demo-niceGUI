from nicegui import ui

# CSS 클래스 정의 (JustPy의 p_classes와 유사)
DISPLAY_CLASSES = "m-2 p-2 h-32 text-xl border-2"


@ui.page("/")  # 웹 페이지의 기본 경로를 정의합니다.
def square_input_page():
    # NiceGUI에서 반응형 데이터를 관리하는 방법입니다.
    # ui.input의 값과 ui.label의 텍스트가 이 `data` 딕셔너리에 바인딩됩니다.
    data = {"input1_value": 0, "input2_value": 0, "result": 0}

    # 결과가 표시될 영역을 생성합니다. (JustPy의 result_div와 유사)
    # .bind_text_from()을 사용하여 data 딕셔너리의 'result' 값에 단방향 바인딩합니다.
    # data['result'] 값이 변경되면 이 레이블의 텍스트도 자동으로 업데이트됩니다.
    ui.label(text="여기에 결과가 표시됩니다.").classes(DISPLAY_CLASSES).bind_text_from(
        data, "result"
    )

    # 첫 번째 숫자 입력 필드 생성 (JustPy의 in1과 유사)
    # .bind_value()를 사용하여 data 딕셔너리의 'input1_value'와 양방향 바인딩합니다.
    # 입력 필드에 값이 입력될 때마다 data['input1_value']가 업데이트됩니다.
    # on_change 이벤트에서 calculate_result 함수를 호출하여 즉시 계산을 수행합니다.
    ui.input(type="number", placeholder="첫 번째 숫자를 입력하세요").bind_value(
        data, "input1_value"
    ).on("change", lambda: calculate_result(data))

    # 두 번째 숫자 입력 필드 생성 (JustPy의 in2와 유사)
    # 마찬가지로 .bind_value()를 사용하여 'input2_value'와 양방향 바인딩합니다.
    # on_change 이벤트에서 calculate_result 함수를 호출합니다.
    ui.input(type="number", placeholder="두 번째 숫자를 입력하세요").bind_value(
        data, "input2_value"
    ).on("change", lambda: calculate_result(data))


# 입력 값이 변경될 때마다 호출될 계산 함수입니다.
def calculate_result(data):
    try:
        # data 딕셔너리에서 현재 입력 값을 가져와 곱셈을 수행합니다.
        # 값이 숫자가 아닐 경우를 대비하여 int() 변환을 시도합니다.
        data["result"] = int(data["input1_value"]) * int(data["input2_value"])
    except (ValueError, TypeError):
        # 숫자가 아닌 값이 입력될 경우 결과 메시지를 설정합니다.
        data["result"] = "유효하지 않은 입력"


ui.run()  # NiceGUI 애플리케이션을 시작합니다.
