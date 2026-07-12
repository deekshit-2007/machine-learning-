r=int(input("Enter number of rows:"))
c=int(input("Enter number of columns:"))
a=[]
print("Enter the matrix")
for i in range(r):
    row=list(map(int,input().split()))
    a.append(row)
t=[]
for i in range(c):
    row=[]
    for j in range(r):
        row.append(a[j][i])
    t.append(row)
print("Transpose is")
for i in t:
    print(i)