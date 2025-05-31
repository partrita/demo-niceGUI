from nicegui import ui
import time
import asyncio

clock_label = None  # 전역 변수로 선언하여 clock_counter에서 접근할 수 있도록 초기화


async def clock_counter():
    """
    1초마다 현재 시간을 업데이트하는 비동기 함수.
    """
    global clock_label  # 전역 변수에 접근하기 위해 global 키워드 사용
    while True:
        current_time = time.strftime("%a, %d %b %Y, %H:%M:%S", time.localtime())
        if clock_label:  # clock_label이 None이 아닌지 확인
            clock_label.set_text(current_time)  # NiceGUI 컴포넌트의 텍스트 업데이트
        await asyncio.sleep(1)  # 1초 대기


@ui.page("/")  # 웹 서버의 기본 경로에 페이지를 정의합니다.
async def clock_test_page():
    """
    시계 페이지를 설정하고 백그라운드 작업을 시작합니다.
    """
    global clock_label  # 전역 변수에 접근
    # 초기 텍스트는 "Loading..."으로 설정하고, 클래스를 적용합니다.
    clock_label = ui.label("Loading...").classes(
        "text-5xl m-1 p-1 bg-gray-300 font-mono"
    )

    # NiceGUI에서는 페이지가 로드될 때 백그라운드 작업을 시작하기 위해
    # asyncio.create_task를 사용합니다.
    # 이렇게 하면 페이지 로딩과 별개로 clock_counter가 독립적으로 실행됩니다.
    asyncio.create_task(clock_counter())


ui.run()  # NiceGUI 애플리케이션 시작
