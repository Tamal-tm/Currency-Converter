# Install the CurrencyConverter library before running:
# pip install CurrencyConverter

# Importing CurrencyConverter class for handling currency conversions
from currency_converter import CurrencyConverter  

# Importing tkinter module for GUI (Graphical User Interface)
import tkinter as tk  

# Creating an object of CurrencyConverter class
a = CurrencyConverter()  

# Creating a Tkinter window
window = tk.Tk()  
window.geometry("500x360")  # Setting window size to 500x360 pixels

# ---------------- Function to run when button is clicked ----------------
def clicked():
    amount = int(e1.get())        # Get amount entered in e1 (convert string to int)
    cur1 = e2.get()               # Get source currency code (e.g., USD) from e2
    cur2 = e3.get()               # Get target currency code (e.g., INR) from e3
    data = a.convert(amount, cur1, cur2)  # Perform conversion using CurrencyConverter
    l5.config(text=data)          # Update label l5 with the converted value

# ---------------- Labels and Entry Fields ----------------
# Title Label
l1 = tk.Label(window, text="Currency Converter", font="Times 25 bold")
l1.place(x=100, y=30)

# Label + Entry for amount input
l2 = tk.Label(window, text="Enter amount here: ", font="Times 18 bold")
l2.place(x=50, y=80)
e1 = tk.Entry(window)  # Entry box for entering amount
e1.place(x=280, y=90)

# Label + Entry for source currency input
l3 = tk.Label(window, text="Enter Currency: ", font="Times 18 bold")
l3.place(x=50, y=130)
e2 = tk.Entry(window)  # Entry box for base currency (e.g., USD)
e2.place(x=280, y=140)

# Label + Entry for target currency input
l4 = tk.Label(window, text="Enter Req. Currency: ", font="Times 18 bold")
l4.place(x=50, y=180)
e3 = tk.Entry(window)  # Entry box for target currency (e.g., INR)
e3.place(x=280, y=190)  # <-- FIXED (was overlapping earlier)

# Button to trigger conversion
b1 = tk.Button(window, text="click", command=clicked)
b1.place(x=230, y=240)

# Label to show result (empty initially, updated later)
l5 = tk.Label(window, text="", font="Times 25 bold")
l5.place(x=200, y=290)

# Start the Tkinter event loop (keeps window running)
window.mainloop()


# Example (console only - not GUI):
# a = CurrencyConverter()
# print(a.convert(12, "USD", "INR"))


'''CurrencyConverter() → Loads exchange rates (by default from European Central Bank).

tk.Entry() → Input fields where users type data (amount, currencies).

tk.Label() → Used to display text on the window.

.place(x,y) → Positions widgets on the window using coordinates.

command=clicked → When button is pressed, function clicked() runs.

l5.config(text=data) → Updates existing label text instead of creating a new one every click.

window.mainloop() → Keeps the window running until closed.'''