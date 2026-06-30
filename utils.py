import os
import glob


INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"


def create_output_folder():
    """Create the output folder if it doesn't exist."""
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def get_excel_files():
    return sorted(glob.glob(os.path.join(INPUT_FOLDER, "*.xlsx")))


def get_csv_files():
    return sorted(glob.glob(os.path.join(INPUT_FOLDER, "*.csv")))


def display_file_menu(files, file_type):
    """
    Display available files and let the user choose one
    or all files.
    """

    if not files:
        print(f"\nNo {file_type} files found.\n")
        return None

    print(f"\nAvailable {file_type} Files")
    print("-" * 35)

    for index, file in enumerate(files, start=1):
        print(f"{index}. {os.path.basename(file)}")

    print("0. All Files")

    while True:

        choice = input("\nEnter your choice: ")

        if choice == "0":
            return files

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(files):
                return [files[choice - 1]]

        print("Invalid choice. Try again.")