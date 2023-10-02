import tkinter as tk
from tkinter import ttk

column_names = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

button_labels = [
    "File Menu",
    "Demo Time...",
    "Freeze Cell...",
    "Find (Ctrl-F)",
    "Find/Replace",
    "Swap Time...",
    "Remove Cl...",
    "Print Menu",
    "Global Cou...",
    "Multi Freeze",
    "Input Wizard",
    "Time Slot S...",
    "Multi Select...",
    "SCHOOL/C...",
    "Printer: No...",
    "Remove Ga...",
    "Clear Freez",
    "Print All Cl...",
    "Insert Row",
    "Delete Row",
    "Help"
]

def create_frame(root, title, row, column):
    frame = tk.Frame(root, bg="white", width=400, height=300)
    frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    label = tk.Label(frame, text=title, font=("Helvetica", 16))
    label.pack(padx=10, pady=10)

    # Define a custom style with cell separation
    style = ttk.Style()
    style.configure("Treeview", rowheight=25, font=("Helvetica", 12))
    style.layout("Treeview.Item",
                 [('Treeitem.padding',
                   {'sticky': 'nswe',
                    'children': [('Treeitem.indicator', {'side': 'left', 'sticky': ''}),
                                 ('Treeitem.image', {'side': 'left', 'sticky': ''}),
                                 ('Treeitem.text', {'side': 'left', 'sticky': ''})]})])

    treeview = ttk.Treeview(frame, columns=column_names, show="headings")
    
    # Set column headings and adjust column width
    for col_name in column_names:
        treeview.heading(col_name, text=col_name)
        treeview.column(col_name, width=80)  # Adjust the width as needed

    for i in range(1, 101):  # Increase the number of rows for scrolling demonstration
        treeview.insert("", "end", values=(f"Row {i}", f"Data {i*2}", f"Data {i*3}", f"Data {i*4}",
                                           f"Data {i*5}", f"Data {i*6}", f"Data {i*7}"))

    treeview.pack(expand=True, fill="both")

    # Add a vertical scrollbar to the right of the Treeview
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=treeview.yview)
    scrollbar.pack(side="right", fill="y")
    treeview.configure(yscrollcommand=scrollbar.set)

def create_buttons(root):
    button_frame = tk.Frame(root)
    button_frame.grid(row=1, column=1, sticky="se", padx=10, pady=10)

    # Create buttons with specified labels
    for i, label_text in enumerate(button_labels):
        button = tk.Button(button_frame, text=label_text)
        button.grid(row=i // 4, column=i % 4, padx=5, pady=5)

def main():
    root = tk.Tk()
    root.title("Two Frames with Spreadsheets and Buttons")

    create_frame(root, "Frame 1", 0, 0)
    create_frame(root, "Frame 2", 0, 1)
    create_buttons(root)

    # Configure row and column weights
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()

