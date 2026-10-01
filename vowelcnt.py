str=input("enter any sentence:")
strl=str.lower()
vow=['a','e','i','o','u']
cnt=0

for i in str:
    for j in vow:
        if i==j:
            cnt=cnt+1

print("total vowels:",cnt)
    