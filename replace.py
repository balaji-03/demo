"""
no_names=int(input("Enter the number of names "))
cars=[]
for i in range(no_names):
    name=input("Enter the car name : ")
    cars.append(name)
print("Original car names are ",cars)
new_car=[]
old=input("Enter the word to be replaced ")
new=input("Enter the replacement word ")
for i in cars:
    
        car=i.replace(old,new)
        new_car.append(car)
print(new_car)
"""

no_names=int(input("Enter the number of names "))
cars=[]
for i in range(no_names):
    name=input("Enter the car name : ")
    cars.append(name)
print("Original car names are ",cars)

old=input("Enter the word to be replaced ")
new=input("Enter the replacement word ")
c=cars.index(old)
cars[c]=new
print(cars)