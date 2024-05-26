"Module contains classes for program Seeker."
import os
import time
import fun

class ObjectDir():
    """Class describes a directory."""

    def __init__(self, path, size, changed):
        self.path = path
        self.size = size
        self.changed = changed
        self.type = "Directory"

    def get_path(self):
        """Return full path directory."""
        return self.path

    def get_size(self):
        """Return size directory."""
        return self.size

    def get_changed(self):
        """Return date of last changes directory."""
        return self.changed

    def get_type(self):
        """Return type of object: string 'diretory'."""
        return self.type

    def get_properties(self):
        """Return type, path,size and changes together."""
        properties = (
            f"{self.type}\n"
            f"path: {self.path}\n"
            f"size: {self.size}MB, changed: {self.changed}"
        )
        return properties


class ObjectFile():
    """Class describes a file."""

    def __init__(self, path, size, changed):
        self.path = path
        self.size = size
        self.changed = changed
        self.type = "File"

    def get_path(self):
        """Return full path of file."""
        return self.path

    def get_size(self):
        """Return a file's size."""
        return self.size

    def get_changed(self):
        """Return date of last changes."""
        return self.changed

    def get_type(self):
        """Return type of object: string 'file'."""
        return self.type

    def get_properties(self):
        """Return type, path,size and changes together."""
        properties = (
            f"{self.type}\n"
            f"path: {self.path}\n"
            f"size: {self.size}MB, changed: {self.changed}"
        )
        return properties



class CreatorOfObjects():
    """Class create an object of directories and files"""

    def __init__(self, path, main_list):
        self.path = path
        self.main_list = main_list


    def get_dir_size(self):
        """Folder size calculation."""
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                total_size += os.path.getsize(file_path)
        return total_size / 1048576



    def create_objects(self):
        """This method directly creates objects."""

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
