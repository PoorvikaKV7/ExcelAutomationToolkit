import os
from datetime import datetime
import pandas as pd


def print_line():
    print("=" * 50)


def filter_records():

    input_folder = "input"
    output_folder = "output"

    os.makedirs(output_folder, exist_ok=True)

    excel_files = [f for f in os.listdir(input_folder) if f.endswith(".xlsx")]

    if not excel_files:
        print("\nNo Excel files found in the input folder.")
        return

    print("\n========== Available Excel Files ==========\n")

    for i, file in enumerate(excel_files, start=1):
        print(f"{i}. {file}")

    while True:
        try:
            choice = int(input("\nChoose file number: "))

            if 1 <= choice <= len(excel_files):
                break

            print("Invalid choice. Please try again.")

        except ValueError:
            print("Please enter a valid integer.")

    filename = excel_files[choice - 1]
    filepath = os.path.join(input_folder, filename)

    try:
        df = pd.read_excel(filepath)

    except Exception as e:
        print(f"\nError reading file:\n{e}")
        return

    columns = list(df.columns)

    print("\n========== Available Columns ==========\n")

    for i, col in enumerate(columns, start=1):
        print(f"{i}. {col}")

    while True:

        try:

            col_choice = int(input("\nChoose column number: "))

            if 1 <= col_choice <= len(columns):
                break

            print("Invalid column number.")

        except ValueError:
            print("Please enter a valid integer.")

    selected_column = columns[col_choice - 1]

    # ============================================
    # NUMERIC COLUMN
    # ============================================

    if pd.api.types.is_numeric_dtype(df[selected_column]):

        print("\n========== Numeric Filters ==========")
        print("1. Equal To")
        print("2. Greater Than")
        print("3. Less Than")
        print("4. Greater Than or Equal To")
        print("5. Less Than or Equal To")
        print("6. Between")

        while True:

            try:

                operation = int(input("\nChoose filter: "))

                if 1 <= operation <= 6:
                    break

                print("Invalid choice.")

            except ValueError:
                print("Please enter a valid integer.")

        if operation == 6:

            while True:

                try:
                    low = float(input("Minimum Value : "))
                    high = float(input("Maximum Value : "))

                    if low > high:
                        print("Minimum value cannot be greater than Maximum value.")
                        continue

                    break

                except ValueError:
                    print("Enter valid numeric values.")

            filtered = df[
                (df[selected_column] >= low) &
                (df[selected_column] <= high)
            ]

        else:

            while True:

                try:
                    value = float(input("Enter value : "))
                    break

                except ValueError:
                    print("Enter a valid number.")

            if operation == 1:
                filtered = df[df[selected_column] == value]

            elif operation == 2:
                filtered = df[df[selected_column] > value]

            elif operation == 3:
                filtered = df[df[selected_column] < value]

            elif operation == 4:
                filtered = df[df[selected_column] >= value]

            elif operation == 5:
                filtered = df[df[selected_column] <= value]

    # ============================================
    # TEXT COLUMN
    # ============================================

    else:

        print("\n========== Text Filters ==========")
        print("1. Equals")
        print("2. Contains")
        print("3. Starts With")
        print("4. Ends With")

        while True:

            try:

                operation = int(input("\nChoose filter: "))

                if 1 <= operation <= 4:
                    break

                print("Invalid choice.")

            except ValueError:
                print("Please enter a valid integer.")

        value = input("Enter text: ").strip()

        column = df[selected_column].astype(str)

        if operation == 1:

            filtered = df[
                column.str.lower() == value.lower()
            ]

        elif operation == 2:

            filtered = df[
                column.str.contains(
                    value,
                    case=False,
                    na=False
                )
            ]

        elif operation == 3:

            filtered = df[
                column.str.lower().str.startswith(
                    value.lower()
                )
            ]

        elif operation == 4:

            filtered = df[
                column.str.lower().str.endswith(
                    value.lower()
                )
            ]

    # ============================================
    # NO RECORDS FOUND
    # ============================================

    if filtered.empty:

        print_line()
        print("No matching records found.")
        print("-" * 50)
        print(f"Column Searched : {selected_column}")

        if pd.api.types.is_numeric_dtype(df[selected_column]):

            operation_names = {
                1: "Equal To",
                2: "Greater Than",
                3: "Less Than",
                4: "Greater Than or Equal To",
                5: "Less Than or Equal To",
                6: "Between"
            }

            print(f"Filter Used     : {operation_names[operation]}")

            if operation == 6:
                print(f"Search Value    : {low} to {high}")
            else:
                print(f"Search Value    : {value}")

        else:

            operation_names = {
                1: "Equals",
                2: "Contains",
                3: "Starts With",
                4: "Ends With"
            }

            print(f"Filter Used     : {operation_names[operation]}")
            print(f"Search Value    : {value}")

        print("\nPlease try another value.")
        print_line()

        return

    # ============================================
    # DISPLAY FILTERED DATA
    # ============================================

    print("\n========== Filtered Records ==========\n")

    print(filtered.to_string(index=False))

    # ============================================
    # GENERATE SMART FILE NAME
    # ============================================

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    safe_column = selected_column.replace(" ", "_")

    if pd.api.types.is_numeric_dtype(df[selected_column]):

        operation_codes = {
            1: "EQ",
            2: "GT",
            3: "LT",
            4: "GE",
            5: "LE",
            6: "Between"
        }

    else:

        operation_codes = {
            1: "Equals",
            2: "Contains",
            3: "StartsWith",
            4: "EndsWith"
        }

    op = operation_codes[operation]

    if operation == 6:
        value_text = f"{low}_{high}"
    else:
        value_text = str(value).replace(" ", "_")

    output_file = os.path.join(
        output_folder,
        f"{safe_column}_{op}_{value_text}_{timestamp}.xlsx"
    )

    # ============================================
    # SAVE OPTION
    # ============================================

    while True:

        save = input("\nSave filtered records? (Y/N): ").strip().upper()

        if save in ["Y", "N"]:
            break

        print("Please enter Y or N.")

    if save == "Y":

        try:

            filtered.to_excel(output_file, index=False)

            print()
            print_line()
            print("          FILTER SUMMARY")
            print_line()

            print(f"Source File      : {filename}")
            print(f"Column Filtered  : {selected_column}")

            if operation == 6:
                search_text = f"{low} to {high}"
            else:
                search_text = value

            print(f"Filter Value     : {search_text}")
            print(f"Original Rows    : {len(df)}")
            print(f"Filtered Rows    : {len(filtered)}")
            print(f"Rows Removed     : {len(df) - len(filtered)}")
            print(f"Output File      : {output_file}")

            print_line()
            print("Filter completed successfully!")
            print_line()

        except Exception as e:

            print(f"\nError while saving file:\n{e}")

    else:

        print("\nResults were not saved.")
