import csv
import sys

def csv_to_csv(source_path_and_name, destination_path = ''):
    """
    Takes in a csv file and rewrites as a quoted csv

    Args:
        source_path_and_name (string): csv file path and name
        destination path (string): [optional] directory where
            converted files should be sent

    Returns:
        bool: True if converted successfully, False if not
    """

    try:
        try:
            reader = csv.reader(open(source_path_and_name, 'r'))
        except IOError:
            print "Source path or file is incorrect"
            return False

        if destination_path == '':
            destination_path = source_path_and_name.lower().replace('.csv', '_modified.csv')
        else:
            destination_path = destination_path + source_path_and_name[source_path_and_name.rfind('/')+1:]


        csv_file = open(destination_path, 'wb')

        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerows(reader)

        csv_file.close()

        return True
    except Exception as e:
        return False

def main():
    args = sys.argv

    if len(args) == 3:
        if csv_to_csv(args[1], args[2]):
            print "File converted successfully"
        else:
            print "File did not convert"
    elif len(args) == 2:
        if csv_to_csv(args[1]):
            print "File converted successfully"
        else:
            print "File did not convert"
    elif len(args) > 3:
        print "Please provide only 1 or 2 arguments"
    else:
        print "No arguments provided!"

if __name__ == '__main__':
    main()
