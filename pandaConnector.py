import pandas
from convertToDictionaries import *

def csv_to_data_frame(path_and_file_name):
    """
    Take in a path and file name for a csv file
    and returns a pandas dataframe

    Args:
        path_and_file_name (string): absolute path for 
            file to be converted to a pandas dataframe

    Returns:
        dataframe (pandas Dataframe): A dataframe created
            based on a list of dictionaries
        None: if there is an error or the file is empty
    """

    list_of_dictionaries = csv_to_list_of_dictionaries(path_and_file_name)
    dataframe = pandas.DataFrame(list_of_dictionaries)

    if dataframe is None:
        return None

    return dataframe
