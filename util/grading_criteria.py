from contextlib import redirect_stdout
import io
from typing import Any, Callable, List


def grade_by_output(func: Callable, *argv: List[Any]) -> str:
    with io.StringIO() as buf, redirect_stdout(buf):
        func(*argv)
        output = buf.getvalue()
    return output

def grade_by_return(func: Callable, *argv: List[Any]) -> Any:
    ret = None
    with io.StringIO() as _buf, redirect_stdout(_buf):  # Avoid garbage message
        ret = func(*argv)
        _buf.getvalue()
    return ret
