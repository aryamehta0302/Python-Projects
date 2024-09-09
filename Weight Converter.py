import tkinter as tk
from tkinter import *

window = Tk()
window.title("PythonGeeks Weight Converter")
window.geometry("500x400")
window.config(bg="white")

input_frame = Frame(window, bg="white")
input_frame.pack(pady=20)

output_frame = Frame(window, bg="white")
output_frame.pack(pady=20)

Label(input_frame, text="WEIGHT CONVERTER", font=("Arial", 20), bg="black", fg='yellow').grid(row=0, columnspan=2, pady=10)
Label(input_frame, text="Enter the weight in Kgs", font=("Arial", 14), bg="white").grid(row=1, column=0, padx=10, pady=10)

kg = tk.IntVar()
Entry(input_frame, textvariable=kg, width=10, font=("Arial", 14)).grid(row=1, column=1, padx=10, pady=10)

def clear_output():
    for widget in output_frame.winfo_children():
        widget.destroy()

def convert_to_gram():
    kg1=kg.get() 
    gram = float(kg1)*1000
    Label(output_frame, text="This weight in grams would be:", font=("Arial", 12), bg="white").pack()
    Label(output_frame, text=f"{gram:.2f} grams", font=("Arial", 14), bg="red", fg="white", width=20).pack(pady=5)

def convert_to_ounce():
    kg1=kg.get()
    ounce = float(kg1)*35.274
    Label(output_frame, text="This weight in ounces would be:", font=("Arial", 12), bg="white").pack()
    Label(output_frame, text=f"{ounce:.2f} ounces", font=("Arial", 14), bg="red", fg="white", width=20).pack(pady=5)

def convert_to_pound():
    kg1=kg.get()
    pound = float(kg1)*2.20462
    Label(output_frame, text="This weight in pounds would be:", font=("Arial", 12), bg="white").pack()
    Label(output_frame, text=f"{pound:.2f} pounds", font=("Arial", 14), bg="red", fg="white", width=20).pack(pady=5)


Button(input_frame, text="Convert to Gram", bg="blue", fg="white", font=("Arial", 12), command=convert_to_gram).grid(row=2, column=0, padx=10, pady=10)
Button(input_frame, text="Convert to Ounce", bg="blue", fg="white", font=("Arial", 12), command=convert_to_ounce).grid(row=2, column=1, padx=10, pady=10)
Button(input_frame, text="Convert to Pound", bg="blue", fg="white", font=("Arial", 12), command=convert_to_pound).grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
