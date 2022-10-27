import importlib
import signal
from typing import Callable
from util.exception_class import TimeOutException

solution = importlib.import_module("solution")


def handler(*_) -> None:
    raise TimeOutException("Timeout!", 0)


def grade_one(
    criteria: Callable,
    func_name: str,
    n_testcase: int = 10,
    time_limit: int = 10,
    module="",
) -> str:
    # Students' code may contain error, leads to termination upon import
    signal.signal(signal.SIGALRM, handler)
    try:
        signal.alarm(time_limit)
        answer = importlib.import_module(module)
        pass_count = 0
        print_first_failed_flag = True
        solution.data_reset()
        failed_data = None
        for _ in range(n_testcase):
            data = solution.gen_data()
            if data is None:
                break  # avoid data out of range
            if criteria(getattr(solution, func_name), *data) == criteria(
                getattr(answer, func_name), *data
            ):
                pass_count += 1
            elif print_first_failed_flag:
                print(data)
                failed_data = data
                print_first_failed_flag = False
        signal.alarm(0)  # Cancel the alarm to avoid race condition.
        if pass_count == n_testcase:
            return "Pass"
        else:
            return (
                f"Score:{(pass_count * 100 / n_testcase):.2f} failed on: "
                + " ".join([str(i) for i in failed_data])
            )
    except Exception as e:
        return e
