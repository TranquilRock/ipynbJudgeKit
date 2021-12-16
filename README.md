# Judge kit for ipynb files
- code for NTU IMP_2021
- Usage
	1. Install python3 and Jupyter
	1. Clone or download files in this repository.
	1. Enter "python3 judge_all.py"
		- add " --convert" if you haven't convert ipynb to py file yet.
		- add " --directory path_to_ipynb_here" if ipynb files are in another directory.
		- add " --funcName function_name_here" to specify the function you would like to be judged.
- File explanation
	- solution.py
		- You should put your solution here, and provide a gen_data function that returns argument list for grading.
	- answer.py
		- You don't have to modify this, students' answer will be converted into answer.py by default.
	- judge_all.py
		- Core code for grading.
		- There are three command line arguments available.
			- " --out result_file_name_here" 
			- " --convert" this will use Jupyter to convert ipynb to py file.
			- " --directory path_to_ipynb_here" tell python where do ipynb files reside.
		    - " --funcName function_name_here" specify the function you would like to be judged.
	- format_filename.sh
		- This shell script will rename all ipynb in the same directory with first 9 characters of the file.
	
	- grade_one.py
		- This file contains function that grade a single file.
	
	- util/
		- extract_function.py
			- This will extract function from target python file, avoiding dirty code issue that leads to import failure.
		- grading_criteria.py
			- Define your own way to verify students' answer.
		- exception_class.py
			- You can add any additional exception type here, for grade one to know what's the problem.

