ist=[12,34,56,3,53,66]
print("orignal list:",ist)

rlis=[]
for i in  ist[::-1]:
    rlis.append(i)

print("reversed list:",rlis)