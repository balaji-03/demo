num=[]
number=int(input("Enter the elements in the list"))
for i in range(number):
    value=int(input("Enter the %d element in the array"%i))
    num.append(value)
temp=num[0]
for j in range(1,number):
    if num[j]<temp:
        small=num[j]
        temp=num[j]
    else:
        small=temp
print(small)


