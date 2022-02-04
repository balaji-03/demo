def phone(x):
    match x:
        case '1':
            with open("D:\\Balaji\\Git\\Demo\\phone.txt","a+") as phone:
                Name=input("Name : ")
                Mobile_no=input("Mobile_no : ")
                Dep = input("Department : ")
                email=input(" email : ")
                phone.write('\n'+Name+','+Mobile_no+','+Dep+','+email)
                
        case '2':
        
                modify=input("enter the old word ")+','
                new=input("enter the new word ")+','
                with open(r"D:\\Balaji\\Git\\Demo\\phone.txt","r") as phone:
                    data=phone.read()
                    if modify in data:
                        data=data.replace(modify,new)
                    else:
                        print("Enter the word in file to be replaced ")
                with open(r"D:\\Balaji\\Git\\Demo\\phone.txt","w") as phone:
                    phone.write(data)       
                phone.close()
     
        case '3':
            enter_word = input("Enter the name of person whose details can be fetched : ")
            phone=open(r"D:\\Balaji\\Git\\Demo\\phone.txt","r")
            ispre=0
            for i in phone:
                c = i.split(',')
               
                if c[0] == enter_word:
                        print(c[0]+','+c[1]+','+c[2]+','+c[3])
                        ispre = 1
                        break
            if ispre == 0:
                print("Enter the word in file that detail to be displayed ")             
            phone.close()
        case '4':
                b=open("D:\\Balaji\\Git\\Demo\\phone.txt","r")
                c=b.readlines()
                b.close()
                d=input("Enter name of person whose details  to be deleted ")
                def ft():
                    ispre=0
                    for e in c:
                        f=e.split(',')
                        if f[0] == d:
                            ispre=1
                            return f
                        
                    if ispre == 0:
                        print("Enter the name of person in file to be printed ")
                h=open("D:\\Balaji\\Git\\Demo\\phone.txt","w+")
                o=ft()
                
                for e in c:
                        f=e.split(',')
                        if f != o:
                            k=f[0]+','+f[1]+','+f[2]+','+f[3]
                            h.write(str(k))
                h.close()
        case _ :
                print("Enter the right choice")
  
a=input("Enter the choice \n 1.Add \n 2.Find & replace \n 3.Extract the details \n 4.Delete details  \n Enter the choice  ")
phone(a)
"""   ca=phone.read()
                    for i in ca:
                        for j in i.split(','):
                            if j  == modify:
                                h=i.replace(j,new)
                                print(h)
                with open(r"D:\\Balaji\\Git\\Demo\\phone.txt","w+") as phone:
                    ca=phone.readlines()
                    for i in ca:
                        for j in i.split(','):
                            if j  == modify:
                                h=str(i.replace(j,new))
                                phone.write(h)
                        print(h)"""

"""
print(lines)
result=[]
for x in lines:
result.append(x.split(' ')[1])
f.close()"""
         
""" if ca == modify:
    ch=phone.read()  
    ch=ch.replace(modify,new)
    with open(r"D:\\Balaji\\Git\\Demo\\phone.txt","w") as phone:
phone.write(ch)"""         

"""
import fileinput

print ("Text to search for:")
textToSearch = input( "> " )

print ("Text to replace it with:")
textToReplace = input( "> " )

print ("File to perform Search-Replace on:")
fileToSearch  = input( "> " )
#fileToSearch = 'D:\dummy1.txt'

tempFile = open( fileToSearch, 'r+' )

for line in fileinput.input( fileToSearch ):
    if textToSearch in line :
        print('Match Found')
    else:
        print('Match Not Found!!')
    tempFile.write( line.replace( textToSearch, textToReplace ) )
tempFile.close()


input( '\n\n Press Enter to exit...' )
print("""
                           
"""if j == enter_word:
    print('a')
    #details={j:{'Name' : j,'Mobile_no': j[Mobile_no],'Dep' : j[Dep],'email' :j[email]}}
if j == 'balajee':
    details={j:{'Name' : j[Name],'Mobile_no': j[Mobile_no],'Dep' : j[Dep],'email' :j[email]}}
    
if j == 'baby':
    details={j:{'Name' : j,'Mobile_no': '7906879866','Dep' : 'coding','email' : 'baby@gmail.com'}}
if j == 'philo':
    details={j:{'Name' : j,'Mobile_no': '8903366993','Dep' : 'hardware','email ': 'philo@gmail.com'}}
print('\nName : '+details[j]['Name']+'\nMobile_no : '+details[j]['Mobile_no']+'\nDepartment : '+details[j]['Dep']+'\n email :'+details[j]['email'])
print(details)
pre = 1
    break
if ispre == 0:
    print("Unknown person ")  
phone.close()"""