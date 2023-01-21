# cot-4500-intro
This file consists of 3 python code problems on how to make a 3x3 matrix; using i for the row and j for the column.

## Instructions on How to Compile intro_to_python.py
- Ensure we have a Python IDE (for this project, I compiled the code on Spyder).
- Copy or type the code into a Python IDE.
- Click Run.
- You will see the answers to all three questions on top of each other.

## Explanation of NumPy
NumPy is a package for scientific computing in Python. It allows us to have access to a library that provides basic mathematical functions and allows us to create complexe array objects.

## requirements.txt
```
anyio==3.6.2
click==8.1.3
h11==0.14.0
idna==3.4
numpy==1.24.1
pandas==1.5.3
pydantic==1.10.4
python-dateutil==2.8.2 
pytz==2022.7.1
six==1.16.0
sniffio==1.3.0 
starlette==0.22.0
typing_extensions==4.4.0 
uvicorn==0.20.0 
```

## Code 
```python
import numpy as np

A = np.array([[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]])		
	
#update matrix where i= j for question 1
for i in range(3):
	for j in range(3):
		if (i == j):
			A[i][j] = 1;
			
#print the matrix
for i in range(3):
	for j in range(3):
		print(A[i][j], end = " ")
	print("")
			
#update the matrix where i != j for question 2
for i in range(3):
	for j in range(3):
		if (i != j):
			A[i][j] = A[i][j] + 3;
			
#print the matrix
for i in range(3):
	for j in range(3):
		print(A[i][j], end = " ")		
	print("")

			
#print only 2 columns of matrix for question 3
for i in range(3):
	for j in range(2):
		print(A[i][j], end = " ")		
	print("")
```
