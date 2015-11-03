import csv
import xlrd
from ordereddict import OrderedDict
import simplejson as json

def excel_to_csv(absolute_source_file_path_and_file_name, absolute_destination_file_path_and_file_name):
    """
    Method opens an excel spreadsheet and reads in each sheet.  We take in the user's desired final file name and
    append the sheet name for each converted sheet.  We convert each sheet with data into its own CSV.

    :param absolute_source_file_path_and_file_name:
    :param absolute_destination_file_path_and_file_name:
    :return True if file converted properly:
    :return False if file failed to convert completely:
    """

    workbook = _get_workbook(absolute_source_file_path_and_file_name)
    sheet_names = _get_sheet_names_as_list(workbook)
    absolute_destination_file_path_and_file_name = absolute_destination_file_path_and_file_name.replace('.csv', "")

    try:
        for sheet in sheet_names:
            worksheet = workbook.sheet_by_name(sheet)
            new_file_name = absolute_destination_file_path_and_file_name + sheet + ".csv"
            csv_file = open(new_file_name, 'wb')
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

            for row_number in range(worksheet.nrows):
                writer.writerow(
                    list(x.encode('utf-8') if type(x) == type('') else x for x in worksheet.row_values(row_number))
                )

            csv_file.close()

        return True
    except Exception as e:
        print("Failed to convert file: " + absolute_source_file_path_and_file_name)

        return False

def _get_workbook(source_file_path):
    return xlrd.open_workbook(source_file_path)

def _get_sheet_names_as_list(workbook):
    return workbook.sheet_names()

def csv_to_csv(source_file_path_and_file_name_with_extension, destination_file_path_and_file_name_with_extension):
    """
    Method takes in a CSV file and rewrites as a quoted CSV

    :param source_file_path_and_file_name_with_extension:
    :param destination_file_path_and_file_name_with_extension:
    :return True if file converted properly:
    :return False if file failed to convert completely:
    """

    try:
        try:
            reader = csv.reader(open(source_file_path_and_file_name_with_extension, 'r'))
        except IOError:
            print("Source path or file is incorrect")
            return False

        csv_file = open(destination_file_path_and_file_name_with_extension, 'wb')

        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerows(reader)

        csv_file.close()

        return True
    except Exception as e:
        print("Failed to convert file: " + source_file_path_and_file_name_with_extension)

        return False

def meta_excel_to_json(source_file_path_and_file_name_with_extension, destination_file_path_and_file_name_with_extension):
    """
    Open an excel file that depicts the appropriate template for the meta data file and convert to JSON file with
    destination file path and extension.

    :param source_file_path_and_file_name_with_extension:
    :param destination_file_path_and_file_name_with_extension:
    :return True if file converts properly:
    :return False if file fails to convert:
    """

    try:
        # Open the workbook and select the first worksheet
        wb = xlrd.open_workbook(source_file_path_and_file_name_with_extension)
        sh = wb.sheet_by_index(0)

        # List to hold dictionaries
        meta_list = []

        # Iterate through each row in worksheet and fetch values into dict
        for row in range(1, sh.nrows):
            meta = OrderedDict()
            row_values = sh.row_values(row)
            meta['AIQ Contact Name'] = row_values[0]
            meta['AIQ Contact Email'] = row_values[1]
            meta['Client Name'] = row_values[2]
            meta['Date of Request'] = row_values[3]
            meta['DBs to Match'] = row_values[4]
            meta['Request Type'] = row_values[5]
            meta['Output Fields'] = row_values[6]
            meta['Custom Notes'] = row_values[7]
            meta['Client File Name'] = row_values[8]

            meta_list.append(meta)

        # Serialize the list of dicts to JSON
        j = json.dumps(meta_list)

        # Write to file
        with open(destination_file_path_and_file_name_with_extension, 'w') as f:
            f.write(j)

        return True
    except Exception as e:
        print("Failed to convert file: " + source_file_path_and_file_name_with_extension)

        return False
