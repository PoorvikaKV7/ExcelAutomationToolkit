import os
import pandas as pd

from utils import (
    create_output_folder,
    get_excel_files,
    display_file_menu,
    OUTPUT_FOLDER
)


def excel_to_csv():

    create_output_folder()

    excel_files = get_excel_files()

    selected_files = display_file_menu(excel_files, "Excel")

    if selected_files is None:
        return

    print("\nStarting conversion...\n")

    converted = 0

    for file in selected_files:

        try:

            filename = os.path.splitext(os.path.basename(file))[0]

            print(f"Converting: {filename}.xlsx")

            df = pd.read_excel(file)

            output_file = os.path.join(OUTPUT_FOLDER, filename + ".csv")

            df.to_csv(output_file, index=False)

            print("✓ Done\n")

            converted += 1

        except Exception as e:

            print(f"✗ Error converting {filename}.xlsx")
            print(e)

    print("=" * 40)
    print("Conversion Summary")
    print("=" * 40)
    print(f"Files Converted : {converted}")
    print(f"Output Folder   : {OUTPUT_FOLDER}")
    print("=" * 40)