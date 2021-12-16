import importlib
import signal
from util.exception_class import TimeOutException
solution = importlib.import_module('solution')

def handler(signum, frame):
    raise TimeOutException("Timeout!", 0)
def grade_one(criteria , funcName:str, n=10, timelimit = 10,module=''):
    # Students' code may contain error, leads to termination upon import
    try:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timelimit)
        answer = importlib.import_module(module)
        pass_count = 0
        flag = True
        solution.data_reset()
        failed_data = None
        for _ in range(n):
            data = solution.gen_data()
            if data is None:
                break # avoid data out of range
            if criteria(getattr(solution, funcName), *data) == criteria(getattr(answer, funcName), *data):
                pass_count+=1
            elif flag:
                print(data)
                failed_data = data
                flag = False
        if pass_count == n:
            return "Pass"
        else:
            return f"Score:{(pass_count * 100 / n):.2f} failed on: " + ' '.join([str(i) for i in failed_data])
    except Exception as e:
        return e
