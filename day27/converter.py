# day27/converter.py
# miles to km conversion
import tkinter
factor = 1.60934
# inverse = 6.213727366498068

window = tkinter.Tk()
window.title("Miles to Kilometers")
window.geometry("500x500")
window.config(padx=10, pady=10)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.rowconfigure(2, weight=1)
window.columnconfigure(2, weight=1)


def calculate():
    value = entry.get()

    try:
        if not value.isnumeric:
            raise ValueError("Must be numeric")
        label_calc.config(text=float(value) * factor)
    except ValueError as e:
        label_calc.config(text="Must be numeric")


# row0
entry = tkinter.Entry(width=20)
entry.insert(tkinter.END, string="0")
entry.grid(column=1, row=0)

label_miles = tkinter.Label(text="miles")
label_miles.grid(column=2, row=0)

# row1
label_is_eq = tkinter.Label(text="is equal to")
label_is_eq.grid(column=0, row=1)

label_calc = tkinter.Label(text="0")
label_calc.grid(column=1, row=1)

label_km = tkinter.Label(text="km")
label_km.grid(column=2, row=1)

# row2
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# always has to be at the bottom of the program
window.mainloop()
