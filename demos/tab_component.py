from nicegui import ui

# 일반적인 Quasar/Tailwind CSS 클래스
# NiceGUI는 이러한 클래스를 기본적으로 지원합니다.
# button_classes = "bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded m-2"
# input_classes = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"

# Highcharts 데이터 정의 (여기서는 사용되지 않으므로 그대로 둡니다)
my_chart_options = """
{
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Fruit Consumption'
        },
        xAxis: {
            categories: ['Apples', 'Bananas', 'Oranges']
        },
        yAxis: {
            title: {
                text: 'Fruit eaten'
            }
        },
        series: [{
            name: 'Jane',
            data: [1, 0, 4],
            animation: false
        }, {
            name: 'John',
            data: [5, 7, 3],
            animation: false
        }]
}
"""

# 강아지 사진 ID
pics_french_bulldogs = ["5458", "7806", "5667", "4860"]
pics_papillons = ["5037", "2556", "7606", "8241"]


# 탭 변경 이벤트 핸들러 (JustPy의 tab_change와 유사)
# NiceGUI의 ui.tabs는 `on_change` 이벤트를 가집니다.
def on_tab_change(e):
    print(f"탭 변경됨: 이전 탭: {e.args.get('previous_tab')}, 새 탭: {e.value}")


@ui.page("/")
def tab_comp_test_page():
    # NiceGUI의 반응형 데이터 모델입니다. JustPy의 wp.data={"tab": "id2556"}에 해당합니다.
    # 이 딕셔너리의 'current_tab_id' 값이 변경되면, 여기에 바인딩된 UI 컴포넌트들이 자동으로 업데이트됩니다.
    data = {"current_tab_id": "id2556"}

    ui.label("차트 탭").classes("text-xl font-bold mt-4")
    # 첫 번째 탭 섹션: Highcharts 차트
    # ui.tabs와 ui.tab_panels는 함께 작동하여 탭 UI를 생성합니다.
    with ui.tabs().props("animated swipeable").classes("w-3/4 m-4") as tabs:
        chart_types = ["bar", "column", "line", "spline"]
        for chart_type in chart_types:
            ui.tab(f"id{chart_type}", label=f"{chart_type.capitalize()}")

    with ui.tab_panels(tabs).props(
        'animated swipeable style="height: 550px; position: relative; overflow: hidden;"'
    ):
        for chart_type in chart_types:
            with ui.tab_panel(f"id{chart_type}").classes(
                "flex items-center justify-center bg-white"
            ):
                # Highcharts 차트를 동적으로 생성하고 업데이트합니다.
                # NiceGUI의 ui.chart는 Highcharts를 지원하며, options 속성을 통해 설정을 전달합니다.
                # 'chart = ' 부분을 제거하여 F841 오류를 해결합니다.
                ui.chart(
                    {
                        "chart": {"type": chart_type},
                        "title": {"text": f"Chart of Type {chart_type.capitalize()}"},
                        "subtitle": {"text": f"Subtitle {chart_type.capitalize()}"},
                        "xAxis": {"categories": ["Apples", "Bananas", "Oranges"]},
                        "yAxis": {"title": {"text": "Fruit eaten"}},
                        "series": [
                            {"name": "Jane", "data": [1, 0, 4], "animation": False},
                            {"name": "John", "data": [5, 7, 3], "animation": False},
                        ],
                    }
                ).classes("m-2 p-2 border").props('style="width: 1000px;"')

    ui.separator()
    ui.label("강아지 사진 탭").classes("text-xl font-bold mt-4")

    # 두 번째 탭 섹션: 강아지 사진 (Papillons)
    # JustPy의 TabsPills와 유사한 스타일을 위해 클래스를 직접 적용합니다.
    with ui.row().classes("w-full"):  # 두 개의 탭 그룹을 나란히 배치하기 위한 컨테이너
        with ui.column().classes("w-1/2 m-4"):
            with ui.tabs().props("animated swipeable").classes(
                "flex flex-wrap border-b"
            ) as dog_tabs_papillons:
                for pic_id in pics_papillons:
                    # 'tab' 데이터 모델에 바인딩
                    ui.tab(f"id{pic_id}", label=f"Pic {pic_id}")

            with ui.tab_panels(dog_tabs_papillons).props(
                'animated swipeable style="height: 550px; position: relative; overflow: hidden;"'
            ).bind_value(data, "current_tab_id").on(
                "change", on_tab_change
            ):  # 탭 변경 이벤트 핸들러 연결
                for pic_id in pics_papillons:
                    with ui.tab_panel(f"id{pic_id}").classes(
                        "flex items-center justify-center bg-white"
                    ):
                        ui.image(
                            f"https://images.dog.ceo/breeds/papillon/n02086910_{pic_id}.jpg"
                        )

        # 세 번째 탭 섹션: 강아지 사진 (French Bulldogs)
        with ui.column().classes("w-1/2 m-4"):
            # Pills 스타일을 위한 클래스 적용
            with ui.tabs().props("animated swipeable").classes(
                "flex flex-wrap border-b"
            ) as dog_tabs_bulldogs:
                for pic_id in pics_french_bulldogs:
                    ui.tab(f"id{pic_id}", label=f"Pic {pic_id}")

            with ui.tab_panels(dog_tabs_bulldogs).props(
                'animated swipeable style="height: 550px; position: relative; overflow: hidden;"'
            ).on("change", on_tab_change):  # 탭 변경 이벤트 핸들러 연결
                for pic_id in pics_french_bulldogs:
                    with ui.tab_panel(f"id{pic_id}").classes(
                        "flex items-center justify-center bg-white"
                    ):
                        ui.image(
                            f"https://images.dog.ceo/breeds/bulldog-french/n02108915_{pic_id}.jpg"
                        )

    # 탭 ID를 직접 입력하여 탭을 변경할 수 있는 입력 필드
    # JustPy의 input_classes는 NiceGUI의 .classes()로 적용
    # data['current_tab_id']와 양방향 바인딩하여 텍스트 입력으로 탭 변경 가능
    ui.input(label="탭 ID 입력", placeholder="예: idbar 또는 id2556").classes(
        "w-1/3 m-2"
    ).bind_value(data, "current_tab_id")


ui.run()
