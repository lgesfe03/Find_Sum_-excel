# Find_Sum_-excel
Author : Mark Lin YL

Date: 2023/04

Executable File Download:  [Link](https://reurl.cc/8qL5ao) (Recommand to compile yourself for lastest version )
# Introduction
This repository is used to search certain sum number from excel file.

[User Manual](Readme/Readme.pdf)

# Package method
Due to "pyinstaller" might pack too large size executable file, we create a virtual environment for packaging it.
Follow steps below:

1.Set python virtual environment:
  ```
  python -m pipenv --python 3.9
  ```
2.Start python virtual environment:
  ```
  python -m pipenv shell
  ```
3.Install modules python need:
	
	pip install pyinstaller
	pip install pandas openpyxl
	
  ...(else more if need)
  
4.Package Command: (set .exe file icon through first argv :XX.ico,  second argv to point out where main .py file is)
	
	
	pyinstaller -F -w -i D:\Tutorial\Python\find_sum_excel\icon\auto.ico D:\Tutorial\Python\find_sum_excel\find_sum_v2_OOP.py
	
	
# Output Path
Output executable file path:
* C:\Users\Mark\dist

# Executable file Version Log
## v1:
	First version:
	1.Choose excel file and read\r\n
	2.Check whether target sum can be compose in array number.

## v2:
	1.UI (User Interface) implement with v1 functions
## v3:
	1.Added a progress bar to prevent misunderstandings that the program has crashed.
	2.Added options for "Equal" and "Closest", but the "Closest" option is not yet fully implemented and may cause the program to freeze. For now, please use the "Equal" option. ("Equal" is the original version that looks for exact matches, and "Closest" is for finding the closest match.)

## v4:
	1.It is now possible to search for the closest set of numbers using the implementation of option 4.Cloest. This search method is now set as the default, and if there is an exact match, it will display "Yes" and "No" if there is no exact match.
	2.Added progress bar text to prevent misunderstandings that the program has crashed.
	3.Fixed an issue where the window may not respond after clicking "Readcolumn".
