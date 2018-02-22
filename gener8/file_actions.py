import pathlib
import os


class FileActions:

    def __init__(self, path='output'):
        self.path = os.getcwd() + '/' + path
        self._create_dir()

    def _create_dir(self):
        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)

    def write_file(self, filename, content):
        full_path = str(self.path) + '/' + filename
        new_file = open(full_path, 'w')
        new_file.write(content)
        new_file.close()
        return full_path
