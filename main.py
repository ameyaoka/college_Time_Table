import tkinter as tk

class SpreadsheetUI:
    def __init__(self, root):
        # Create a label for the title
        title_label = tk.Label(root, text="Timetable")
        title_label.pack()

        # Create a frame for the spreadsheet grid
        spreadsheet_frame = tk.Frame(root)
        spreadsheet_frame.pack()

 # Create a list of additional button names
        additional_buttons = [
            "File menu",
            "Demo time",
            "Freeze cell",
            "Find (Ctrl-F)",
            "Find/Replace",
            "Swap time",
            "Remove Cl",
            "Print menu",
            "Global Cou",
            "Multi Freeze",
            "Input Wizard",
            "Time Slot S",
            "Multi Select...",
            "SCHOOL/C",
            "Printer: No",
            "Remove Ga",
            "Clear Freez",
            "Print All Cl",
            "Insert Row",
            "Delete Row",
            "Help",
        ]

        # Create a text widget for each cell in the spreadsheet
        self.cell_text_widgets = []
        for i in range(10):
            for j in range(10):
                cell_text_widget = tk.Text(spreadsheet_frame, height=1, width=10)
                self.cell_text_widgets.append(cell_text_widget)
                cell_text_widget.grid(row=i, column=j)

        # Create a button for each additional button
        self.additional_buttons = []
        for i in range(24):
            additional_button = tk.Button(
                spreadsheet_frame, text="Button " + str(i + 1), command=lambda: print(additional_buttons["text"])
            )
            self.additional_buttons.append(additional_button)
            additional_button.grid(row=7 + i // 7, column=i % 7)


# Create a root window
root = tk.Tk()

# Create a spreadsheet UI instance
spreadsheet_ui = SpreadsheetUI(root)

# Start the mainloop
root.mainloop()

