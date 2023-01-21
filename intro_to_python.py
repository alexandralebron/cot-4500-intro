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