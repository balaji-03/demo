def list1(a):
    b=0
    with open("D:\\Balaji\\Git\\Demo\\dictionary.txt") as dic:
        for line in dic:
            for word in line.split():
                if word == a:
                    b=2
                    break
        print(a)
        if b == 0:
            choice=input("add or modify")
            if choice == "add":
                with open("D:\\Balaji\\Git\\Demo\\dictionary.txt","a+") as dic:
                    dic.write(a+" ")
                   
            if choice == "modify":
                modify=input("enter the word to be modified ")
                new=input("enter the correct word ")
                with open(r"D:\\Balaji\\Git\\Demo\\users.txt","r") as users:
                    content=users.read() 
                    content=content.replace(modify,new)
                with open(r"D:\\Balaji\\Git\\Demo\\users.txt","w") as users:
                    users.write(content)
with open("users.txt") as users:
    for k in users:
        for l in k.split():
            list1(l)
            
            
       
"""           
string=input("Enter the word")
#def args(b):

isPresent = 0 
with open("dictionary.txt") as dic:
    for k in dic:
        for word1 in k.split():
            if word1 == string:
                print("word present")
                isPresent = 1
                break
    if isPresent == 0 :
        print("word NOT present")
     """   
    
                   
