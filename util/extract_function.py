def extract_function(directory="./", source="a.py", out="out.py"):
    with open(directory + out, "w") as f:  # clear out file
        # Notice this code can't handle breakline '\' yet
        with open(directory + source, "r") as myfile:
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
