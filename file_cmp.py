def list1(a):
    with open("list1.txt") as list1:
        for i in list1:
            for j in i.split():
                if j == a:
                    print(j)
with open("list2.txt") as list2:
    for k in list2:
        for l in k.split():
            list1(l)