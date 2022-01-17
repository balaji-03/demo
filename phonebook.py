def phone(x):
    match x:
        case '1':
            with open("D:\\Balaji\\Git\\Demo\\phone.txt","a+") as phone:
                Name=input("Name : ")
                Mobile_no=input("Mobile_no ")
                Age = input(" Age : ")
                email=input(" email : ")
                phone.write('\n'+'\n'+'Name : '+Name)
                phone.write('\n'+'Mobile_no : '+Mobile_no)
                phone.write('\n'+'Age : '+Age)
                phone.write('\n'+'email :'+email)
        case '2':
                modify=input("enter the word to be modified ")
                new=input("enter the correct word ")
                with open(r"D:\\Balaji\\Git\\Demo\\phone.txt","r") as phone:
                    ch=phone.read()  
                    ch=ch.replace(modify,new)
                with open(r"D:\\Balaji\\Git\\Demo\\phone.txt","w") as phone:
                    phone.write(ch)               
                    
        case '3':
                pass
        case  '4':
            print("better luck ")
        case _ :
            print("Enter the right choice")
a=input("enter choice ")  
phone(a)
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