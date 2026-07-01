import os
import pandas as pd


def search_records():
    input_folder = "input"
    output_folder = "output"

    # Get all Excel files
    excel_files = [f for f in os.listdir(input_folder) if f.endswith(".xlsx")]

    if not excel_files:
        print("No Excel files found.")
        return

    # Display files
    print("\n========== Available Excel Files ==========\n")

    for i, file in enumerate(excel_files, start=1):
        print(f"{i}. {file}")

    # Select file
    while True:
        try:
            choice = int(input("\nEnter file number: "))

            if 1 <= choice <= len(excel_files):
                break

            print("Invalid choice.")

        except ValueError:
            print("Please enter a valid integer.")

    filename = excel_files[choice - 1]
    filepath = os.path.join(input_folder, filename)

    try:
        df = pd.read_excel(filepath)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Display columns
    print("\n========== Available Columns ==========\n")

    columns = list(df.columns)

    for i, column in enumerate(columns, start=1):
        print(f"{i}. {column}")

    # Select column
    while True:
        try:
            col_choice = int(input("\nChoose column number: "))

            if 1 <= col_choice <= len(columns):
                break

            print("Invalid column number.")

        except ValueError:
            print("Please enter a valid integer.")

    selected_column = columns[col_choice - 1]

    search_value = input(f"\nEnter value to search in '{selected_column}': ").strip()

    # Search
    if pd.api.types.is_numeric_dtype(df[selected_column]):
        try:
            search_value = float(search_value)
            results = df[df[selected_column] == search_value]
        except ValueError:
            print("Please enter a valid numeric value.")
            return
    else:
        results = df[
            df[selected_column]
            .astype(str)
            .str.contains(search_value, case=False, na=False)
        ]

    # No records found
    if results.empty:
        print("\nNo matching records found.")
        return

    # Display results
    print("\n========== Search Results ==========\n")
    print(results.to_string(index=False))

    print("\n===================================")
    print(f"Records Found : {len(results)}")
    print("===================================")

    # Save results
    save = input("\nDo you want to save the results? (Y/N): ").strip().upper()

    if save == "Y":

        output_file = os.path.join(
            output_folder,
            f"Search_Results_{os.path.splitext(filename)[0]}.xlsx"
        )

        results.to_excel(output_file, index=False)

        print("\nSearch results saved successfully!")
        print(f"Saved to: {output_file}")

    else:
        print("\nSearch results were not saved.")