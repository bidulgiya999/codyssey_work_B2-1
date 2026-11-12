"""명령 처리의 예외 경계와 실행 시간 로그를 분리한다."""
from __future__ import annotations

import csv
import logging
import sys
import time
from functools import wraps
from typing import Callable, ParamSpec

from .models import AppError

P = ParamSpec("P")


def command_boundary(function: Callable[P, None]) -> Callable[P, int]:
    @wraps(function)
    def wrapped(*args: P.args, **kwargs: P.kwargs) -> int:
        started = time.perf_counter()
        status = 1
        try:
            function(*args, **kwargs)
            status = 0
        except AppError as exc:
            print(f"[오류] {exc}", file=sys.stderr)
            print(f"[힌트] {exc.hint}", file=sys.stderr)
        except (OSError, UnicodeError, csv.Error) as exc:
            print(f"[오류] 파일 처리 실패: {exc}", file=sys.stderr)
            print("[힌트] 경로·권한·UTF-8 인코딩·CSV 형식을 확인하세요. 기존 저장 파일은 유지됩니다.",
                  file=sys.stderr)
        except (EOFError, KeyboardInterrupt):
            status = 130
            print("[오류] 입력이 취소되었습니다.\n[힌트] 명령을 다시 실행해 입력을 완료하세요.",
                  file=sys.stderr)
        finally:
            logging.getLogger("budget_app").info("command=%s exit=%d elapsed=%.6fs",
                                                function.__name__, status, time.perf_counter() - started)
        return status
    return wrapped
