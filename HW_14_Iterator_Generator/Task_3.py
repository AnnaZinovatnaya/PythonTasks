def reader(path_to_file):
    unique_lines = set()
    with open(path_to_file) as f:
        for line in f:
            line = line.strip('\n')
            if line not in unique_lines:
                unique_lines.add(line)
                yield line


gen = reader('file.txt')

for line in gen:
    print(line)