# Python Matrix Programs
    
# 1) Python Matrix Programs

m1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    
m2=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    
# 2) Python Program to Add Two Matrices

def addMatrix(m1,m2):
    row=len(m1)
    col=len(m1[0])
    result=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
    for i in range(row):
        for j in range(col):
            result[i][j]=m1[i][j]+m2[i][j]
    print(result)
    
addMatrix(m1,m2)

# 3) Python Program to Multiply Two Matrices

def mulMatrix(m1,m2):
    row=len(m1)
    col=len(m1[0])
    result=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
    for i in range(row):
        for j in range(col):
            result[i][j]=m1[i][j]*m2[i][j]
    print(result)
    
mulMatrix(m1,m2)


# 4) Python Program to subtract the two matrices

def subMatrix(m1,m2):
    row=len(m1)
    col=len(m1[0])
    result=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
    for i in range(row):
        for j in range(col):
            result[i][j]=m1[i][j]-m2[i][j]
    print(result)
    
subMatrix(m1,m2)

# 5) Python Program to determine whether two matrices are equal

if m1==m2:
    print("Both matrices are equal.")
else:
    print("Both matrices are not equal.")
    
# 6) Python Program to display the lower triangular matrix

def lowerTriangularMatrix(m1):
    row=len(m1)
    col=len(m1[0])
    for i in range(row):
        for j in range(col):
            if j>i:
                print(0,end=" ")
            else:
                print(m1[i][j],end=' ')
        print()

print()   
lowerTriangularMatrix(m1)


# 7) Python Program to display the upper triangular matrix

def upperTriangularMatrix(m1):
    row=len(m1)
    col=len(m1[0])
    for i in range(row):
        for j in range(col):
            if j<i:
                print(0,end=" ")
            else:
                print(m1[i][j],end=' ')
        print()

print()    
upperTriangularMatrix(m1)

# 8) Python Program to find the frequency of odd & even numbers in the given matrix

def frequencyOfEvenAndOdd(m1):
    row=len(m1)
    col=len(m1[0])
    even=0
    odd=0
    for i in range(row):
        for j in range(col):
            if m1[i][j]%2==0:
                even+=1
            else:
                odd+=1
    print("Frequency of even elements are :- ",even)
    print('Frequency of odd elements are :- ',odd)

print()    
frequencyOfEvenAndOdd(m1)


# 9) Python Program to find the product of two matrices


# 10) Python Program to find the sum of each row and each column of a matrix

def rowSum(m):
    row=len(m)
    col=len(m[0])
    for i in range(row):
        rowsum=0
        for j in range(col):
            rowsum+=m[i][j]
        print(i," row sum is :- ",rowsum)
        
def colSum(m):
    row=len(m)
    col=len(m[0])
    for i in range(row):
        colsum=0
        for j in range(col):
            colsum+=m[j][i]
        print(i," col sum is :- ",colsum)

print(m1)       
rowSum(m1)
colSum(m1)
        
        
# 11) Python Program to find the transpose of a given matrix

def transposeMatrix(m):
    row=len(m)
    col=len(m[0])
    result=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
    for i in range(row):
        for j in range(col):
            result[i][j]=m[j][i]
    
    return result

print("Before Transpose Operation :- ")
print(m1)
m1=transposeMatrix(m1)
print("After Transpose Operation :- ")
print(m1)
    
    
# 12) Python Program to determine whether a given matrix is an identity matrix

def checkIdentityMatrix(m):
    row=len(m)
    col=len(m[0])
    for i in range(row):
        for j in range(col):
            if i==j:
                if m[i][j]!=1:
                    return False
            else:
                if m[i][j]!=0:
                    return False
    return True

r=checkIdentityMatrix(m1)
if r:
    print("It is an Identity Matrix.")
else:
    print("It is not an Identity Matrix.")
                    
    
    
  
# 13) Python Program to determine whether a given matrix is a sparse matrix
# 14) Python Program to Transpose matrix
