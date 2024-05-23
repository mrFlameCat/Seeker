"Module contains classes for this program"
import os
import time

class ObjectDir():
    """Some docstring"""

    def __init__(self, path, size, changed):
        self.path = path
        self.size = size
        self.changed = changed
        self.type = "directory"

    def get_path(self):
        """Some docstring"""
        return self.path

    def get_size(self):
        """Some docstring"""
        return self.size

    def get_changed(self):
        """Some docstring"""
        return self.changed

    def get_type(self):
        """Some docstring"""
        return self.type

    def get_properties(self):
        """Some docstring"""
        properties = f"""Type: {self.type}, path: {self.path},
        size: {self.size}MB, changed: {self.changed}"""
        return properties


class ObjectFile():
    """Some docstring"""

    def __init__(self, path, size, changed):
        self.path = path
        self.size = size
        self.changed = changed
        self.type = "file"

    def get_path(self):
        """Some docstring"""
        return self.path

    def get_size(self):
        """Some docstring"""
        return self.size

    def get_changed(self):
        """Some docstring"""
        return self.changed

    def get_type(self):
        """Some docstring"""
        return self.type

    def get_properties(self):
        """Some docstring"""
        properties = f"""Type: {self.type}, path: {self.path},
        size: {self.size}MB, changed: {self.changed}"""
        return properties



class CreatorOfObjects():
    """Some docstring"""

    def __init__(self, path, main_list):
        """Some docstring"""
        self.path = path
        self.main_list = main_list


    def get_dir_size(self):
        """Some docstring"""
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                total_size += os.path.getsize(file_path)
        return total_size / 1048576



    def create_objects(self):
        """Some docstring"""

        if os.path.isdir(self.path):
            timestamp_direct = os.path.getmtime(self.path)
            formated_time_direct = time.strftime("%d-%m-%Y %H:%M:%S",
                                                    time.localtime(timestamp_direct))
            size_directory = round(self.get_dir_size(), 2)
            direct = ObjectDir(self.path, size_directory, formated_time_direct)
            self.main_list.append(direct)
        else:
            size_file = round(os.path.getsize(self.path) / 1048576, 2)
            timestamp_file = os.path.getmtime(self.path)
            formated_time_file = time.strftime("%d-%m-%Y %H:%M:%S",
                                                time.localtime(timestamp_file))
            file = ObjectFile(self.path, size_file, formated_time_file)
            self.main_list.append(file)