import tkinter

window = tkinter.Tk()
window.title("Hello World")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# my_label
my_label = tkinter.Label(text="Foo Bar Baz", font=("Consolas", 24, "bold"))
# my_label.pack()
#my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

##########
# Button
##########


def button_clicked():
    my_label["text"] = input.get()


button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

##########
# Button2
##########

button2 = tkinter.Button(text="Second Button")
button2.grid(column=2, row=0)

##########
# Entry
##########
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

# always has to be at the bottom of the program
window.mainloop()
