import tkinter as tk
import re

def validate_iban(iban):
    iban = iban.replace(" ","")
    if not re.match("^[A-Z]{2}[0-9]{2}[A-Z0-9]{1,30}$", iban):
        return False
    else:
        return True
    iban = iban[4:] + iban[0:4]
    iban = iban.translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "12345678912345678923456789"))
    return int(iban) % 97 == 1

def on_submit():
    iban = iban_entry.get()
    if validate_iban(iban):
        result_label.configure(text="Valid IBAN", fg="green")
    else:
        result_label.configure(text="Invalid IBAN", fg="red")

app = tk.Tk()
app.title("IBAN Validator")

iban_label = tk.Label(text="Enter IBAN:")
iban_entry = tk.Entry()
result_label = tk.Label()
submit_button = tk.Button(text="Validate", command=on_submit)

iban_label.pack()
iban_entry.pack()
result_label.pack()
submit_button.pack()

app.mainloop()
