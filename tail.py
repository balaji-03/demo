a=open("D:\\Balaji\\Git\\Demo\\file2.txt","r")
def no_lines():
    c=0
    for line in a:
        c=c+1
    return c
d=no_lines()
e,l,z,k,m= [str(e) for e in input("Enter function name: ").split()]
s=e+l+z+k+m
def lastline(f,c):
    b=open("D:\\Balaji\\Git\\Demo\\"+c+'.'+'txt')   
    user=int(f)
    for i,line1 in enumerate(b):
        if i>=d-(user):
            print(line1)
if s == 'tail('+l+z+k+')':   
    lastline(l,k)
