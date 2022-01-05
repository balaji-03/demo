string=input("Enter the string")
a=list(string)
b=[]
b=a[::-1]
c=''.join(b)
if c == string:
	print("Its a palindrome")
else:
	print("Not a palindrome")