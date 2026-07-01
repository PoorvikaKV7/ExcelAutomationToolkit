import os

# ==========================================
# Header
# ==========================================

def print_header(title):

    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


# ==========================================
# Footer
# ==========================================

def print_footer():

    print("=" * 50)


# ==========================================
# Integer Input
# ==========================================

def get_integer(prompt):

    while True:

        try:
            return int(input(prompt))

        except ValueError:
            print("Please enter a valid integer.")


# ==========================================
# Float Input
# ==========================================

def get_float(prompt):

    while True:

        try:
            return float(input(prompt))

        except ValueError:
            print("Please enter a valid number.")


# ==========================================
# Yes / No
# ==========================================

def get_yes_no(prompt):

    while True:

        choice = input(prompt).strip().upper()

        if choice in ("Y", "N"):
            return choice

        print("Please enter Y or N.")


# ==========================================
# Display Excel Files
# ==========================================

def list_excel_files(folder):

    excel_files = [
        file for file in os.listdir(folder)
        if file.endswith(".xlsx")
    ]

    if not excel_files:
        return []

    print()

    for i, file in enumerate(excel_files, start=1):
        print(f"{i}. {file}")

    return excel_files


# ==========================================
# Choose Excel File
# ==========================================

def choose_excel_file(folder):

    excel_files = list_excel_files(folder)

    if not excel_files:
        print("No Excel files found.")
        return None

    while True:

        choice = get_integer("\nChoose file number: ")

        if 1 <= choice <= len(excel_files):
            return excel_files[choice - 1]

        print("Invalid choice.")


# ==========================================
# Success Message
# ==========================================

def success(message):

    print("\n✅ " + message)


# ==========================================
# Error Message
# ==========================================

def error(message):

    print("\n❌ " + message)


# ==========================================
# Summary Line
# ==========================================

def summary(label, value):

    print(f"{label:<20}: {value}")