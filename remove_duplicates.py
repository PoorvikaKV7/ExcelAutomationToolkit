import os
import pandas as pd

from config import OUTPUT_FOLDER
from utils import print_header, print_footer, success, error, summary
from logger import log_info, log_error


def remove_duplicates():
    """
    Remove duplicate rows from the merged Excel file.
    """

    input_file = os.path.join(
        OUTPUT_FOLDER,
        "Merged.xlsx"
    )

    output_file = os.path.join(
        OUTPUT_FOLDER,
        "Merged_NoDuplicates.xlsx"
    )

    if not os.path.exists(input_file):

        error("Merged.xlsx not found.")
        print("Please merge the Excel files first.")

        log_error("Duplicate removal failed: Merged.xlsx not found.")

        return

    try:

        df = pd.read_excel(input_file)

        original_rows = len(df)

        cleaned_df = df.drop_duplicates()

        new_rows = len(cleaned_df)

        duplicates_removed = original_rows - new_rows

        cleaned_df.to_excel(output_file, index=False)

        print_header("Duplicate Removal Summary")

        summary("Original Rows", original_rows)
        summary("Duplicates Removed", duplicates_removed)
        summary("Rows Remaining", new_rows)
        summary("Output File", output_file)

        print_footer()

        success("Duplicate removal completed successfully!")

        log_info(
            f"Removed {duplicates_removed} duplicate rows."
        )

    except Exception as e:

        error("Failed to remove duplicate rows.")

        print(e)

        log_error(f"Duplicate removal error: {e}")