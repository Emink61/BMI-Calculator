import tkinter as tk

window = tk.Tk()
window.geometry("250x300")

def clicking():
    Name = entry1.get()
    Age = entry2.get()
    try:
        Hight = float(entry3.get())
        Weight = float(entry4.get())*10000
        bmi = Weight / (Hight ** 2)
    except ValueError:
        print("Nah")
        return
    newWindow = tk.Toplevel(window)
    newWindow.geometry("300x200")
    NewWriting = tk.Label(newWindow, text="Your BMI RESULT", font=("Arial",20))
    NewWriting.place(x=30,y=10)
    if bmi <= 18.5:
        BMIResult = tk.Label(newWindow, text=f"{Name}, your BMI Result is: {bmi:.2f}", font=("Arial",12))
        BMIResult.place(x=30, y=60)
        BMIResult2 = tk.Label(newWindow, text="You are Very Weak!", font=("Arial",9))
        BMIResult2.place(x=80, y=100)
    elif bmi > 30:
        BMIResult = tk.Label(newWindow, text=f"{Name}, your BMI Result is: {bmi:.2f}", font=("Arial",12))
        BMIResult.place(x=30, y=60)
        BMIResult2 = tk.Label(newWindow, text="You have Obesite", font=("Arial",9))
        BMIResult2.place(x=80, y=100)
    elif bmi > 25:
        BMIResult = tk.Label(newWindow, text=f"{Name}, your BMI Result is: {bmi:.2f}", font=("Arial",12))
        BMIResult.place(x=30, y=60)
        BMIResult2 = tk.Label(newWindow, text="You are a LITTLE bit Fat!", font=("Arial",9))
        BMIResult2.place(x=80, y=100)
    elif bmi > 18:
        BMIResult = tk.Label(newWindow, text=f"{Name}, your BMI Result is: {bmi:.2f}", font=("Arial",12))
        BMIResult.place(x=30, y=60)
        BMIResult2 = tk.Label(newWindow, text="You are Normal!", font=("Arial",9))
        BMIResult2.place(x=80, y=100)

    print("All saved")

writing = tk.Label(window, text="BMI Calculator", font=("Arial",20))
writing.place(x=30,y=10)
Name = tk.Label(window, text="Enter Name:")
Name.place(x=10,y=60)
Age = tk.Label(window, text="Enter Age:")
Age.place(x=12,y=90)
High = tk.Label(window, text="Enter Height:")
High.place(x=10,y=120)
Kilo = tk.Label(window, text="Enter Weight:")
Kilo.place(x=10,y=150)
entry1 = tk.Entry()
entry1.place(x=90,y=60)
entry2 = tk.Entry()
entry2.place(x=90,y=90)
entry3 = tk.Entry()
entry3.place(x=90,y=120)
entry4 = tk.Entry()
entry4.place(x=90,y=150)

button1 = tk.Button(window, height=1, width=8, text="Save", command=clicking)
button1.place(x=80,y=210)
window.mainloop()