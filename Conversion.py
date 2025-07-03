from tkinter import*
import math 

root = Tk()
root.title('Conversion')
root.geometry('800x400')

def convert():
    binary = int(num_En.get())
    value = bin(binary)
    mylabel = Label(root,text= value[2:],font=("Goudy old style",18,'bold'),fg="#52D017",bg="white").place(x=90,y=290)
    a = list(oct(int(binary)))
    b = a[2:]
    mylabel = Label(root,text=b,font=("Goudy old style",18,'bold'),fg="#52D017",bg="white").place(x=270,y=290)
    a = list(hex(int(binary)))
    b = a[2:]
    mylabel = Label(root,text=b,font=("Goudy old style",18,'bold'),fg="#52D017",bg="white").place(x=425,y=290)

def Exit():
    root.destroy()

title = Label(root,text = 'Conversion',font=("Goudy old style",50,'bold'),fg="#52D017",bg="white").pack(pady=10)
num_la = Label(root,text = 'Enter decimal number',font=("Goudy old style",15,'bold'),fg="#52D017",bg="white").place(x=90,y=150)
num_En = Entry(root,font=("times new roman",15),bg="lightgray")
num_En.place(x=90,y=190,width=350,height=35)

num_de = Label(root,text = 'Binary number',font=("Goudy old style",15,'bold'),fg="#52D017",bg="white").place(x=90,y=250)
num_oct = Label(root,text = 'Octal number',font=("Goudy old style",15,'bold'),fg="#52D017",bg="white").place(x=270,y=250)
num_hex = Label(root,text = 'hexadecimal number',font=("Goudy old style",15,'bold'),fg="#52D017",bg="white").place(x=425,y=250)

Convert = Button(root,text="Convert",bg="white",fg="#52D017",bd=5,font=("times new roman",12),command = convert).place(x=90,y=340)
Exit = Button(root,text="Exit",bg="white",fg="#52D017",bd=5,font=("times new roman",12),command = Exit).place(x=210,y=340)


root.mainloop()