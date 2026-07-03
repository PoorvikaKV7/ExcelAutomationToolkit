import os
from datetime import datetime
import pandas as pd

from config import INPUT_FOLDER, OUTPUT_FOLDER
from utils import (
    print_header,
    print_footer,
    success,
    error,
    summary,
    get_integer,
    get_float,
    get_yes_no
)
from logger import log_info, log_error


def filter_records():

    excel_files = [
        file for file in os.listdir(INPUT_FOLDER)
        if file.endswith(".xlsx")
    ]

    if not excel_files:
        error("No Excel files found.")
        log_error("Filter failed: No Excel files found.")
        return

    print_header("Filter Records")

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

        col_choice = get_integer("\nChoose column number: ")

        if 1 <= col_choice <= len(df.columns):
            break

        print("Invalid choice.")

    selected_column = df.columns[col_choice - 1]

    # ==================================================
    # Numeric Filters
    # ==================================================

    if pd.api.types.is_numeric_dtype(df[selected_column]):

        print("\nNumeric Filters")
        print("1. Equal")
        print("2. Greater Than")
        print("3. Less Than")
        print("4. Greater or Equal")
        print("5. Less or Equal")
        print("6. Between")

        while True:

            operation = get_integer("\nChoose filter: ")

            if 1 <= operation <= 6:
                break

            print("Invalid choice.")

        if operation == 6:

            low = get_float("Minimum Value : ")
            high = get_float("Maximum Value : ")

            filtered = df[
                (df[selected_column] >= low) &
                (df[selected_column] <= high)
            ]

            value_text = f"{low}-{high}"
            operation_name = "Between"

        else:

            value = get_float("Enter value : ")

            if operation == 1:
                filtered = df[df[selected_column] == value]
                operation_name = "Equal"

            elif operation == 2:
                filtered = df[df[selected_column] > value]
                operation_name = "Greater Than"

            elif operation == 3:
                filtered = df[df[selected_column] < value]
                operation_name = "Less Than"

            elif operation == 4:
                filtered = df[df[selected_column] >= value]
                operation_name = "Greater or Equal"

            else:
                filtered = df[df[selected_column] <= value]
                operation_name = "Less or Equal"

            value_text = str(value)

    # ==================================================
    # Text Filters
    # ==================================================

    else:

        print("\nText Filters")
        print("1. Equals")
        print("2. Contains")
        print("3. Starts With")
        print("4. Ends With")

        while True:

            operation = get_integer("\nChoose filter: ")

            if 1 <= operation <= 4:
                break

            print("Invalid choice.")

        value = input("Enter text : ").strip()

        column = df[selected_column].astype(str)

        if operation == 1:

            filtered = df[column.str.lower() == value.lower()]
            operation_name = "Equals"

        elif operation == 2:

            filtered = df[column.str.contains(
                value,
                case=False,
                na=False
            )]
            operation_name = "Contains"

        elif operation == 3:

            filtered = df[column.str.lower().str.startswith(value.lower())]
            operation_name = "Starts With"

        else:

            filtered = df[column.str.lower().str.endswith(value.lower())]
            operation_name = "Ends With"

        value_text = value

    # ==================================================
    # No Results
    # ==================================================

    if filtered.empty:

        error("No matching records found.")

        summary("Column", selected_column)
        summary("Filter", operation_name)
        summary("Value", value_text)

        log_info("Filter returned zero records.")

        return

    # ==================================================
    # Display Results
    # ==================================================

    print_header("Filtered Records")

    print(filtered.to_string(index=False))

    print_footer()

    summary("Original Rows", len(df))
    summary("Filtered Rows", len(filtered))
    summary("Column", selected_column)
    summary("Filter", operation_name)
    summary("Value", value_text)

    # ==================================================
    # Save Results
    # ==================================================

    save = get_yes_no("\nSave filtered results? (Y/N): ")

    if save == "Y":

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        output_file = os.path.join(
            OUTPUT_FOLDER,
            f"Filtered_{timestamp}.xlsx"
        )

        filtered.to_excel(output_file, index=False)

        success("Filtered file saved successfully.")

        summary("Output File", output_file)

        log_info(f"Filtered data saved to {output_file}")

    else:

        print("\nResults were not saved.")

        log_info("Filtered results displayed only.")