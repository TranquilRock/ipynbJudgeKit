import os
from contextlib import redirect_stdout
import io
def get_print(func=None, argv=None):
            with io.StringIO() as buf, redirect_stdout(buf):
                func(*argv)
                output = buf.getvalue()
            return output

def get_ret(func=None, *argv):
    ret= None
    with io.StringIO() as buf, redirect_stdout(buf): #Avoid garbage message
        ret = func(*argv)
        buf.getvalue()
    return ret


class TimeOutException(Exception):
    def __init__(self, message, errors):
        super(TimeOutException, self).__init__(message)
        self.errors = errors

def extract_function(directory="./", source = "a.py", out="out.py"):
    with open(directory + out, "w") as f:  # clear out file
        # Notice this code can't handle breakline '\' yet
        with open(directory + source, "r") as myfile:
            f.writelines(['m = 2722458769\n'])
            function = []
            writing = False
            for line in myfile:
                # Skip comments and magic command
                if line.startswith('#') or line.startswith('%') or (len(line.strip()) == 0):
                    continue
                # Not empty line and no indent, means the function have ended.
                if writing:
                    if line[0] != ' ':
                        f.writelines(function)
                        function = []
                        # Then the line will be check by the following if.
                        writing = False
                    else:
                        function.append(line)
                # If line is not inside a function, check if it's a function
                if not writing:
                    if line.startswith("def"):
                        writing = True
                        function.append(line)
                    elif line.startswith("import"):  # write directly
                        f.writelines([line])
            f.writelines(function)
