n= int(input("Enter the total no to print:"))


n1, n2= 0, 1
count=0
if (n<=0):
    print("Please enter a positive no. ")
elif (n==1): 
    print("Fibonacci sequence upto ", n)
    print(n1)
else:
    print("Fibonacci Sequence ")

    while(count<n):
        print(n1) 
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1 