# 공통 처리 계층: 실행 함수를 감싸 오류·종료 코드·시간 측정을 한곳에 모읍니다.
# 모델과 서비스는 오류를 발생시키고, 이 데코레이터는 사용자에게 안내합니다.
"""명령 처리의 예외 경계와 실행 시간 로그를 분리한다."""
# 타입 힌트 평가를 늦춰 클래스 자신의 타입과 전방 참조를 안전하게 표기합니다.
from __future__ import annotations

# 쉼표·인용·개행을 직접 나누지 않고 표준 CSV 규칙으로 처리합니다.
import csv
# verbose 옵션에서 실행 결과와 소요 시간 로그를 표시합니다.
import logging
# 오류 출력 스트림과 프로세스 실행 관련 정보를 사용합니다.
import sys
# 명령의 실행 시간을 perf_counter로 측정합니다.
import time
# 데코레이터가 원래 함수의 이름과 메타데이터를 보존하게 합니다.
from functools import wraps
# 데코레이터 입력 함수와 그 인자 타입을 정확히 표현합니다.
from typing import Callable, ParamSpec

# 서비스가 전달한 예상 오류의 원인과 힌트를 공통 처리에서 읽습니다.
from .models import AppError

# 원래 함수의 인자 타입을 감싼 함수에도 전달하는 타입 변수입니다.
P = ParamSpec("P")


# 명령 함수를 받아 종료 코드(int)를 반환하는 함수로 감싸는 데코레이터입니다.
def command_boundary(function: Callable[P, None]) -> Callable[P, int]:
    # 감싸진 함수의 이름·문서 등 메타데이터를 유지합니다.
    @wraps(function)
    # 정상/예상 오류/취소를 구분하고 성공 여부와 무관하게 실행 시간을 기록합니다.
    def wrapped(*args: P.args, **kwargs: P.kwargs) -> int:
        # 벽시계 변경의 영향이 적은 타이머로 소요 시간을 측정합니다.
        started = time.perf_counter()
        # 기본값을 실패로 두고 실제 명령이 끝난 뒤에만 성공으로 바꿉니다.
        status = 1
        try:
            # 입력 인자를 그대로 원래 execute 함수에 전달합니다.
            function(*args, **kwargs)
            # 정상적으로 끝난 명령의 종료 코드는 0입니다.
            status = 0
        # 모델/서비스의 예상 오류는 원인과 해결 힌트를 따로 안내합니다.
        except AppError as exc:
            print(f"[오류] {exc}", file=sys.stderr)
            print(f"[힌트] {exc.hint}", file=sys.stderr)
        # 없는 파일·권한·인코딩·CSV 파싱 오류도 스택트레이스 대신 안내합니다.
        except (OSError, UnicodeError, csv.Error) as exc:
            print(f"[오류] 파일 처리 실패: {exc}", file=sys.stderr)
            print("[힌트] 경로·권한·UTF-8 인코딩·CSV 형식을 확인하세요. 기존 저장 파일은 유지됩니다.",
                  file=sys.stderr)
        # 입력 종료와 Ctrl+C를 취소로 취급합니다.
        except (EOFError, KeyboardInterrupt):
            # 사용자 취소도 정상 성공과 구분되는 종료 코드입니다.
            status = 130
            print("[오류] 입력이 취소되었습니다.\n[힌트] 명령을 다시 실행해 입력을 완료하세요.",
                  file=sys.stderr)
        finally:
            # finally이므로 성공·예상 오류·취소 모두 로그를 남깁니다. INFO는 --verbose일 때 보입니다.
            logging.getLogger("budget_app").info("command=%s exit=%d elapsed=%.6fs",
                                                function.__name__, status, time.perf_counter() - started)
        # 상위 __main__.py가 이 int를 프로세스 종료 코드로 사용합니다.
        return status
    # 데코레이터 적용 결과로 원래 함수 대신 공통 처리가 포함된 함수를 돌려줍니다.
    return wrapped
