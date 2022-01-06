"""
no_names=int(input("Enter the number of names "))
names=[]
for i in range(no_names):
    name=input("Enter the name : ")
    names.append(name)
print("Original names are ",names)
temp=names[0]
i=0
while(i<len(names)):
   j=i+1
   while(j<len(names)):
      if names[i]>names[j]:
         temp=names[i]
         names[i]=names[j]
         names[j]=temp
      j=j+1
   i=i+1
print("The ascending order is ",names)
"""
no_names=int(input("Enter the number of names "))
names=[]
for i in range(no_names):
    name=input("Enter the name : ")
    names.append(name)
print("Original names are ",names)
temp=names[0]
i=0
while(i<len(names)):
   j=i+1
   while(j<len(names)):
      c=names.split()
      print(c)
      if ord(names[i])> ord(names[j]):
         temp=names[i]
         names[i]=names[j]
         names[j]=temp
      j=j+1
   i=i+1
print("The ascending order is ",names)