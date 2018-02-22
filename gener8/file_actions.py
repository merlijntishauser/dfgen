import pathlib
import os
import shutil


class FileActions:

    def __init__(self, path='output'):
        self.path = os.getcwd() + '/' + path
        self._create_dir()

    def _create_dir(self):
        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def get_current_location():
        return os.path.dirname(os.path.realpath(__file__))

    def write_file(self, filename, content):
        full_path = str(self.path) + '/' + filename
        new_file = open(full_path, 'w')
        new_file.write(content)
        new_file.close()
        return full_path

    def copy_to_path(self, source, destination_dir, destination_filename):
        pathlib.Path(self.path + '/' + destination_dir).mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, self.path + '/' + destination_dir + '/' + destination_filename)
