from tkinter import*
import time

root = Tk()
root.title("Clock")
root.geometry("350x200")

root.wm_attributes("-transparentcolor",root['bg'])

def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)

clock = Label(root,font=("times new roman",50,"bold"),fg="white")
clock.grid(pady=25,padx=50)
times()

label = Label(root,text="    hours       minutes       seconds",font=("times new roman",15,"bold"),fg="white")
label.grid(row=1,column=0)

root.mainloop()


# print(calendar.calendar(2023))

# print(calendar.month(2020,5))

# print(calendar.monthcalendar(2020,5))

# day_name=calendar.weekday(2020,5,26)
# print(day_name)

# print(calendar.weekheader(3))

# month_name=calendar.monthrange(2020,5)
# print(month_name)

#print(calendar.firstweekday())