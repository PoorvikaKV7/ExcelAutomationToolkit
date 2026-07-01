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


def csv_to_excel():
    """
    Convert CSV file(s) from input folder to Excel format.
    """

    csv_files = [
        file for file in os.listdir(INPUT_FOLDER)
        if file.endswith(".csv")
    ]

    if not csv_files:

        error("No CSV files found in the input folder.")
        log_error("CSV to Excel failed: No CSV files found.")
        return

    print_header("CSV to Excel Converter")

    print("\nAvailable CSV Files\n")

    for i, file in enumerate(csv_files, start=1):
        print(f"{i}. {file}")

    print("0. All Files")

    while True:

        try:

            choice = int(input("\nChoose file: "))

            if 0 <= choice <= len(csv_files):
                break

            print("Invalid choice.")

        except ValueError:

            print("Please enter a valid integer.")

    converted = 0

    if choice == 0:

        selected_files = csv_files

    else:

        selected_files = [csv_files[choice - 1]]

    for filename in selected_files:

        input_path = os.path.join(
            INPUT_FOLDER,
            filename
        )

        output_path = os.path.join(
            OUTPUT_FOLDER,
            filename.replace(".csv", ".xlsx")
        )

        try:

            df = pd.read_csv(input_path)

            df.to_excel(output_path, index=False)

            print(f"\nConverted : {filename} → {os.path.basename(output_path)}")

            log_info(f"Converted {filename} to Excel")

            converted += 1

        except Exception as e:

            error(f"Failed to convert {filename}")

            print(e)

            log_error(f"{filename}: {e}")

    print_header("Conversion Summary")

    summary("CSV Files Found", len(csv_files))
    summary("Files Converted", converted)
    summary("Output Folder", OUTPUT_FOLDER)

    print_footer()

    success("CSV to Excel conversion completed successfully!")