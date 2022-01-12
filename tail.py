a=open("D:\\Balaji\\Git\\Demo\\file2.txt","r")
def no_lines():
    c=1
    for line in a:
        c=c+1
    return c
d=no_lines()
e=input("enter the lines")
f=input("enter file name")
s=input("enter the function name :")
def lastline(a,b):
    b=open("D:\\Balaji\\Git\\Demo\\"+b+'.'+'txt')   
    user=int(a)
    for i,line1 in enumerate(b):
        if i>=d-(user+1):
            print(line1)    
if s == 'tail('+e+','+f+')':                
    lastline(e,f)
