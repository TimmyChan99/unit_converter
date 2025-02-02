from tkinter import *
from tkinter import ttk
from converter import convert_length, convert_temperature, convert_weight


def create_conversion_tab(parent, title, units, convert_function):
    tab = ttk.Frame(parent)
    parent.add(tab, text=title)

    input_var = StringVar()
    from_unit_var = StringVar()
    to_unit_var = StringVar()
    result_label = Label(tab, text="")

    Label(tab, text=title).grid(row=0, column=0)
    Entry(tab, textvariable=input_var).grid(row=0, column=1)

    Label(tab, text='From').grid(row=1, column=0)
    from_unit_box = ttk.Combobox(tab, textvariable=from_unit_var, values=units)
    from_unit_box.grid(row=1, column=1)
    from_unit_box.current(0)

    Label(tab, text='To').grid(row=2, column=0)
    to_unit_box = ttk.Combobox(tab, textvariable=to_unit_var, values=units)
    to_unit_box.grid(row=2, column=1)
    to_unit_box.current(0)

    def convert():
        try:
            value = float(input_var.get())
            result = convert_function(value, from_unit_var.get(), to_unit_var.get())
            result_label.config(text=f'{value} {from_unit_var.get()} = {result} {to_unit_var.get()}')
        except ValueError:
            result_label.config(text='Invalid input! Enter a number.')

    Button(tab, text="Submit", command=convert).grid(row=3, column=0, columnspan=2)
    result_label.grid(row=4, column=0, columnspan=2)

    return tab


def main():
    window = Tk(className="Unit Converter")
    tab_control = ttk.Notebook(window)

    create_conversion_tab(tab_control, "Length",
                          ['meter', 'millimeter', 'centimeter', 'kilometer', 'inch', 'foot', 'yard', 'mile'],
                          convert_length)
    create_conversion_tab(tab_control, "Temperature", ['kelvin', 'celsius', 'fahrenheit'], convert_temperature)
    create_conversion_tab(tab_control, "Weight",
                          ['gram', 'kilogram', 'milligram', 'microgram', 'tonne', 'pound', 'ounce', 'stone'],
                          convert_weight)

    tab_control.pack(expand=1, fill='both')
    window.mainloop()


if __name__ == "__main__":
    main()
