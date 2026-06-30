import os
import pandas as pd


def remove_duplicates():

    input_file = os.path.join("output", "Merged.xlsx")

    output_file = os.path.join("output", "Merged_NoDuplicates.xlsx")

    if not os.path.exists(input_file):
        print("\nMerged.xlsx not found.")
        print("Please merge the Excel files first.\n")
        return

    df = pd.read_excel(input_file)

    original_rows = len(df)

    df = df.drop_duplicates()

    new_rows = len(df)

    duplicates_removed = original_rows - new_rows

    df.to_excel(output_file, index=False)

    print("\n========== Duplicate Removal Summary ==========")
    print(f"Original Rows      : {original_rows}")
    print(f"Duplicates Removed : {duplicates_removed}")
    print(f"Rows Remaining     : {new_rows}")
    print(f"Output File        : {output_file}")
    print("Duplicate removal completed successfully!\n")