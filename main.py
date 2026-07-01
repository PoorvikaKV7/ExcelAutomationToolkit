from merge_excel import merge_excel_files
from remove_duplicates import remove_duplicates
from csv_to_excel import csv_to_excel
from excel_to_csv import excel_to_csv
from split_excel import split_excel
from statistics import excel_statistics

def display_menu():

    while True:

        print("=" * 45)
        print("        Excel Automation Toolkit")
        print("=" * 45)

        print("1. Merge Excel Files")
        print("2. Remove Duplicate Rows")
        print("3. CSV to Excel")
        print("4. Excel to CSV")
        print("5. Split Excel File")
        print("6. Excel Statistics")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            merge_excel_files()

        elif choice == "2":
            remove_duplicates()

        elif choice == "3":
            csv_to_excel()

        elif choice == "4":
            excel_to_csv()

        elif choice == "5":
            split_excel()

        elif choice == "6":
            excel_statistics()

        elif choice == "7":
            print("\nThank you for using Excel Automation Toolkit.")
            print("Goodbye!\n")
            break

        else:
            print("\nInvalid Choice! Please try again.\n")


if __name__ == "__main__":
    display_menu()