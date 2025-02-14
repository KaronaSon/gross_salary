import tkinter as tk
from tkinter import messagebox

# Function to calculate tax and net salary
def calculate_salary():
    try:
        gross_salary = float(entry_gross_salary.get()) #Get the gross salary from input
        if gross_salary < 0:
            raise ValueError("Gross salary cannot be negative.")
        
        # Initialize tax rate and payback variables
        tax_rate = 0
        payback = 0
        
        #Determine tax rate and payback based on salary range
        if gross_salary <= 1500000:
            tax_rate = 0 # 0% tax rate
            payback = 0
        elif gross_salary <= 2000000:
            tax_rate = 0.05 # 5% tax rate
            payback = 75000
        elif gross_salary <= 8500000:
            tax_rate = 0.10 # 10% tax rate
            payback = 172500
        elif gross_salary <=12500000:
            tax_rate = 0.15 # 15% tax rate
            payback = 600000
        else:
            tax_rate = 0.20 # 20% tax rate
            payback = 1250000
            
        # Calculate tax and net salary
        tax = (gross_salary * tax_rate) - payback
        net_salary = gross_salary - tax
        
        #Display the results
        label_tax_salary_result.config(text=f"Tax: {tax:.2f} R")
        label_net_salary_result.config(text=f"Net Salary: {net_salary:.2f} R")
        
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")
        
# Create main window
root = tk.Tk()
root.title("Salary Tax Application System")

#Create and place labels, entries, and buttons
label_title = tk.Label(root, text="Salary Tax Application System", font=("Arial", 16))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

label_gross_salary = tk.Label(root, text="Enter Gross Salary (R):")
label_gross_salary.grid(row=1, column=0, padx=10, pady=5)

entry_gross_salary = tk.Entry(root, width=20)
entry_gross_salary.grid(row=1, column=1, padx=10, pady=5)

button_calculate = tk.Button(root, text="Calculate", command=calculate_salary)
button_calculate.grid(row=2, column=0, columnspan=2, pady=10)

label_tax_salary_result = tk.Label(root, text="Tax: 0.00 R")
label_tax_salary_result.grid(row=3, column=0, columnspan=2, pady=5)

label_net_salary_result = tk.Label(root, text="Net Salary: 0.00 R")
label_net_salary_result.grid(row=4, column=0, columnspan=2, pady=5)

#Start the Tkinter event loop
root.mainloop()