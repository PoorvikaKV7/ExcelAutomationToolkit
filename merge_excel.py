import os
import glob
import pandas as pd


def merge_excel_files():

    input_folder = "input"
    output_folder = "output"

    os.makedirs(output_folder, exist_ok=True)

    excel_files = glob.glob(os.path.join(input_folder, "*.xlsx"))

    if not excel_files:
        print("\nNo Excel files found in the input folder.\n")
        return

    dataframes = []

    for file in excel_files:
        try:
            print(f"Reading: {os.path.basename(file)}")
            df = pd.read_excel(file)
            dataframes.append(df)

        except Exception as e:
            print(f"Error reading {os.path.basename(file)}")
            print(e)

    if not dataframes:
        print("\nNo valid Excel files found.\n")
        return

    merged_df = pd.concat(dataframes, ignore_index=True)

    # Remove duplicate rows

    output_file = os.path.join(output_folder, "Merged.xlsx")

    merged_df.to_excel(output_file, index=False)

    print("\n========== Merge Summary ==========")
    print(f"Files Merged : {len(dataframes)}")
    print(f"Rows Saved   : {len(merged_df)}")
    print(f"Output File  : {output_file}")
    print("Merge Completed Successfully!\n")