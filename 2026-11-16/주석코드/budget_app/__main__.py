# 실행 진입점: python -m budget_app이 이 파일을 실행합니다.
# 명령 처리 결과를 운영체제의 종료 코드로 전달합니다.
# CLI의 main 함수를 모듈 실행 진입점에 연결합니다.
from .cli import main

# main의 0/1/130 반환값을 실제 프로세스 종료 코드로 전달합니다. 인자 오류는 Parser가 2로 종료합니다.
raise SystemExit(main())
