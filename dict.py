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
"""
for j in range(len(names)):
    for i in range(len(names)-1):#len(names)-1 is the condition for iteration variable i+1
        if names[i][0] == names [i+1][0]:
            if (names[i][1]>names[i+1][1]):
                pass
                '''
                temp=names[i]
                names[i]=names[i+1]
                names[i+1]=temp
                '''
        else:
        
             if names[i][0]>names[i+1][0]:
                temp=names[i]
                names[i]=names[i+1]
                names[i+1]=temp
       
"""
for i in range(len(names)):
    for j in range(len(names)):
        if (names[i][0] == names[j][0]):
            if (names[i][1]<names[j][1]):
                temp=names[i]
                names[i]=names[j]
                names[j]=temp
        if (names[i][0] == names[j][0]) and (names[i][1] == names[j][1]):
            if (names[i][2]<names[j][2]):
                temp=names[i]
                names[i]=names[j]
                names[j]=temp
        if (names[i][0]<names[j][0]):
            temp=names[i]
            names[i]=names[j]
            names[j]=temp
print("ascending order is",names)
