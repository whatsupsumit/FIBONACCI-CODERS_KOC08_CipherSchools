N = int(input("Enter the number you want to check: "))

# variables for generating fibonacci sequence
f3 = 0
f1 = 1
f2 = 1
# 0 and 1 both are fibonacci numbers
if (N == 0 or N == 1):
    print("Given number is fibonacci number")

else:
    # generating the fibonacci numbers until the generated number is less than  N
    while f3 < N:
        f3 = f1 + f2
        f2 = f1
        f1 = f3
    if f3 == N:
        print("Given number is a valid fibonacci number")
    else:
        print("No its not a valid fibonacci number")
