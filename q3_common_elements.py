a=list(map(int,input("Enter first list:").split()))
b=list(map(int,input("Enter second list:").split()))
common=[]
for i in a:
    if i in b:
        if i not in common:
            common.append(i)
print("Common elements are",common)
print("Number of common elements are",len(common))
