num=[]
number=int(input("Enter the number of elements in  a list "))
for i in range(1,number+1):
    value=int(input("Enter the %d element in array "%i))
    num.append(value)
temp=num[0]
for j in range(1,number):
  if num[j]>temp: 
       temp=num[j]
print("the largest number in array is ",temp)

