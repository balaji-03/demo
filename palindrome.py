string=input("Enter the string ")
a=list(string)
b=[]
b=a[::-1]
c=''.join(b)
if c == string:
	print("%s is a palindrome"%string)
else:
	print("%s is not a palindrome"%string)