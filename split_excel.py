import os
import pandas as pd

from config import INPUT_FOLDER, OUTPUT_FOLDER
from utils import (
    print_header,
    print_footer,
    success,
    error,
    summary,
    get_integer,
)
from logger import log_info, log_error


def split_excel():
    """
    Split an Excel file into multiple smaller Excel files.
    """

    excel_files = [
        file for file in os.listdir(INPUT_FOLDER)
        if file.endswith(".xlsx")
    ]

    if not excel_files:
        error("No Excel files found in the input folder.")
        log_error("Split failed: No Excel files found.")
        return

    print_header("Split Excel File")

    print("\nAvailable Excel Files\n")

    for i, file in enumerate(excel_files, start=1):
        print(f"{i}. {file}")

    while True:

        choice = get_integer("\nChoose file number: ")

        if 1 <= choice <= len(excel_files):
            break

        print("Invalid choice.")

    filename = excel_files[choice - 1]

    filepath = os.path.join(INPUT_FOLDER, filename)

    try:

        df = pd.read_excel(filepath)

    except Exception as e:

        error("Unable to open Excel file.")
        print(e)

        log_error(str(e))
        return

    total_rows = len(df)

    print(f"\nTotal Rows : {total_rows}")

    while True:

        rows_per_file = get_integer("Rows per file: ")

        if rows_per_file <= 0:
            print("Rows must be greater than 0.")
            continue

        if rows_per_file > total_rows:
            print("Rows per file cannot exceed total rows.")
            continue

        break

    file_count = 0

    for start in range(0, total_rows, rows_per_file):

        end = min(start + rows_per_file, total_rows)

        split_df = df.iloc[start:end]

        output_filename = (
            f"{os.path.splitext(filename)[0]}"
            f"_Part{file_count + 1}"
            f"_Rows{start + 1}-{end}.xlsx"
        )

        output_path = os.path.join(
            OUTPUT_FOLDER,
            output_filename
        )

        split_df.to_excel(
            output_path,
            index=False
        )

        print(f"Created : {output_filename}")

        log_info(f"Created {output_filename}")

        file_count += 1

    print_header("Split Summary")

    summary("Source File", filename)
    summary("Total Rows", total_rows)
    summary("Rows Per File", rows_per_file)
    summary("Files Created", file_count)
    summary("Output Folder", OUTPUT_FOLDER)

    print_footer()

    success("Excel file split successfully!")

    log_info(f"Split completed for {filename}")