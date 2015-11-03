from boto.s3.connection import S3Connection
import re
import os
import time


class BucketManager:
    def __init__(self, bucket_name, aws_key, aws_secret):
        """
        Method initializes the connection with AWS S3 and gets instance of bucket into class variable named 'bucket'

        :param bucket_name:
        :param aws_key:
        :param aws_secret:
        :return:
        """

        aws_connection = S3Connection(aws_key, aws_secret)
        self.bucket = aws_connection.get_bucket(bucket_name)

    def download_object_by_key_name(self, key_string, path_and_filename_to_download_to):
        """
        Method downloads specific file by key name to location on host machine

        :param key:
        :param path_and_filename_to_download_to:
        :return True if download was successful:
        :return False if download failed:
        """

        try:
            key = self.bucket.get_key(key_string)
            key.get_contents_to_filename(path_and_filename_to_download_to)
        except Exception as e:
            print "Failed to download file / folder with name: " + str(key_string)
            print e

    def upload_file_to_bucket(self, key, path_to_upload_from):
        """
        Method uploads file from host machine to location on AWS with specified key name.  To place file into a folder
        write key as 'Folder/newkey'

        :param key:
        :param path_to_upload_from:
        :return True if upload was successful:
        :return False if upload failed:
        """

        try:
            key = self.bucket.new_key(key)
            key.set_contents_from_filename(path_to_upload_from)
        except Exception as e:
            print "Failed to upload file / folder with name: " + key
            print e

    def delete_object_by_key_name(self, key):
        """
        Method deletes file / folder with specified key

        :param key:
        :return True if deletion is successful:
        :return False if deletion failed:
        """

        try:
            self.bucket.delete_key(key)
        except Exception as e:
            print "Failed to delete file / folder with name : " + key
            print e

    def print_list_of_keys(self):
        """
        Method gets all keys in folder and prints them vertically

        :param:
        :return:
        """

        key_list = self.bucket.get_all_keys()
        for key in key_list:
            print key.name

    def get_all_keys(self):
        """
        Method returns a list of all keys in bucket; Files in folder have key format like: "Folder/file.txt"

        :param:
        :return list of all keys in bucket
        """

        return list(self.bucket.get_all_keys())

    def get_all_keys_in_folder(self, folder):
        """
        Method returns a list of all keys in a folder

        :param folder:
        :return list of keys in a folder:
        """

        list_of_files_in_folder = []
        for key in list(self.bucket.list(folder)):
            parsed_key = ''.join(key.name).split('/')[-1]
            if len(parsed_key) > 0:
                list_of_files_in_folder.append(parsed_key)

        return list_of_files_in_folder

    def get_csv_by_key(self, key):
        """
        Method returns a list of strings from a CSV file

        :param key:
        :return list of strings:
        """

        instance = self.bucket.get_key(key)
        return instance.get_contents_as_string().split("\r\n")


    def get_all_files_from_folder(self, remote_folder, local_folder):
        """
        Method downloads files from folder in S3 bucket to folder on local machine

        :param remote_folder:
        :param local_folder:
        :return True if all files download successfully:
        :return False if download fails:
        """

        if len(list(self.bucket.list(remote_folder))) < 1 :
            print "Bucket : " + self.bucket.name + "; Folder: " + remote_folder + " is empty or does not exist."
            return False

        if not os.path.isdir(local_folder) :
            print "Local folder: " + local_folder + " not exists."
            return False

        try: 
            for key in self.bucket.list(remote_folder):
                fn = self._clean_filename(key.name)
                if fn: 
                    self.bucket.get_key(key).get_contents_to_filename(local_folder + fn)
                    print fn + " copied to " + local_folder
        except Exception as e:
            print e
            return False
            
        return True

    def _clean_filename(self, aws_fn):
        if aws_fn:
            pnams = aws_fn.split("/")
            if pnams[-1]:
                return re.sub(r'[_\s]+', "_", pnams[-1].lower())

        return None

    def move_file_to_new_folder(self, original_path, new_path):
        """
        Method moves file from folder on S3 to new folder on S3.  File should be written with folder and file name as
        "Folder/file" and vice versa

        :param original_path:
        :param new_path:
        :return True if file moves successfully:
        :return False if file doesn't transfer properly"
        """

        try:
            key = self.bucket.get_key(original_path)
            new_key = key.copy(self.bucket, new_path)
            time.sleep(3)
            if new_key.exists:
                key.delete()
        except Exception as e:
            print 'Error moving file to new folder'
            print e
            return False

        return True
