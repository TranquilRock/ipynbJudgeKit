from contextlib import redirect_stdout
import io

def grade_by_output(func=None, argv=None):
    with io.StringIO() as buf, redirect_stdout(buf):
        func(*argv)
        output = buf.getvalue()
    return output

def grade_by_return(func=None, *argv):
    ret = None
    with io.StringIO() as buf, redirect_stdout(buf):  # Avoid garbage message
        ret = func(*argv)
        buf.getvalue()
    return ret
