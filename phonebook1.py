def phone(x):
    match x:
        case '1' :
            myFile="C:\\Users\\balaji\\Desktop\\phone.csv"
            import csv
            Name=input("Name : ")
            Mobile_no=input("Mobile_no : ")
            Dep = input("Department : ")
            email=input(" email : ")
            with open(myFile, "a",newline="") as f:
                print('\n')
                append = csv.writer(f)
                append.writerow([Name+','+Mobile_no+','+Dep+','+email])
            f.close()   
        case '2':
            old=input("old ")
            new=input("new ")
            text = open("C:\\Users\\balaji\\Desktop\\phone.csv", "r")
            text = ''.join([i for i in text]).replace(old, new)
            print(text)
            x = open("C:\\Users\\balaji\\Desktop\\phone.csv","w")
            x.writelines(text)
            x.close()
        case '3':
            myFile="C:\\Users\\balaji\\Desktop\\phone.csv"
            import csv
            display=input("Enter details of name to be fetched ")
            with open(myFile,"r") as f:
                read = csv.reader(f)
                #head = next(read)
                for row in read:
                    if display == row[0]:
                        print(row)
            f.close()
        case '4':
            lines=[]
            myFile="C:\\Users\\balaji\\Desktop\\phone.csv"
            import csv
            display=input("Enter details of name to be fetched ")
            with open(myFile,"r") as f:
                read=csv.reader(f)
                
                for row in read:
                    lines.append(row)
                    for field in row:
                        if field == display:
                            lines.remove(row)
            with open(myFile,"w") as f:
                write=csv.writer(f)
                write.writerows(lines)
            f.close()        
user=input("Enter \n 1.Add detail \n 2.Modify details \n 3.Display details \n 4.Delete details ")
phone(user)
