
A=[]
m=int(input("enter number of rows :"))
n=int(input("enter the number of columns :"))
for i in range(m):
    row=[]
    for j in range(n):
        k=int(input())
        row.append(k)
    A.append(row) 
print(A)
B=[]
m=int(input("enter number of rows :"))
n=int(input("enter the number of columns :"))
for i in range(m):
    row=[]
    for j in range(n):
        k=int(input())
        row.append(k)
    B.append(row)  #[[1 2 3]]
print(B)
c=[[0,0],[0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):  
            c[i][j]=c[i][j]+A[i][j]*B[k][j]
print("resultant matrix is: ",c[i][j]);

