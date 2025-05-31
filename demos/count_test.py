from nicegui import ui
import asyncio

# 버튼에 사용할 Tailwind CSS 클래스 정의
button_classes = "m-2 p-2 text-orange-700 bg-white hover:bg-orange-200 hover:text-orange-500 border focus:border-orange-500 focus:outline-none"


async def count_down_animation(
    start_num: int, animation: str, button_to_hide: ui.button
):
    """
    카운트다운 애니메이션을 실행하고 UI를 동적으로 업데이트합니다.
    """
    # 버튼 숨기기
    button_to_hide.visible = False

    # 기존 카운트다운 Div/Label이 있다면 제거합니다.
    # NiceGUI에서는 'clear()'나 'remove()'를 통해 자식 컴포넌트를 제거할 수 있습니다.
    # 여기서는 새로운 컴포넌트를 생성하여 대체하는 방식을 사용합니다.
    # 이전 카운트다운 레이블을 참조하여 제거하거나, 아니면 단순히 새롭게 생성합니다.
    # 실제 애플리케이션에서는 해당 컨테이너를 .clear()하는 것이 더 나을 수 있습니다.
    # 예를 들어, with ui.column() as countdown_container: ... countdown_container.clear()

    # 'bomb' 아이콘 생성
    bomb_icon = ui.icon("bomb").classes("inline-block text-5xl ml-1 mt-1")

    # 카운트다운 숫자를 표시할 라벨 생성
    # .props()를 사용하여 스타일을 적용할 수 있습니다.
    # 여기서는 Tailwind CSS/Animate.css 클래스를 직접 사용합니다.
    countdown_label = ui.label("").classes(
        f"text-center m-4 p-4 text-6xl text-red-600 bg-blue-500 {animation} faster"
    )

    # 카운트다운 시작
    for i in range(start_num, 0, -1):
        countdown_label.set_text(str(i))
        await asyncio.sleep(1)

    # 카운트다운 종료 후 "Boom!" 표시 및 스타일 변경
    countdown_label.set_text("Boom!")
    countdown_label.classes(
        replace="text-red-500 bg-white zoomIn"
    )  # 기존 클래스 교체 및 새 애니메이션 추가
    bomb_icon.classes(replace="text-red-700")  # 아이콘 색상 변경

    # 일정 시간 후 컴포넌트 제거 (선택 사항)
    await asyncio.sleep(2)
    bomb_icon.set_visibility(False)  # 아이콘 숨기기
    countdown_label.set_visibility(False)  # 레이블 숨기기

    # 버튼 다시 보이게 하기
    button_to_hide.visible = True


@ui.page("/")  # 웹 서버의 기본 경로에 페이지를 정의합니다.
def count_test_page(num: int = 10, animation: str = "flip"):
    """
    카운트다운 테스트 페이지를 설정합니다.
    URL 쿼리 파라미터(예: /?num=5&animation=bounce)를 통해 시작 숫자와 애니메이션을 설정할 수 있습니다.
    """
    ui.label("Countdown Timer Demo").classes("text-3xl font-bold m-4")

    # 카운트다운 시작 버튼
    # on_click 이벤트 핸들러에서 비동기 함수를 호출합니다.
    # 이 버튼 객체 자체를 count_down_animation 함수에 전달하여 가시성을 제어할 수 있도록 합니다.
    start_button = ui.button(
        "Start Countdown",
        on_click=lambda: asyncio.create_task(
            count_down_animation(num, animation, start_button)
        ),
    ).classes(button_classes)


ui.run()  # NiceGUI 애플리케이션 시작
