num=[]
number=int(input("Enter the number of elements in  a list "))
for i in range(1,number+1):
    value=int(input("Enter the %d element in array "%i))
    num.append(value)
temp=num[0]
i=0
while(i<len(num)):
	j=i+1
	while(j<len(num)):
		if num[i]<num[j]:
			temp=num[i]
			num[i]=num[j]
			num[j]=temp
		j=j+1
	i=i+1
print("The descending order is ",num)