import csv 

def csv_to_list_of_dictionaries(path_and_file):
    """
    Take in a csv file and return a list of dictionaries
    using column headers as keys

    Args:
        path_and_file (string): path and file name + extension

    Returns:
        list_of_dictionaries (list): csv represented in dictionaries
            with one row having its own dictionary
        None: If CSV is empty or an error occurs
    """

    list_of_dictionaries = []

    with open(path_and_file) as f:
        reader = csv.reader(f, skipinitialspace=True)
        header = next(reader)
        list_of_dictionaries = [dict(zip(header, map(str, row))) for row in reader]

    return list_of_dictionaries

def excel_to_list_of_dictionaries(path_and_file):
    """
    Take in an excel file and return a list of dictionaries
    using column headers as keys

    Args:
        path_and_file (string): path and file name + extension

    Returns:
        list_of_dictionaries (list): excel represented in dictionareis
            with one row having its own dictionary
        None: If excel is empty or an error occurs
    """

    list_of_dictionaries = []

    return list_of_dictionaries
