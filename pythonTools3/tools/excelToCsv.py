import xlrd
import csv
import sys

def _get_workbook(source_path_and_name):
    return xlrd.open_workbook(source_path_and_name)

def _get_sheet_names_as_list(workbook):
    return workbook.sheet_names()

def excel_to_csv(source_path_and_name, destination_path_and_name = ""):
    """
    Convert all sheets in excel file to csv

    Args:

    Returns:
        bool: True if converted successfully, False if there is an error
    """

    workbook = _get_workbook(source_path_and_name)
    sheet_names = _get_sheet_names_as_list(workbook)

    if destination_path_and_name == "":
        destination_path_and_name = source_path_and_name[:source_path_and_name.find('.')] + '.csv'

    for sheet in sheet_names:
        worksheet = workbook.sheet_by_name(sheet)
        csv_file = open(destination_path_and_name.replace('.csv','') + str(sheet) + '.csv', 'wb')
        writer = csv.writer(csv_file, quoting = csv.QUOTE_ALL)

        for row_number in range(worksheet.nrows):
            writer.writerow(
                    list(x.encode('utf-8') if type(x) == type('') else
                        x for x in worksheet.row_values(row_number))
                    )

        csv_file.close()

def main():
    args = sys.argv
    
    if len(args) == 3:
        try:
            excel_to_csv(args[1], args[2])
            return True
        except Exception as e:
            print("Failed to convert %s" % args[1])
    elif len(args) == 2:
        try:
            excel_to_csv(args[1])
            return True
        except Exception as e:
            print("Failed to convert %s" % args[1])
        excel_to_csv(args[1])
    elif len(args) > 3:
        print("Please provide 1 or 2 arguments only")
    else:
        print("No arguments provided!")

if __name__ == '__main__':
    main()
