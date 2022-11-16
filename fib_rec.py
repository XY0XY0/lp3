def fibonacci(n):
    if(n<=1):
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n= int(input("Enter number of terms to print: "))
print("Fibonacci Sequence |")
for i in range(n):
    print(fibonacci(i))