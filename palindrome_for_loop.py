string=input("Enter the string ")
num=[]
for i in range(int(len(string)/2)):
    if string[i] == string[len(string)-i-1]:
        if i == ((int(len(string)/2))-1):
            print(string," is a palindrome")
if string[i]!= string[len(string)-i-1]:
    print(string ," is not palindrome")
           