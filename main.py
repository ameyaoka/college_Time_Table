import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter.simpledialog import Dialog

column_names = [
    "Time",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

button_labels = [
    "File Menu",
    "Print Menu",
    "Demo Time...",
    "Freeze Cell...",
    "Find (Ctrl-F)",
    "Find/Replace",
    "Swap Time...",
    "Remove Cl...",
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

# Create a dictionary to store editable cell values
editable_cells = {}

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

    treeview = ttk.Treeview(frame, columns=column_names, show="headings", selectmode="browse")
    
    # Set column headings and adjust column width
    for col_name in column_names:
        treeview.heading(col_name, text=col_name)
        treeview.column(col_name, width=80)  # Adjust the width as needed

    for i in range(1, 101):  # Increase the number of rows for scrolling demonstration
        item_values = [f"Time {i}"] + [f"Data {i*j}" for j in range(2, 9)]
        treeview.insert("", "end", values=item_values)

    treeview.pack(expand=True, fill="both")

    # Add a vertical scrollbar to the right of the Treeview
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=treeview.yview)
    scrollbar.pack(side="right", fill="y")
    treeview.configure(yscrollcommand=scrollbar.set)




    # Bind double-click event to each cell
    for col_name in column_names:
        treeview.bind('<Double-1>', lambda event, col=col_name: edit_cell(event, col, treeview))

def edit_cell(event, column, treeview):
    item = treeview.selection()[0]
    value = treeview.item(item, 'values')[column_names.index(column)]

    # Create an Entry widget to edit the cell
    entry = tk.Entry(treeview, justify='center')
    entry.insert(0, value)
    
    # Get the column index using the column name
    col_index = column_names.index(column)
    
    entry.grid(row=event.widget.index(item), column=col_index + 1, padx=1, pady=1, sticky="nsew")
    entry.bind('<Return>', lambda event, item=item, column=column, entry=entry: save_edit(event, item, column, entry))

def save_edit(event, item, column, entry):
    new_value = entry.get()
    event.widget.item(item, values=(event.widget.item(item, "values")[0], new_value))
    entry.grid_remove()  # Remove the Entry widget



def save_edit(event, item, column, entry):
    edited_value = entry.get()
    event.widget.item(item, values=(event.widget.item(item, "values")[0], edited_value))
    entry.destroy()
    del editable_cells[(item, column)]

def cancel_edit(event, entry):
    entry.destroy()

def create_buttons(root):
    global file_button, print_button, school_college_button, find_button, find_replace_button

    button_frame = tk.Frame(root)
    button_frame.grid(row=1, column=1, sticky="se", padx=10, pady=10)

    # Create buttons with specified labels
    for i, label_text in enumerate(button_labels):
        if label_text == "File Menu":
            file_button = tk.Button(button_frame, text=label_text, command=show_file_menu)
            file_button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        elif label_text == "Print Menu":
            print_button = tk.Button(button_frame, text=label_text, command=show_print_menu)
            print_button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        elif label_text == "SCHOOL/C...":
            school_college_button = tk.Button(button_frame, text=label_text, command=show_school_college_dialog)
            school_college_button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        elif label_text == "Find (Ctrl-F)":
            find_button = tk.Button(button_frame, text=label_text, command=show_find_dialog)
            find_button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        elif label_text == "Find/Replace":
            find_replace_button = tk.Button(button_frame, text=label_text, command=show_find_replace_dialog)
            find_replace_button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        else:
            button = tk.Button(button_frame, text=label_text)
            button.grid(row=i // 4, column=i % 4, padx=5, pady=5)

def show_file_menu():
    file_menu = tk.Menu(root, tearoff=0)
    file_menu.add_command(label="New Timetable")
    file_menu.add_command(label="Save Timetable")
    file_menu.add_command(label="Save Timetable As")
    file_menu.add_command(label="Load Timetable")
    file_menu.add_separator()
    file_menu.add_command(label="Close Popup")

    # Display the popup menu at the location of the "File Menu" button
    file_menu.post(file_button.winfo_rootx(), file_button.winfo_rooty() + file_button.winfo_height())

def show_print_menu():
    print_menu = tk.Menu(root, tearoff=0)
    print_menu.add_command(label="Print Current")
    print_menu.add_command(label="Print All Individuals")
    print_menu.add_command(label="Print All Classes")
    print_menu.add_command(label="Print Master Table")
    print_menu.add_separator()
    print_menu.add_command(label="Close Popup")

    # Display the popup menu at the location of the "Print Menu" button
    print_menu.post(print_button.winfo_rootx(), print_button.winfo_rooty() + print_button.winfo_height())

def show_school_college_dialog():
    # Create a dialog box for entering school/college name using simpledialog
    school_college_name = simpledialog.askstring("Add School/College Name", "Enter School/College Name:")
    if school_college_name:
        # Perform some action with the entered school/college name (e.g., store it)
        print(f"Entered School/College Name: {school_college_name}")

def show_find_dialog():
    # Create a dialog box for finding text using simpledialog
    text_to_find = simpledialog.askstring("Find (Ctrl-F)", "Input Word to Find:")
    if text_to_find:
        # Perform the find operation (e.g., search in the spreadsheet)
        # You can customize this part based on your application
        print(f"Searching for: {text_to_find}")

class FindReplaceDialog(Dialog):
    def __init__(self, parent):
        self.text_to_find = ""
        self.text_to_replace = ""
        super().__init__(parent)

    def body(self, frame):
        find_label = tk.Label(frame, text="Find:")
        find_label.grid(row=0, column=0, padx=10, pady=5)

        self.find_entry = tk.Entry(frame)
        self.find_entry.grid(row=0, column=1, padx=10, pady=5)

        replace_label = tk.Label(frame, text="Replace:")
        replace_label.grid(row=1, column=0, padx=10, pady=5)

        self.replace_entry = tk.Entry(frame)
        self.replace_entry.grid(row=1, column=1, padx=10, pady=5)

        return self.find_entry  # Focus on the Find entry field

    def apply(self):
        self.text_to_find = self.find_entry.get()
        self.text_to_replace = self.replace_entry.get()

def show_find_replace_dialog():
    dialog = FindReplaceDialog(root)
    if dialog.text_to_find:
        # Perform the find and replace operation (e.g., search in the spreadsheet)
        # You can customize this part based on your application
        print(f"Finding and Replacing: '{dialog.text_to_find}' with '{dialog.text_to_replace}'")

def create_teacher_code_entry(root):
    entry_frame = tk.Frame(root)
    entry_frame.grid(row=1, column=0, sticky="sw", padx=10, pady=10)

    label = tk.Label(entry_frame, text="Teacher Code:")
    label.pack(side="left")

    entry = tk.Entry(entry_frame)
    entry.pack(side="left")

def main():
    global root
    root = tk.Tk()
    root.title("Timetable")

    create_frame(root, "Frame 1", 0, 0)
    create_frame(root, "Frame 2", 0, 1)
    create_buttons(root)
    create_teacher_code_entry(root)

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()

