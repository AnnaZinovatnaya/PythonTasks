import json
import pprint
import os

class JsonWorker(object):
    @staticmethod
    def read_file(path_to_file):
        with open(path_to_file, 'r') as f:
            data = json.load(f)
            return data

    @staticmethod
    def get_absolute_path(relative_path):
        return os.path.abspath(relative_path)

    @staticmethod
    def get_relative_path(absolute_path):
        return os.path.relpath(absolute_path)

    @staticmethod
    def save_to_file(data_dict, path_to_file):
        with open(path_to_file, "w") as f:
            json.dump(data_dict, f)

    @staticmethod
    def join_files(file1, file2, new_file_path):
        with open(file1, 'r') as f:
            data1 = json.load(f)
        with open(file2, 'r') as f:
            data2 = json.load(f)
        joined_data = {**data1, **data2}
        with open(new_file_path, "w") as f:
            json.dump(joined_data, f) 


pprint.pprint(JsonWorker.read_file('a.json')) 
print(JsonWorker.get_absolute_path('a.json'))
print(JsonWorker.get_relative_path('/home/hzinovatna/Desktop/Data/Py/PythonTasks/HW_8_Classes_Part_1/a.json'))

JsonWorker.save_to_file(JsonWorker.read_file('a.json'), 'www.json')
pprint.pprint(JsonWorker.read_file('www.json'))


JsonWorker.join_files('a.json', 'b.json', new_file_path='ab.json')
pprint.pprint(JsonWorker.read_file('ab.json'))

