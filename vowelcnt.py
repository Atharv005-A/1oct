str=input("enter any sentence:")
strl=str.lower()
vow=['a','e','i','o','u']
cnt=0
acnt=0
ecnt=0
icnt=0
ocnt=0
ucnt=0
for i in str:
    for j in vow:
        if i==j:
            cnt=cnt+1
        if i=='a':
            acnt=acnt+1
        if i=='e':
            ecnt=ecnt+1
        if i=='i':
            icnt=icnt+1
        if i=='o':
            ocnt=ocnt+1
        if i=='u':
            ucnt=ucnt+1


print("total vowels:",cnt)
print("a total vowels:",acnt)
print("e total vowels:",ecnt)
print("i total vowels:",icnt)
print("o total vowels:",ocnt)
print("u total vowels:",ucnt)
    