str=input("Enter string :- ")
a=len(str)
char=[]
arr=[]
freq=[]
for i in range(a):
    arr.append(str[i])
    if(str[i] not in char):
        char.append(str[i])
    else:
        continue
print(arr)
print(char)
a=len(arr)
count=0

for j in range (len(char)):
    for i in range(a):
        if(char[j]==arr[i]):
            count+=1

    freq.append(count)
    count=0

print(freq)