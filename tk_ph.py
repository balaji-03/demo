from tkinter import *

root = Tk()
root.title("Phonebook")
root.geometry('500x450')

name1=StringVar()
mobile1=StringVar()
dep1=StringVar()
email1=StringVar()

modify1 = StringVar()
new1 = StringVar()
choice1=StringVar()

disp1=StringVar()

l_add=Label(root,text='Name',font=('calibre',10,'bold'))
e_add=Entry(root,textvariable=name1,font=('calibre',10,'normal'))

l1_add=Label(root,text='Mobile_no',font=('calibre',10,'bold'))
e1_add=Entry(root,textvariable=mobile1,font=('calibre',10,'normal'))

l2_add=Label(root,text='Department',font=('calibre',10,'bold'))
e2_add=Entry(root,textvariable=dep1,font=('calibre',10,'normal'))

l3_add=Label(root,text='email',font=('calibre',10,'bold'))
e3_add=Entry(root,textvariable=email1,font=('calibre',10,'normal'))

l4_modify=Label(root,text='Enter the word in file to be modified ',font=('calibre',10,'bold'))
e4_modify=Entry(root,textvariable=modify1,font=('calibre',10,'normal'))
 
l5_modify=Label(root,text='Enter the new word ',font=('calibre',10,'bold'))
e5_modify=Entry(root,textvariable=new1,font=('calibre',10,'normal'))

    
l6_display=Label(root,text='Enter the name whose details are fetched ',font=('calibre',10,'bold'))
e6_display=Entry(root,textvariable=new1,font=('calibre',10,'normal'))

l7_delete=Label(root,text='Enter the name whose details are deleted ',font=('calibre',10,'bold'))
e7_delete=Entry(root,textvariable=new1,font=('calibre',10,'normal'))

l9_add = Label(root,text='The details of the person are added to the file ',font=('calibre',10,'bold'))

l10_modify=Label(root,text = 'The word got modified ',font=('calibre',10,'bold'))

l11_modify=Label(root,text = 'Enter the word in file to be modified ',font=('calibre',10,'bold'))

l12_delete=Label(root,text='Enter the word in file to be deleted ',font=('calibre',10,'bold'))

l13_delete=Label(root,text='The word in file got deleted ',font=('calibre',10,'bold'))

t_display = Text(root,width=40,height=5)
#t_display.insert(INSERT,"Enter the word in file to be displayed")

b_add=Button(root,text='Submit')
b1_modify=Button(root,text = 'Submit')
b2_display=Button(root,text='Submit')
bu_delete = Button(root,text='Submit')

def case1():
# we have used grid_forget() method for all labels, entries and button hiding
    l4_modify.grid_forget()
    e4_modify.grid_forget()
    l5_modify.grid_forget()
    e5_modify.grid_forget()
    
    global b1_modify
    b1_modify.grid_forget()
    
    l6_display.grid_forget()
    e6_display.grid_forget()
    t_display.grid_forget()
    
    global b2_display
    b2_display.grid_forget()
    
    l7_delete.grid_forget()
    e7_delete.grid_forget()
   
    
    global l10_modify
    l10_modify.grid_forget()
    
    global l11_modify
    l11_modify.grid_forget()
    
    global l12_delete
    l12_delete.grid_forget()
    
    global l13_delete
    l13_delete.grid_forget()
    
    global bu_delete
    bu_delete.grid_forget()
    
    def gf():
        name=name1.get()
        mobile=mobile1.get()
        dep=dep1.get()
        email=email1.get()
        with open("D:\\Balaji\\Git\\demo\\phone.txt","a+") as phone:
            phone.write('\n'+name+','+mobile+','+dep+','+email)
            global l9_add
            
            l9_add.grid(row=6,column=2)
    
    global b_add
    b_add=Button(text='submit',command=gf)
    
  
        
    l_add.grid(row=2,column=2)
    e_add.grid(row=2,column=3)
    l1_add.grid(row=3,column=2)
    e1_add.grid(row=3,column=3)
    l2_add.grid(row=4,column=2)
    e2_add.grid(row=4,column=3)
    l3_add.grid(row=5,column=2)
    e3_add.grid(row=5,column=3)
    
    b_add.grid(row=6,column=3)
    #b.visible = False
def case2(): 
 
    l_add.grid_forget()
    e_add.grid_forget()
    l1_add.grid_forget()
    e1_add.grid_forget()
    l2_add.grid_forget()
    e2_add.grid_forget()
    l3_add.grid_forget()
    e3_add.grid_forget()
    
    global b_add
    b_add.grid_forget()
    
    l6_display.grid_forget()
    e6_display.grid_forget()
    t_display.grid_forget()
    
    global b2_display
    b2_display.grid_forget()
    
    l7_delete.grid_forget()
    e7_delete.grid_forget()
    
    global bu_delete
    bu_delete.grid_forget()
   
    global l9_add
    l9_add.grid_forget()
    
    global l12_delete
    l12_delete.grid_forget()
    
    global l13_delete
    l13_delete.grid_forget()
    
    def gf1():
        modify=modify1.get()+','
        new=new1.get()+','
        global ispre
        ispre=0
        with open(r"D:\\Balaji\\Git\\Demo\\phone.txt","r") as phone:
            data=phone.read()
            if modify in data:
                global l10_modify
                #l10_modify=Label(root,text = 'The word got modified ',font=('calibre',10,'bold'))
                l10_modify.grid(row=6,column=2)
                data=data.replace(modify,new)
                ispre = 1    
            if modify not in data:    
                l10_modify.text="Enter the word in file "
        with open(r"D:\\Balaji\\Git\\Demo\\phone.txt","w") as phone:
            phone.write(data)
        phone.close()
        
        return ispre 
     
    def pri(a):
        if a == 0:
            global l11_modify
            
            l11_modify.grid(row=7,column=2)
    global b1_modify
    b1_modify=Button(text='Submit',command=gf1)
    a=gf1()
    pri(a)
    
            
    l4_modify.grid(row=2,column=2)
    e4_modify.grid(row=2,column=3)
    l5_modify.grid(row=3,column=2)
    e5_modify.grid(row=3,column=3)
    b1_modify.grid(row=4,column=2)
def case3():
    global b_add
    b_add.grid_forget()
    l_add.grid_forget()
    e_add.grid_forget()
    l1_add.grid_forget()
    e1_add.grid_forget()
    l2_add.grid_forget()
    e2_add.grid_forget()
    l3_add.grid_forget()
    e3_add.grid_forget()
    
    l9_add.grid_forget()
    
    l4_modify.grid_forget()
    e4_modify.grid_forget()
    l5_modify.grid_forget()
    e5_modify.grid_forget()
    
    global b1_modify
    b1_modify.grid_forget()
    
    l7_delete.grid_forget()
    e7_delete.grid_forget()
    
    global bu_delete
    bu_delete.grid_forget()
    
    global l10_modify
    l10_modify.grid_forget()
    
    global l11_modify
    l11_modify.grid_forget()
    
    global l12_delete
    l12_delete.grid_forget()
    
    global l13_delete
    l13_delete.grid_forget()
    
    
    def dis():
        disp=new1.get()
        phone=open(r"D:\\Balaji\\Git\\Demo\\phone.txt","r")
        
        ispre=0
        for i in phone:
            c = i.split(',')
            if c[0] == disp:
                m=c[0]+','+c[1]+','+c[2]+','+c[3]
                t_display.insert(INSERT,m)
                ispre=1
                return ispre
    a = dis()
    if a == 0:
        t_display.insert(INSERT,"Enter the word in file to be displayed")
                
        
        phone.close()
    
    
    global b2_display
    
    b2_display=Button(root,text='Submit',command=dis) 
    
  
    l6_display.grid(row=3,column=1)
    e6_display.grid(row=3,column=2)
    
    b2_display.grid(row=4,column=2)
    
    t_display.grid(row=5,column=2)

   

def case4():
    ispr =0    
    l_add.grid_forget()
    e_add.grid_forget()
    l1_add.grid_forget()
    e1_add.grid_forget()
    l2_add.grid_forget()
    e2_add.grid_forget()
    l3_add.grid_forget()
    e3_add.grid_forget()
    
    global b_add
    b_add.grid_forget()
    
    l4_modify.grid_forget()
    e4_modify.grid_forget()
    l5_modify.grid_forget()
    e5_modify.grid_forget()
    
    global b1_modify
    b1_modify.grid_forget()
    
    l6_display.grid_forget()
    e6_display.grid_forget()
    t_display.grid_forget()
    
    global b2_display
    b2_display.grid_forget()
    
    l9_add.grid_forget()
    
    global l10_modify
    l10_modify.grid_forget()
    
    global l11_modify
    l11_modify.grid_forget()
    
     
    d =new1.get()
    b=open("D:\\Balaji\\Git\\Demo\\phone.txt","r")
    c=b.readlines()
    b.close()
    def ft():
        global ispr
        ispr =0
        for e in c:
            f=e.split(',')
            if f[0] == d:
                
                ispr = 1
                return f
    
    h=open("D:\\Balaji\\Git\\Demo\\phone.txt","w+")
    bu=Button(root,text='Submit',command=ft)
    o=ft()
    for e in c:
        f=e.split(',')
        if f != o:
            k=f[0]+','+f[1]+','+f[2]+','+f[3]
            h.write(str(k))
            ispr=1
            global l13_delete
            
            l13_delete.grid(row=5,column=1)
    h.close()
    
    if ispr == 0:
        global l12_delete
        
        l12_delete.grid(row=6,column=2)
    a=ft()
    l7_delete.grid(row=2,column=1)
    e7_delete.grid(row=3,column=1)

    bu_delete.grid(row=4,column=1) 
     
la_option=Label(root,text='Choose your option ',font=('calibre',20,'bold'))

bu1_add= Button(root,text='Add the details ',command=case1) 
bu2_modify= Button(root,text='Modify the details ',command=case2) 
bu3_display= Button(root,text='Display the details ',command=case3) 
bu4_delete= Button(root,text='Delete the details',command=case4) 

la_option.grid(row=0,column=0)
bu1_add.grid(row=1,column=0)
bu2_modify.grid(row=2,column=0)
bu3_display.grid(row=3,column=0)
bu4_delete.grid(row=4,column=0)

root.mainloop()
