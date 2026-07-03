import os
import pandas as pd

from config import INPUT_FOLDER, OUTPUT_FOLDER
from utils import (
    print_header,
    print_footer,
    success,
    error,
    summary,
    get_integer
)
from logger import log_info, log_error


def excel_statistics():

    excel_files = [
        file for file in os.listdir(INPUT_FOLDER)
        if file.endswith(".xlsx")
    ]

    if not excel_files:
        error("No Excel files found.")
        log_error("Statistics failed: No Excel files found.")
        return

    print_header("Excel Statistics")

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

        error("Unable to read Excel file.")
        print(e)

        log_error(str(e))
        return

    print_header("Statistics Report")

    summary("File Name", filename)
    summary("Total Rows", len(df))
    summary("Total Columns", len(df.columns))
    summary("Duplicate Rows", df.duplicated().sum())
    summary("Missing Values", df.isnull().sum().sum())

    print("\nColumns")
    print("-" * 40)

    for column in df.columns:
        print(column)

    print("\nData Types")
    print("-" * 40)

    for column in df.columns:
        print(f"{column:<20}{df[column].dtype}")

    print("\nMissing Values Per Column")
    print("-" * 40)

    for column in df.columns:
        print(f"{column:<20}{df[column].isnull().sum()}")

    numeric_columns = df.select_dtypes(include="number")

    if not numeric_columns.empty:

        print("\nNumeric Statistics")
        print("-" * 40)

        for column in numeric_columns.columns:

            print(f"\n{column}")
            print("-" * 20)
            print(f"Minimum : {numeric_columns[column].min()}")
            print(f"Maximum : {numeric_columns[column].max()}")
            print(f"Average : {numeric_columns[column].mean():.2f}")
            print(f"Median  : {numeric_columns[column].median():.2f}")
            print(f"Sum     : {numeric_columns[column].sum()}")
            print(f"Unique  : {numeric_columns[column].nunique()}")

    report_file = os.path.join(
        OUTPUT_FOLDER,
        f"{os.path.splitext(filename)[0]}_Statistics.txt"
    )

    try:

        with open(report_file, "w") as report:

            report.write("Excel Statistics Report\n")
            report.write("=" * 40 + "\n\n")

            report.write(f"File Name : {filename}\n")
            report.write(f"Rows      : {len(df)}\n")
            report.write(f"Columns   : {len(df.columns)}\n")
            report.write(f"Duplicates: {df.duplicated().sum()}\n")
            report.write(f"Missing   : {df.isnull().sum().sum()}\n\n")

            report.write("Columns\n")
            report.write("-" * 30 + "\n")

            for column in df.columns:
                report.write(f"{column}\n")

            report.write("\nData Types\n")
            report.write("-" * 30 + "\n")

            for column in df.columns:
                report.write(f"{column:<20}{df[column].dtype}\n")

            if not numeric_columns.empty:

                report.write("\nNumeric Statistics\n")
                report.write("-" * 30 + "\n")

                for column in numeric_columns.columns:

                    report.write(f"\n{column}\n")
                    report.write(f"Minimum : {numeric_columns[column].min()}\n")
                    report.write(f"Maximum : {numeric_columns[column].max()}\n")
                    report.write(f"Average : {numeric_columns[column].mean():.2f}\n")
                    report.write(f"Median  : {numeric_columns[column].median():.2f}\n")
                    report.write(f"Sum     : {numeric_columns[column].sum()}\n")
                    report.write(f"Unique  : {numeric_columns[column].nunique()}\n")

        print_footer()

        success("Statistics generated successfully!")

        summary("Report Saved", report_file)

        log_info(f"Statistics generated for {filename}")

    except Exception as e:

        error("Unable to save report.")

        print(e)

        log_error(str(e))