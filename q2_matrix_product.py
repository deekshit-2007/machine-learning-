r1=int(input("Enter rows of A:"))
c1=int(input("Enter columns of A:"))
a=[]
print("Enter matrix A")
for i in range(r1):
    row=list(map(int,input().split()))
    a.append(row)
r2=int(input("Enter rows of B:"))
c2=int(input("Enter columns of B:"))
b=[]
print("Enter matrix B")
for i in range(r2):
    row=list(map(int,input().split()))
    b.append(row)
if c1!=r2:
    print("Matrix multiplication not possible")
else:
    result=[]
    for i in range(r1):
        row=[]
        for j in range(c2):
            s=0
            for k in range(c1):
                s=s+a[i][k]*b[k][j]
            row.append(s)
        result.append(row)
    print("Result is")
    for i in result:
        print(i)