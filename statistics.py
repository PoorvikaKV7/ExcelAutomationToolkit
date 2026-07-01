import os
import pandas as pd


def excel_statistics():
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
    try:
        df = pd.read_excel(filepath)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Basic Statistics
    total_rows = len(df)
    total_columns = len(df.columns)
    duplicate_rows = df.duplicated().sum()
    missing_values = df.isnull().sum().sum()

    # Missing values per column
    missing_per_column = df.isnull().sum()

    # Numeric columns
    numeric_columns = df.select_dtypes(include="number")

    # ---------------- Display Report ---------------- #

    print("\n========== Excel Statistics ==========\n")

    print(f"File Name       : {filename}")
    print(f"Total Rows      : {total_rows}")
    print(f"Total Columns   : {total_columns}")
    print(f"Duplicate Rows  : {duplicate_rows}")
    print(f"Missing Values  : {missing_values}")

    print("\nColumns")
    print("--------------------------------------")

    for column in df.columns:
        print(column)

    print("\nData Types")
    print("--------------------------------------")

    for column, dtype in df.dtypes.items():
        print(f"{column:<20} {dtype}")

    print("\nMissing Values Per Column")
    print("--------------------------------------")

    for column, count in missing_per_column.items():
        print(f"{column:<20} {count}")

    print("\nNumeric Statistics")
    print("--------------------------------------")

    if numeric_columns.empty:
        print("No numeric columns found.")

    else:
        for column in numeric_columns.columns:
            print(f"\n{column}")
            print("-" * 30)
            print(f"Minimum : {numeric_columns[column].min()}")
            print(f"Maximum : {numeric_columns[column].max()}")
            print(f"Average : {numeric_columns[column].mean():.2f}")
            print(f"Median  : {numeric_columns[column].median():.2f}")

    # ---------------- Save Report ---------------- #

    report_file = os.path.join(
        output_folder,
        f"{os.path.splitext(filename)[0]}_Statistics.txt"
    )

    with open(report_file, "w") as file:

        file.write("========== Excel Statistics ==========\n\n")

        file.write(f"File Name       : {filename}\n")
        file.write(f"Total Rows      : {total_rows}\n")
        file.write(f"Total Columns   : {total_columns}\n")
        file.write(f"Duplicate Rows  : {duplicate_rows}\n")
        file.write(f"Missing Values  : {missing_values}\n\n")

        file.write("Columns\n")
        file.write("--------------------------------------\n")

        for column in df.columns:
            file.write(f"{column}\n")

        file.write("\nData Types\n")
        file.write("--------------------------------------\n")

        for column, dtype in df.dtypes.items():
            file.write(f"{column:<20} {dtype}\n")

        file.write("\nMissing Values Per Column\n")
        file.write("--------------------------------------\n")

        for column, count in missing_per_column.items():
            file.write(f"{column:<20} {count}\n")

        file.write("\nNumeric Statistics\n")
        file.write("--------------------------------------\n")

        if numeric_columns.empty:
            file.write("No numeric columns found.\n")

        else:
            for column in numeric_columns.columns:
                file.write(f"\n{column}\n")
                file.write(f"Minimum : {numeric_columns[column].min()}\n")
                file.write(f"Maximum : {numeric_columns[column].max()}\n")
                file.write(f"Average : {numeric_columns[column].mean():.2f}\n")
                file.write(f"Median  : {numeric_columns[column].median():.2f}\n")

    # ---------------- Success Message ---------------- #

    print("\n======================================")
    print("Statistics generated successfully!")
    print(f"Report saved to: {report_file}")
    print("======================================")