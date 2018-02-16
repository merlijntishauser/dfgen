import pathlib
import os


class FileActions:

    def __init__(self, path='output'):
        self.path = os.getcwd() + '/' + path
        self._create_dir()

    def _create_dir(self):
        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)

    def write_file(self, filename, content):
        fqfn = str(self.path) + '/' + filename
        print(fqfn)
        new_file = open(fqfn, 'w')
        new_file.write(content)
        new_file.close()
