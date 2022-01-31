from tkinter import *
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<20 or y1<20): 
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    fps=100
    canvas.after(1000//fps,shift)

############# Main program ###############
from tkinter import *
root=Tk()
root.title('Phonebook concept')
canvas=Canvas(root,bg='black')
canvas.pack(fill=BOTH, expand=20)
text_var="Enter the option \n 1.Add the details \n 2.Modify the details \n 3.Display details \n 4.Delete the details "
text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',20,'bold'),fill='white',tags=("marquee",),anchor='w')
Label(root,padx=20,pady=20,font='GREEN').pack()
x1,y1,x2,y2 = canvas.bbox("marquee")
width = x2-x1
height = y2-y1
canvas['width']=width
canvas['height']=height
    
shift()


def nextPage():
   root.destroy() 
   import page2 
def prevPage():
    root.destroy()
    import page3
Button(
    root, 
    text="Previous Page",
    font=("arial",20),
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root, 
    text="Next Page", 
    font=("arial",20),
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

root.mainloop()

from tkinter import *
root=Tk()
root.title('Phonebook concept')
def nextPage():
   root.destroy() 
   import page3
def prevPage():
    root.destroy()
    import page1
Label(root,text='Enter the employee details or information',
padx=2,pady=2,font=('green')).pack(side=TOP)
Button(
    root, 
    text="Previous Page",
    font=("arial",20),
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root, 
    text="Next Page", 
    font=("arial",20),
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)
root.mainloop()

"""
from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg']='#ffbf00'

font = ("Times bold", 20)

    
def nextPage():
    ws.destroy()
    import page2

def prevPage():
    ws.destroy()
    import page3
    
Label(
   
    ws,
    
    #font = ("Times bold", 30)
    padx=20,
    pady=20,
    bg='blue',
    font='GREEN'
).pack(expand=TRUE,fill=BOTH)

def shift():
        canvas=Canvas(ws,bg='red')
        canvas.pack(fill=BOTH, expand=TRUE)
        text_var="Enter the option \n 1.Add the details \n 2.Modify the details \n\b 3.Display details \n 4.delete the details"
        text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',20,'bold'),fill='white',tags=("marquee",),anchor='w')
        x1,y1,x2,y2 = canvas.bbox("marquee")
        width=x2-x1
        height=y2-y1
        canvas['width']=width
        canvas['height']=height
        fps=40   
        canvas.move("marquee",-10,40)
        shift()

    

Button(
    ws, 
    text="Previous Page", 
    font=font,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="Next Page", 
    font=font,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg']='#ffbf00'

f = ("Times bold", 20)
 
def nextPage():
    ws.destroy()
    import page3

def prevPage():
    ws.destroy()
    import page1

Label(
    ws,
    text="This is Second page",
    padx=20,
    pady=20,
    bg='#ffbf00',
    font=font
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Previous Page", 
    font=font,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws, 
    text="Next Page", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
"""