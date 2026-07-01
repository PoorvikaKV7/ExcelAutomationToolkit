import os
import pandas as pd


def split_excel():
    input_folder = "input"
    output_folder = "output"

    # Get all Excel files
    excel_files = [f for f in os.listdir(input_folder) if f.endswith(".xlsx")]

    if not excel_files:
        print("No Excel files found in the input folder.")
        return

    # Display available files
    print("\n========== Available Excel Files ==========\n")
    for i, file in enumerate(excel_files, start=1):
        print(f"{i}. {file}")

    # Get valid file choice
    while True:
        try:
            choice = int(input("\nEnter file number: "))

            if 1 <= choice <= len(excel_files):
                break

            print("Please choose a valid file number.\n")

        except ValueError:
            print("Please enter a valid integer.\n")

    filename = excel_files[choice - 1]
    filepath = os.path.join(input_folder, filename)

    # Read Excel file
    df = pd.read_excel(filepath)

    # Get valid rows per file
    while True:
        try:
            rows = int(input("Rows per file: "))

            if rows <= 0:
                print("Rows per file must be greater than 0.\n")
                continue

            break

        except ValueError:
            print("Please enter a valid integer.\n")

    total_rows = len(df)
    file_number = 1

    # Split the file
    for start in range(0, total_rows, rows):
        end = start + rows
        split_df = df.iloc[start:end]

        output_file = os.path.join(
            output_folder,
            f"{os.path.splitext(filename)[0]}_Part{file_number}.xlsx"
        )

        split_df.to_excel(output_file, index=False)

        print(f"Created: {output_file}")

        file_number += 1

    # Summary
    print("\n========== Split Summary ==========")
    print(f"Source File   : {filename}")
    print(f"Total Rows    : {total_rows}")
    print(f"Rows per File : {rows}")
    print(f"Files Created : {file_number - 1}")
    print("Split completed successfully!")