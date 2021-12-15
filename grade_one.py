import solution # Where TA's solution resides in.
import importlib
import signal
from utils import TimeOutException

def handler(signum, frame):
    raise TimeOutException("Timeout!", 0)
def grade_one(criteria , modulename,n=10):
    # Students' code may contain error, leads to termination upon import
    try:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(10)
        answer = importlib.import_module(modulename)
        pass_count = 0
        for _ in range(n):
            data = solution.gen_data()
            if data is None:
                break # avoid data out of range
            if criteria(solution.Q1_CountNumbers, data) == criteria(answer.Q1_CountNumbers, data):
                pass_count+=1
        if pass_count == n:
            return "Pass"
        else:
            return f"Score:{(pass_count * 100 / n):.2f}\n"
    except TimeOutException:
        return "Timeout"
    except Exception as e:
        print(e)
        return "Error"
