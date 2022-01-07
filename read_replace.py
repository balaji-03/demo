"""
import re
f=open("D:\\Balaji\\Git\\Demo\\acufore.txt","r")
old=input("Enter the word to be replaced ")
new=input("Enter the replacement word ")
arr=[]
for i in f:
   
    c=i.split()
    for j in c:
        if(re.fullmatch(old,j)):
            e=str(j.replace(old,new))
h=c.index(old)
c[h]=new       
print(c)
"""
f=open("D:\\Balaji\\Git\\Demo\\acufore.txt","r")
old=input("Enter the word to be replaced ")
new=input("Enter the replacement word ")
arr=[]
for i in f:
    c=i.split()
    for j in c:
        if old == j:
            e=str(j.replace(old,new))
h=c.index(old)
c[h]=new       
print(c)