import tkinter as tk
from tkinter import *     # build GUI in python
from tksheet import Sheet  # for spreadsheet like excel 
from tkinter import ttk
from tkinter import simpledialog
from tkinter.simpledialog import Dialog # to show dialog box when button pressed
import csv
from tkinter import filedialog  # load data from file




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




def create_frame(root):

	global sheet1 , heading
	# Frame 1 

	frame1 = tk.Frame(root, bg="white", width=700, height=300)
	frame1.grid(row=0 ,column=0,padx=10, pady =10 ,sticky="nsew")
	sheet1 = Sheet(frame1,width = 660 ,height=400, headers =["time","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])

	heading = tk.Label(frame1, text='college timetable')
	heading.pack()

	# frame 2 

	frame2 = tk.Frame(root, bg="white", width=700, height=300)
	frame2.grid( row=0 , column=1 , padx=10  ,pady=10, sticky="nsew" )

	sheet2 = Sheet(frame2,width = 660 ,height=500, headers =["time","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])

	sheet1.enable_bindings(
			(
			 "single_select",
			 "arrowkeys",
			 "edit_cell",
			 "column_width_resize",
			 "double_click_column_resize" # added double click column resize
			)
			)

	sheet2.enable_bindings(
			(
			 "single_select",
			 "arrowkeys",
			 "edit_cell",
			 "column_width_resize",
			 "double_click_column_resize" # added double click column resize
			)
			)



	sheet1.pack(side="right",fill=BOTH, expand=True)
	sheet2.pack(side="left" , fill=BOTH, expand=True)


def create_buttons(root):
    global file_button, print_button, school_college_button, find_button, find_replace_button, insert_row_button  

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
            school_college_button = tk.Button(button_frame, text=label_text, command=change_heading)
            school_college_button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        elif label_text == "Find (Ctrl-F)":
            find_button = tk.Button(button_frame, text=label_text, command=show_find_dialog)
            find_button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        elif label_text == "Find/Replace":
            find_replace_button = tk.Button(button_frame, text=label_text, command=show_find_replace_dialog)
            find_replace_button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        elif label_text == "insert_row":
            insert_row_button = tk.Button(button_frame, text=label_text, command=insert_row)  
            insert_row_button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        else:
            button = tk.Button(button_frame, text=label_text)
            button.grid(row=i // 4, column=i % 4, padx=5, pady=5)

def show_file_menu():
    file_menu = tk.Menu(root, tearoff=0)
    file_menu.add_command(label="New Timetable")
    file_menu.add_command(label="Save Timetable" , command=save_to_csv)
    file_menu.add_command(label="Save Timetable As")
    file_menu.add_command(label="Load Timetable" , command=load_data )
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
    num_rows = sheet1.total_rows()
    num_cols = sheet1.total_columns()
    for i  in range( num_rows):
	    for j in range(num_cols):
		    cell_data = sheet1.get_cell_data(i ,j , get_displayed = False)
		    if (text_to_find == cell_data) :
			    sheet1.highlight_cells(row=i  ,column=j , bg="yellow")


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


# perform find_replace in tksheet 
def show_find_replace_dialog():
    # Create a dialog box for finding text using simpledialog
    dialog = FindReplaceDialog(root)
    num_rows = sheet1.total_rows()
    num_cols = sheet1.total_columns()
    for i  in range( num_rows):
	    for j in range(num_cols):
		    cell_data = sheet1.get_cell_data(i ,j , get_displayed = False)
		    if (dialog.text_to_find == cell_data) :
			    sheet1.set_cell_data(i , j ,dialog.text_to_replace)






def create_teacher_code_entry(root):
    entry_frame = tk.Frame(root)
    entry_frame.grid(row=1, column=0, sticky="sw", padx=10, pady=10)

    label = tk.Label(entry_frame, text="Teacher Code:")
    label.pack(side="left")

    entry = tk.Entry(entry_frame)
    entry.pack(side="left")

# create a button to save the sheet to a CSV file
def save_to_csv():
    file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    if file_path:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(sheet1.get_sheet_data())


# function to load data from csv file 

def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        with open(file_path, "r") as file:
            data = [line.strip().split(",") for line in file]
            sheet1.set_sheet_data(data)


def insert_row():
    sheet1.insert_row()


# function to set college name 

def change_heading():
    new_heading = simpledialog.askstring('set college name' , 'college name')
    if new_heading:
        heading.config(text=new_heading)





def main():
    global root
    root = tk.Tk()
    root.title("Timetable")
    create_frame(root)
    create_buttons(root)
    create_teacher_code_entry(root)
    #root.rowconfigure(0, weight=1)
    #root.columnconfigure(0, weight=1)
    #root.columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()






