def list1(a):
    b=0
    with open("dictionary.txt") as dic:
        for line in dic:
            for word in line.split():
                if word == a:
                    b=2
                    break
        if b == 0:
            dic.write(a)
            dic.write(score)
            dic.write
            dic.close()    
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
    
                   
                        
"""
with open("users.txt") as users:
    for line in users:
        for word in line.split():
            args(word)       """
