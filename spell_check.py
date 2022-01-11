def list1(a):
    with open("users.txt") as users:
        for line in users:
            for word in line.split(): 
                if word != a:
                    print(word)
                    break
            else:
                print("not present")
                
                    
with open("dictionary.txt") as dic:
    for k in dic:
        for l in k.split():
            list1(l)
 
"""string=input("Enter the word")
#def args(b):
with open("dictionary.txt") as dic:
    for k in dic:
        for word1 in k.split():
            if word1 == string:
                print("word present")
                break
        else:
            print("not present")"""
         
    
            
                
                
                
                        
                        
                        
                            
                   
                        
"""
with open("users.txt") as users:
    for line in users:
        for word in line.split():
            args(word)       """