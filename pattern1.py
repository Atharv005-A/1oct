# n=int(input("enter number for pattern:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# n = int(input("Enter number for pattern: "))

# for i in range(1, n + 1):
#     #  spaces
#     for j in range(n - i):
#         print(" ", end=" ")

#     # stars
#     for j in range(2 * i - 1):
#         print("*", end=" ")

#     print()



n = int(input("Enter number for pattern: "))

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end=" ")

    if i % 2 == 1:
        symbol = "*"
    else:
        symbol = "#"

    for j in range(2 * i - 1):
        print(symbol, end=" ")

    print()


