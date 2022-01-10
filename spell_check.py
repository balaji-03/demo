
def dic(a):
    with open("D:\\Balaji\\Git\\Demo\\Dictionary.txt") as dicty:
        for i in dicty:
            for j in i.split():
                if j != a:
                    print(j) 
with open("D:\\Balaji\\Git\\Demo\\users.txt" )as users:
    for k in users:
        for l in k.split():
            dic(l)
           
