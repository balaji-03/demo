f=open("D:\\Balaji\\Git\\Demo\\acufore.txt","r")
old=input("Enter the word to be replaced ")
new=input("Enter the replacement word ")
arr=[]
for i in f:
    c=i.split()
    for j in c:
        d=j.replace(old,new)
        arr.append(d)
print(arr)        
        