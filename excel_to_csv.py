import os
import pandas as pd

from config import INPUT_FOLDER, OUTPUT_FOLDER
from utils import (
    print_header,
    print_footer,
    success,
    error,
    summary
)
from logger import log_info, log_error


def excel_to_csv():
    """
    Convert Excel file(s) from input folder to CSV format.
    """

    excel_files = [
        file for file in os.listdir(INPUT_FOLDER)
        if file.endswith(".xlsx")
    ]

    if not excel_files:

        error("No Excel files found in the input folder.")
        log_error("Excel to CSV failed: No Excel files found.")
        return

    print_header("Excel to CSV Converter")

    print("\nAvailable Excel Files\n")

    for i, file in enumerate(excel_files, start=1):
        print(f"{i}. {file}")

    print("0. All Files")

    while True:

        try:

            choice = int(input("\nChoose file: "))

            if 0 <= choice <= len(excel_files):
                break

            print("Invalid choice.")

        except ValueError:

            print("Please enter a valid integer.")

    if choice == 0:
        selected_files = excel_files
    else:
        selected_files = [excel_files[choice - 1]]

    converted = 0

    for filename in selected_files:

        input_path = os.path.join(INPUT_FOLDER, filename)

        output_path = os.path.join(
            OUTPUT_FOLDER,
            filename.replace(".xlsx", ".csv")
        )

        try:

            df = pd.read_excel(input_path)

            df.to_csv(output_path, index=False)

            print(f"\nConverted : {filename} → {os.path.basename(output_path)}")

            converted += 1

            log_info(f"Converted {filename} to CSV")

        except Exception as e:

            error(f"Failed to convert {filename}")

            print(e)

            log_error(f"{filename}: {e}")

    print_header("Conversion Summary")

    summary("Excel Files Found", len(excel_files))
    summary("Files Converted", converted)
    summary("Output Folder", OUTPUT_FOLDER)

    print_footer()

    success("Excel to CSV conversion completed successfully!")