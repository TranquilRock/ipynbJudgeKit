import argparse
import os
from grade_one import grade_one
from util.grading_criteria import *
from util.extract_function import *

parser = argparse.ArgumentParser(description="Extract function from ipynb")
parser.add_argument("--out", default="result", type=str, help="Target file's name.")
parser.add_argument(
    "--convert", action="store_true", help="Convert ipynb to py by jupyter."
)
parser.add_argument(
    "--directory", default="./", type=str, help="File directory of *.ipynbs."
)
parser.add_argument(
    "--funcName", default="./", type=str, help="Function you want to grade."
)
args = parser.parse_args()


def main(args: argparse.Namespace):
    file_names = os.popen(f"ls {args.directory} | grep ipynb").read().split()
    if args.convert:
        for file_name in file_names:
            os.system(
                f"jupyter nbconvert --to python {args.directory}{file_name} --output {args.directory}{file_name[:9]}.py"
            )
    criteria = grade_by_return
    with open(args.out + "_pass.txt", "w") as correct:  # Clear file
        with open(args.out + "_err.txt", "w") as error:
            for file_name in file_names:
                print(f"grading {file_name}")
                extract_function(
                    source=f"{args.directory}{file_name[:9]}.py",
                    out=f"{file_name[:9]}_answer.py",
                )
                ret = grade_one(
                    criteria=criteria,
                    func_name=args.funcName,
                    n_testcase=10,
                    module=f"{file_name[:9]}_answer",
                    time_limit=10,
                )
                os.system(f"rm {file_name[:9]}_answer.py")
                if ret != "Pass":
                    error.writelines([f"{file_name[:9]} => {ret}\n"])
                else:
                    correct.writelines([f"{file_name[:9]} => {ret}\n"])

if __name__ == "__main__":
    main(args)
