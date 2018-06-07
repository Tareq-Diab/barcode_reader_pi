from tkinter import*
root=Tk()
frame=Frame(root,width=900 , height=400)
color= open('bin/color.txt','r').read()
frame.config(bg=color)
root.title("Barcode Scanner")

frame.pack()
frameg=Frame(root)
frameg.place(relx=0.1, rely=.3)
def donothing():
    print  ('nothing')

MyButton3 = Button(frame, text="scan", width=10, command=donothing,fg='blue')
MyButton3.place(relx=.2, rely=.6)
MyButton2 = Button(frame, text="delete", width=10, command=donothing,fg='red')
MyButton2.place(relx=.3, rely=.6)

up = Button(frame, text="up", width=10, command=donothing,fg='green')
up.place(relx=.01, rely=.3)
down = Button(frame, text="down", width=10, command=donothing,fg='green')
down.place(relx=.01, rely=.5)
empty = Button(frame, text="empty the cart", width=13, command=donothing,fg='red')
empty.place(relx=0.23, rely=.7)


#--------------------------statusbar--------------------------------------------

status = Label(root,text= 'wating for user to scan his barcode',bd=3,relief=SUNKEN, anchor=W)#bd is  boarder , rellief , anchore to the w 'west'
status.pack(side=BOTTOM,fill=X)

#----------------------------------------------------
photo=PhotoImage(file="bin/facebook.png")
label =Label(root , image=photo)

label.place(relx=0.5,rely=0.1)

photo2=PhotoImage(file="bin/user.png")
label2 =Label(root , image=photo2)

label2.place(relx=0.75,rely=0.1)

#_________________________________________________________

name=Label(root, text='user name: ',bg="black",fg="white")
user=Label(root, text='tareq ahmed fahmy',bg="black",fg="white")
name.place(relx=0.78, rely=0.65)
user.place(relx=0.84, rely=0.65)

num=Label(root, text='number',bg=color)

price=Label(root, text='price',bg=color)
img=Label(root, text='image',bg=color)
num.place(relx=0.15, rely=0.25)
price.place(relx=0.27, rely=0.25)
img.place(relx=0.4, rely=0.25)
height = 5
width = 3
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(frameg, text="")
        b.grid(row=i, column=j)




"""
"""



    



menu=Menu(root)
root.config(menu=menu)# means that i am configuring a menu called menu
#--------------------------------
submenu=Menu(menu)

options=Menu(menu)
menu.add_cascade(label='options',menu=options)

options.add_command(label='redo')
#---------------------------------------------
edit=Menu(menu)
menu.add_cascade(label='edit',menu=edit)

edit.add_command(label='redo')
#---------------------------------------------
def yellow():
      color="yellow"
      guifile=open('bin/color.txt','w')
      guifile.write(color)
      guifile.close()
      frame.config(bg="yellow")
      num.config(bg="yellow")
      img.config(bg="yellow")
      price.config(bg="yellow")
      
      
def red():
      color="red"
      guifile=open('bin/color.txt','w')
      guifile.write(color)
      guifile.close()
      frame.config(bg="red")
      num.config(bg="red")
      img.config(bg="red")
      price.config(bg="red")
      
      


def white():
      color="white"
      guifile=open('bin/color.txt','w')
      guifile.write(color)
      guifile.close()
      frame.config(bg="white")
      num.config(bg="white")
      img.config(bg="white")
      price.config(bg="white")
      
      


def gray():
      color="gray"
      guifile=open('bin/color.txt','w')
      guifile.write(color)
      guifile.close()
      frame.config(bg="gray")
      num.config(bg="gray")
      img.config(bg="gray")
      price.config(bg="gray")
      
      




def green():
      color="green"
      guifile=open('bin/color.txt','w')
      guifile.write(color)
      guifile.close()
      frame.config(bg="green")
      num.config(bg="green")
      img.config(bg="green")
      price.config(bg="green")
      
      


    

    

menu.add_cascade(label='color',menu=submenu)

submenu.add_command(label='yellow',command=yellow)
submenu.add_command(label='red',command=red)
submenu.add_command(label='white',command=white)
submenu.add_command(label='green',command=green)
submenu.add_command(label='gray',command=gray)



#--------------------------------------

root.mainloop()
