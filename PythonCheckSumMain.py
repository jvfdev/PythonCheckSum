from Tkinter import *
window = Tk()
window.title("Python Checksum Tool")
window.geometry('800x450')


lbl = Label(window, text= "Hello There!",font=("Arial Bold", 25))
lbl.grid(column=0, row=0)



def clicked():
    lbl.configure(text="Button was clicked")
    
btn = Button(window, text="click me", command=clicked)
btn.grid(column=1, row=0)

txt = Entry(window,width=10)
txt.grid(column=2, row=0)

window.mainloop()
