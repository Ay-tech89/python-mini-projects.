from tkinter import*
from tkinter import messagebox

root = Tk()

#root.config(bg="black")
#root.geometry("500x500")
#title = Label(root,text="Tik tok toe",font=("Goudy old style",30,"bold")).place(x=150,y=10)


clicked = True
count = 0

def disable_all_button():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)

def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"]=="X" and b3["text"] =="X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation X win")
        disable_all_button()
    elif b4["text"] == "X" and b5["text"]=="X" and b6["text"] =="X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation X win")
        disable_all_button()
    elif b7["text"] == "X" and b8["text"]=="X" and b9["text"] =="X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation X win")
        disable_all_button()
    elif b1["text"] == "X" and b4["text"]=="X" and b7["text"] =="X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation X win")
        disable_all_button()
    elif b2["text"] == "X" and b5["text"]=="X" and b8["text"] =="X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation X win")
        disable_all_button()
    elif b3["text"] == "X" and b6["text"]=="X" and b9["text"] =="X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation X win")
        disable_all_button()
    elif b1["text"] == "X" and b5["text"]=="X" and b9["text"] =="X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation X win")
        disable_all_button()
    elif b3["text"] == "X" and b5["text"]=="X" and b7["text"] =="X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation X win")
        disable_all_button()

# O win
    if b1["text"] == "O" and b2["text"]=="O" and b3["text"] =="O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation O win")
        disable_all_button()
    elif b4["text"] == "O" and b5["text"]=="O" and b6["text"] =="O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation O win")
        disable_all_button()
    elif b7["text"] == "O" and b8["text"]=="O" and b9["text"] =="O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation O win")
        disable_all_button()
    elif b1["text"] == "O" and b4["text"]=="O" and b7["text"] =="O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation O win")
        disable_all_button()
    elif b2["text"] == "O" and b5["text"]=="O" and b8["text"] =="O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation O win")
        disable_all_button()
    elif b3["text"] == "O" and b6["text"]=="O" and b9["text"] =="O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation O win")
        disable_all_button()
    elif b1["text"] == "O" and b5["text"]=="O" and b9["text"] =="O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation O win")
        disable_all_button()
    elif b3["text"] == "O" and b5["text"]=="O" and b7["text"] =="O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tik tok toe","Congratulation O win")
        disable_all_button()

def b_click(b):  
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] ="X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False: 
        b["text"] = "O"
        clicked = True
        count +=1
        checkifwon()
    else:
        messagebox.showerror("Tik Tok Toe","click another")


b1 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command=lambda:b_click(b1))
b2 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command=lambda:b_click(b2))
b3 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command=lambda:b_click(b3))

b4 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command=lambda:b_click(b4))
b5 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command=lambda:b_click(b5))
b6 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command=lambda:b_click(b6))

b7 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command=lambda:b_click(b7))
b8 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command=lambda:b_click(b8))
b9 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command=lambda:b_click(b9))

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

root.mainloop()