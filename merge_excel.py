import os
import glob
import pandas as pd

from config import INPUT_FOLDER, OUTPUT_FOLDER
from utils import print_header, print_footer, success, error, summary
from logger import log_info, log_error


def merge_excel_files():
    """
    Merge all Excel files from the input folder into a single Excel file.
    """

    excel_files = glob.glob(os.path.join(INPUT_FOLDER, "*.xlsx"))

    if not excel_files:
        error("No Excel files found in the input folder.")
        log_error("Merge failed: No Excel files found.")
        return

    dataframes = []

    print_header("Merging Excel Files")

    for file in excel_files:

        try:
            filename = os.path.basename(file)

            print(f"Reading : {filename}")

            df = pd.read_excel(file)

            dataframes.append(df)

            log_info(f"Successfully read {filename}")

        except Exception as e:

            filename = os.path.basename(file)

            error(f"Unable to read {filename}")

            print(e)

            log_error(f"{filename} : {e}")

    if not dataframes:
        error("No valid Excel files available for merging.")
        log_error("Merge failed: No valid Excel files.")
        return

    merged_df = pd.concat(dataframes, ignore_index=True)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        "Merged.xlsx"
    )

    try:

        merged_df.to_excel(output_file, index=False)

        print_header("Merge Summary")

        summary("Files Merged", len(dataframes))
        summary("Rows Saved", len(merged_df))
        summary("Output File", output_file)

        print_footer()

        success("Merge completed successfully!")

        log_info(
            f"Merged {len(dataframes)} files into {output_file}"
        )

    except Exception as e:

        error("Unable to save merged file.")

        print(e)

        log_error(f"Error saving merged file : {e}")