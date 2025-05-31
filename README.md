# Learn NiceGUI

[NiceGUI 공식 웹사이트](https://NiceGUI.io/)


## 소개

**NiceGUI**는 프론트엔드 프로그래밍이 필요 없는 객체 지향적이고 컴포넌트 기반의 고수준 Python 웹 프레임워크입니다. 단 몇 줄의 파이썬 코드만으로도 JavaScript 프로그래밍 없이 인터랙티브한 웹사이트를 만들 수 있습니다.

> NiceGUI를 가장 잘 이해하는 방법은 다양한 예제를 포함하고 있는 튜토리얼을 따라 해보는 것입니다.


## 설치 방법

가장 먼저 의존성 관리를 위해 **uv**가 필요합니다. 터미널을 열고 다음 명령어를 실행하여 설치합니다.

```bash
pip install uv
```

설치가 완료되면, NiceGUI 데모 프로젝트를 클론하고 필요한 의존성을 동기화합니다.

```bash
gh repo clone partrita/demo-niceGUI
cd demo-niceGUI
uv sync
```

-----

## 프로그램 실행

프로그램을 실행하려면, `main.py` 파일을 생성하고 그 안에 코드를 작성해야 합니다. 예시로 `demos/main.py` 파일을 실행하는 방법은 다음과 같습니다.

```bash
uv run python demos/main.py
```

명령어를 실행하면 NiceGUI 애플리케이션이 시작되고, 웹 브라우저에서 접근할 수 있는 로컬 주소가 터미널에 표시됩니다. 일반적으로 `http://127.0.0.1:8080`과 같은 주소가 나타날 것입니다. 해당 주소로 접속하여 NiceGUI로 만든 웹 애플리케이션을 확인해 보세요.