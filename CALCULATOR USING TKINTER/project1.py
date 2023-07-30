import tkinter as tk

def on_button_click(event):
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget to display the result
entry = tk.Entry(root, font=("Arial", 20), justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Define the button text in a 2D array
button_texts = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

# Create buttons and add them to the button frame
for i in range(4):
    for j in range(4):
        button = tk.Button(button_frame, text=button_texts[i][j], font=("Arial", 20), padx=20, pady=20)
        button.grid(row=i, column=j, padx=5, pady=5)
        button.bind("<Button-1>", on_button_click)

# Run the Tkinter event loop
root.mainloop()
