import customtkinter as ctk
from tkinter import messagebox

# ============================
# Import Backend Modules
# ============================

from tkinter import filedialog, messagebox
from backend.excel_operations import merge_excel_files
from remove_duplicates import remove_duplicates
from csv_to_excel import csv_to_excel
from excel_to_csv import excel_to_csv
from split_excel import split_excel
from statistics import excel_statistics
from search_records import search_records
from filter_records import filter_records
from format_excel import format_excel

# ============================
# Theme
# ============================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# ============================
# Main Window
# ============================

app = ctk.CTk()

app.title("Excel Automation Toolkit")

app.geometry("1000x650")

app.resizable(False, False)


# ============================
# Header
# ============================

title = ctk.CTkLabel(
    app,
    text="📊 Excel Automation Toolkit",
    font=("Arial", 28, "bold")
)

title.pack(pady=20)


subtitle = ctk.CTkLabel(
    app,
    text="Professional Excel Automation using Python",
    font=("Arial", 15)
)

subtitle.pack()


# ============================
# Main Frame
# ============================

main_frame = ctk.CTkFrame(app)

main_frame.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)


# ============================
# Left Menu
# ============================

left_frame = ctk.CTkFrame(
    main_frame,
    width=250
)

left_frame.pack(
    side="left",
    fill="y",
    padx=15,
    pady=15
)


# ============================
# Right Frame
# ============================

right_frame = ctk.CTkFrame(main_frame)

right_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=15,
    pady=15
)


# ============================
# Status Label
# ============================

status = ctk.CTkLabel(
    right_frame,
    text="Ready",
    font=("Arial", 18)
)

status.pack(pady=20)


# ============================
# Function Wrapper
# ============================

def run_function(function, name):

    try:

        status.configure(text=f"Running {name}...")

        app.update()

        function()

        status.configure(
            text=f"✅ {name} Completed Successfully"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

        status.configure(text="❌ Error")

def merge_excel_gui():

    files = filedialog.askopenfilenames(
        title="Select Excel Files",
        filetypes=[("Excel Files", "*.xlsx *.xls")]
    )

    if not files:
        return

    output_file = filedialog.asksaveasfilename(
        title="Save Merged File",
        defaultextension=".xlsx",
        filetypes=[("Excel File", "*.xlsx")],
        initialfile="Merged.xlsx"
    )

    if not output_file:
        return

    success, message = merge_excel_files(
        list(files),
        output_file
    )

    if success:
        messagebox.showinfo(
            "Success",
            message
        )
    else:
        messagebox.showerror(
            "Error",
            message
        )


# ============================
# Buttons
# ============================

buttons = [

    ("Merge Excel Files", merge_excel_gui),

    ("Remove Duplicates", remove_duplicates),

    ("CSV ➜ Excel", csv_to_excel),

    ("Excel ➜ CSV", excel_to_csv),

    ("Split Excel File", split_excel),

    ("Excel Statistics", excel_statistics),

    ("Search Records", search_records),

    ("Filter Records", filter_records),

    ("Format Excel", format_excel)

]

for text, func in buttons:

    button = ctk.CTkButton(

        left_frame,

        text=text,

        width=220,

        height=40,

        command=lambda f=func, n=text:
        run_function(f, n)

    )

    button.pack(pady=8)


# ============================
# Exit Button
# ============================

exit_button = ctk.CTkButton(

    left_frame,

    text="Exit",

    fg_color="red",

    hover_color="#8B0000",

    command=app.destroy

)

exit_button.pack(
    side="bottom",
    pady=20
)


# ============================
# Footer
# ============================

footer = ctk.CTkLabel(

    app,

    text="Version 2.0 | Developed by Poorvika K V",

    font=("Arial", 12)

)

footer.pack(pady=10)


# ============================
# Start
# ============================

app.mainloop()