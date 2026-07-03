import os
import pandas as pd

from config import INPUT_FOLDER
from utils import (
    print_header,
    print_footer,
    success,
    error,
    summary,
    get_integer
)
from logger import log_info, log_error


def search_records():

    excel_files = [
        file for file in os.listdir(INPUT_FOLDER)
        if file.endswith(".xlsx")
    ]

    if not excel_files:
        error("No Excel files found.")
        log_error("Search failed: No Excel files found.")
        return

    print_header("Search Records")

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

    print("\nAvailable Columns\n")

    for i, column in enumerate(df.columns, start=1):
        print(f"{i}. {column}")

    while True:

        column_choice = get_integer("\nChoose column number: ")

        if 1 <= column_choice <= len(df.columns):
            break

        print("Invalid choice.")

    selected_column = df.columns[column_choice - 1]

    search_value = input("\nEnter value to search: ").strip()

    result = df[
        df[selected_column]
        .astype(str)
        .str.contains(search_value, case=False, na=False)
    ]

    print_header("Search Results")

    if result.empty:

        error("No matching records found.")

        summary("Column", selected_column)
        summary("Search Value", search_value)
        summary("Records Found", 0)

        log_info(
            f"No records found while searching '{search_value}' "
            f"in column '{selected_column}'."
        )

        return

    print(result.to_string(index=False))

    print_footer()

    summary("Records Found", len(result))

    success("Search completed successfully!")

    log_info(
        f"Search completed in '{selected_column}' "
        f"for '{search_value}'. "
        f"Records Found: {len(result)}"
    )