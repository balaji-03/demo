
def dic(a):
    with open("D:\\Balaji\\Git\\Demo\\list1.txt") as dicty:
        print(a)
        for i in dicty:
            for j in i.split():
                if j == a:
                    print(j)
                        
with open("D:\\Balaji\\Git\\Demo\\list2.txt" )as users:
    for k in users:
        for l in k.split():
            dic(l)
           
