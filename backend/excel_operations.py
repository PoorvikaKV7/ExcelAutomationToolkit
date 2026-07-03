import os
import pandas as pd


def merge_excel_files(file_paths, output_path):
    """
    Merge multiple Excel files into one.

    Parameters:
        file_paths (list): List of Excel file paths.
        output_path (str): Output Excel file path.

    Returns:
        tuple(bool, str)
    """

    try:

        if not file_paths:
            return False, "No files selected."

        merged_data = []

        for file in file_paths:

            if not os.path.exists(file):
                return False, f"File not found:\n{file}"

            df = pd.read_excel(file)

            merged_data.append(df)

        merged_df = pd.concat(
            merged_data,
            ignore_index=True
        )

        merged_df.to_excel(
            output_path,
            index=False
        )

        return True, f"Merged {len(file_paths)} file(s) successfully."

    except Exception as e:

        return False, str(e)