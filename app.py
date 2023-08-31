import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    weight_str = weight_entry.get()
    height_str = height_entry.get()

    if not weight_str or not height_str:
        result_label.config(text="Please enter valid weight and height.")
        return

    try:
        weight = float(weight_str)
        height = float(height_str)
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers for weight and height.")
        return

    bmi = weight / (height ** 2)
    interpretation = interpret_bmi(bmi)

    result_label.config(text=f"Your BMI is: {bmi:.2f}\nInterpretation: {interpretation}")

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal weight"
    elif bmi <= 30:
        return "Overweight"
    elif bmi >= 35 and bmi <= 40:
        return "Obese"
    
    return "سير اتعالج"

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("1000x400")  # Set the initial window size
root.configure(bg="black")  # Set the background color

# Configure style
style = ttk.Style()
style.configure("TFrame", background="black")
style.configure("TButton", background="black", foreground="red", font=("Times New Roman", 30))
style.configure("TLabel", background="black", foreground="red", font=("Times New Roman", 30))

# Create and configure the input frame
input_frame = ttk.Frame(root)
input_frame.pack(pady=20)

weight_label = ttk.Label(input_frame, text="Enter your weight in kilograms:")
weight_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

weight_entry = ttk.Entry(input_frame, font=("Times New Roman", 30), background="black", foreground="red")
weight_entry.grid(row=0, column=1, padx=10, pady=5)

height_label = ttk.Label(input_frame, text="Enter your height in meters:")
height_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

height_entry = ttk.Entry(input_frame, font=("Times New Roman", 30), background="black", foreground="red")
height_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = ttk.Button(input_frame, text="Calculate BMI", command=calculate_bmi, style="TButton")
calculate_button.grid(row=2, columnspan=2, padx=10, pady=15)

# Center-align the input frame
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

# Create and configure the result label
result_label = ttk.Label(root, text="", font=("Times New Roman", 30))
result_label.pack()

root.mainloop()
