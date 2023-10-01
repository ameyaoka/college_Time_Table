import tkinter as tk
from tkinter import ttk

def create_frame1(root):
    frame1 = tk.Frame(root, bg="blue", width=400, height=400)
    frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    label1 = tk.Label(frame1, text="Frame 1", fg="white", bg="blue", font=("Helvetica", 16))
    label1.pack(padx=10, pady=10)

    # Create a Treeview widget (spreadsheet) in frame1
    tree1 = ttk.Treeview(frame1, columns=("Column1", "Column2", "Column3"))
    tree1.heading("#1", text="Column 1")
    tree1.heading("#2", text="Column 2")
    tree1.heading("#3", text="Column 3")

    # Insert some sample data
    for i in range(50):
        tree1.insert("", "end", values=(f"Data {i+1}", f"Data {i+2}", f"Data {i+3}"))

    tree1.pack(expand=True, fill="both", side="left")  # Adjust the side to the left

    # Create a vertical scrollbar for the spreadsheet
    scrollbar = tk.Scrollbar(frame1, orient="vertical", command=tree1.yview)
    scrollbar.pack(side="right", fill="y")  # Adjust the side to the right

    # Configure the spreadsheet to use the scrollbar
    tree1.configure(yscrollcommand=scrollbar.set)

def create_frame2(root):
    frame2 = tk.Frame(root, bg="green", width=400, height=400)
    frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    label2 = tk.Label(frame2, text="Frame 2", fg="white", bg="green", font=("Helvetica", 16))
    label2.pack(padx=10, pady=10)

    # Create a Treeview widget (table) in frame2
    table2 = ttk.Treeview(frame2, columns=("Column1", "Column2", "Column3"))
    table2.heading("#1", text="Column 1")
    table2.heading("#2", text="Column 2")
    table2.heading("#3", text="Column 3")

    # Insert some sample data
    for i in range(5):
        table2.insert("", "end", values=(f"Data {i+6}", f"Data {i+7}", f"Data {i+8}"))

    table2.pack(expand=True, fill="both")

def create_buttons(root):
    button_frame = tk.Frame(root)
    button_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="se")

    # Create 24 buttons
    for i in range(24):
        button = tk.Button(button_frame, text=f"Button {i+1}")
        button.grid(row=i // 4, column=i % 4, padx=5, pady=5)

def main():
    root = tk.Tk()
    root.title("Two Frames with Spreadsheet, Buttons, and Scrollbar")

    create_frame1(root)
    create_frame2(root)
    create_buttons(root)

    # Configure row and column weights for resizing
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()

