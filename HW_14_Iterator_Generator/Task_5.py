import os


def walker(path_to_directory):
    for subdir, dirs, files in os.walk(path_to_directory):
        for file in files:
        	yield os.path.join(subdir, file)


gen = walker('/home/hzinovatna/Desktop/Data/Py/vision_board')

for el in gen:
    print(el)