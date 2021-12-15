import argparse
import os
import sys
from grade_one import grade_one
from utils import *
parser = argparse.ArgumentParser(description='Extract function from ipynb')
parser.add_argument('--out', default="result", type=str,
                    help='Targe file\'s name')
parser.add_argument('--convert', action="store_true", help='Targe file\'s name')
parser.add_argument('--directory', default="./", type=str,
                    help='Targe file\'s name')
args = parser.parse_args()
filenames = os.popen(f'ls {args.directory} | grep "ipynb"').read().split()
if args.convert:
    for filename in filenames:
        os.system(
            f'jupyter nbconvert --to python {args.directory}{filename} --output {args.directory}{filename[:9]}.py')
criteria = get_print
with open(args.out + "_pass.txt", "w") as correct:  # Clear file
    with open(args.out+"_err.txt", "w") as error:
        for filename in filenames:
            print(f'grading {filename}')
            print(f'grading {filename}', file=sys.stderr)
            extract_function(
                source=f"{args.directory}{filename[:9]}.py", out=f"{filename[:9]}_answer.py")
            ret = grade_one(criteria=criteria,
                            modulename=f"{filename[:9]}_answer", n=10)
            os.system(f"rm {filename[:9]}_answer.py")
            if ret != "Pass":
                error.writelines([f"{filename[:9]} => {ret}\n"])
            else:
                correct.writelines([f"{filename[:9]} => {ret}\n"])
