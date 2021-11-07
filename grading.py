try:
    from contextlib import redirect_stdout
    import io
    import argparse
    import solution

    parser = argparse.ArgumentParser(description='Grading')
    parser.add_argument('--n', default=10, type=int, help='How many test cases')
    parser.add_argument('--name', default="None", type=str, help='Tested student name')
    parser.add_argument('--passonly', action='store_true', help='Tested student name')
    parser.add_argument('--output', default="output.txt",
                        type=str, help='Output filename')

    args = parser.parse_args()
    import answer

    def get_print(func=None, argv=None):
        with io.StringIO() as buf, redirect_stdout(buf):
            func(*argv)
            output = buf.getvalue()
        return output

    pass_count = 0

    for i in range(args.n):
        data = solution.gen_data()
        if get_print(solution.Q1_Draw_an_arrow, data) == get_print(answer.Q1_Draw_an_arrow, data):
            pass_count+=1
            
    with open(args.output, 'a') as f:
        if args.passonly:
            if pass_count == args.n:
                f.write(f"{args.name} pass\n")
        else:
            if pass_count != args.n:
                f.write(f"{args.name} => Score:{(pass_count * 100 / args.n):.2f}\n")
except:
    with open(args.output, 'a') as f:
        if not args.passonly:
            f.write(f"{args.name} Error\n")