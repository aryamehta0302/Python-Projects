import tkinter as tk
from tkinter import *

window = Tk()
window.title("Weight Converter")
window.geometry("600x500")
window.config(bg="#2C2F33")

input_frame = Frame(window, bg="#2C2F33")
input_frame.pack(pady=20)

output_frame = Frame(window, bg="#23272A")
output_frame.pack(pady=20)

Label(input_frame, text="WEIGHT CONVERTER", font=("Helvetica", 24, "bold"), bg="#7289DA", fg='white').grid(row=0, columnspan=2, pady=10)
Label(input_frame, text="Enter the weight in Kgs", font=("Helvetica", 14), bg="#2C2F33", fg="white").grid(row=1, column=0, padx=10, pady=10)

kg = tk.DoubleVar()
Entry(input_frame, textvariable=kg, width=10, font=("Helvetica", 14), bg="#99AAB5", fg="black", justify="center").grid(row=1, column=1, padx=10, pady=10)

def clear_output():
    for widget in output_frame.winfo_children():
        widget.destroy()

def convert_to_gram():
    clear_output()
    gram = kg.get() * 1000
    Label(output_frame, text=f"{gram:.2f} grams", font=("Helvetica", 16, "bold"), bg="#23272A", fg="#43B581").pack(pady=10)

def convert_to_ounce():
    clear_output()
    ounce = kg.get() * 35.274
    Label(output_frame, text=f"{ounce:.2f} ounces", font=("Helvetica", 16, "bold"), bg="#23272A", fg="#F04747").pack(pady=10)

def convert_to_pound():
    clear_output()
    pound = kg.get() * 2.20462
    Label(output_frame, text=f"{pound:.2f} pounds", font=("Helvetica", 16, "bold"), bg="#23272A", fg="#FAA61A").pack(pady=10)

def convert_to_ton():
    clear_output()
    ton = kg.get() / 1000
    Label(output_frame, text=f"{ton:.6f} tons", font=("Helvetica", 16, "bold"), bg="#23272A", fg="#7289DA").pack(pady=10)

Button(input_frame, text="Convert to Gram", bg="#5865F2", fg="white", font=("Helvetica", 14), command=convert_to_gram).grid(row=2, column=0, padx=10, pady=10)
Button(input_frame, text="Convert to Ounce", bg="#43B581", fg="white", font=("Helvetica", 14), command=convert_to_ounce).grid(row=2, column=1, padx=10, pady=10)
Button(input_frame, text="Convert to Pound", bg="#FAA61A", fg="white", font=("Helvetica", 14), command=convert_to_pound).grid(row=3, column=0, columnspan=2, pady=10)
Button(input_frame, text="Convert to Ton", bg="#F04747", fg="white", font=("Helvetica", 14), command=convert_to_ton).grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
