import os
import glob
import pandas as pd


def csv_to_excel():

    input_folder = "input"
    output_folder = "output"

    os.makedirs(output_folder, exist_ok=True)

    csv_files = glob.glob(os.path.join(input_folder, "*.csv"))

    if not csv_files:
        print("\nNo CSV files found.\n")
        return

    for file in csv_files:

        try:
            df = pd.read_csv(file)

            filename = os.path.splitext(os.path.basename(file))[0]

            output_file = os.path.join(output_folder, filename + ".xlsx")

            df.to_excel(output_file, index=False)

            print(f"Converted: {filename}.csv → {filename}.xlsx")

        except Exception as e:
            print(f"Error converting {file}")
            print(e)

    print("\nCSV to Excel conversion completed.\n")