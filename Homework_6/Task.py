import os
import zipfile
import itertools
import string

# extract files
z = zipfile.ZipFile('./lesson6.zip', 'r')

for p in itertools.product(string.ascii_lowercase, string.ascii_lowercase, string.ascii_lowercase):
    try:
        z.extractall('.', pwd=bytes(''.join(p), 'utf-8'))
        print('Found password: {}'.format(''.join(p)))
        break
    except RuntimeError:
        continue
    except zipfile.zlib.error:
        continue
    except zipfile.BadZipFile:
        continue

# create folder
os.mkdir('./data')

# get data
cities = {}  # {city: {search: set(user_1, user_2)}}
for address, dirs, files in os.walk('./lesson6'):
    for file in files:
        with open(os.path.join(address, file)) as f:
            for line in f:
                data = line.split('\t')

                city = data[3]
                user_id = data[4]
                search = data[5]

                if city not in cities.keys():
                    cities[city] = {}
                if search not in cities[city].keys():
                    cities[city][search] = set()

                cities[city][search].add(user_id)

# write data to files
for city, city_data in cities.items():
    f1 = open('./data/{}.tsv'.format(city), 'w+')
    for search, user_ids in city_data.items():
        f1.write('{}\t{}\n'.format(search, len(user_ids)))
    f1.flush()
    f1.close()
