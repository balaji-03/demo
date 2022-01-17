a=open("D:\\Balaji\\Git\\Demo\\file2.txt","r")
def no_lines():
    c=0
    for line in a:
        c=c+1
    return c
d=no_lines()
s= input("Enter function name: ").split('\b')
string=""
for element in s:
    string += element 
f=s[0][5:7]
g=s[0][7:-1]
def lastline(k,r):
    b=open("D:\\Balaji\\Git\\Demo\\"+r+'.'+'txt')   
    user=int(k)
    for i,line1 in enumerate(b):
        if i>=d-(user):
            print(line1)
if  string =='tail('+f+','+g+')':
    lastline(f,g)
