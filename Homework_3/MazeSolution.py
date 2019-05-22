import queue
import collections

maze = ['111111111111111111',
        '1x0010000000000001',
        '111011101111111101',
        '101010000100000001',
        '101011010101111111',
        '101000010100001001',
        '100011110101111101',
        '101110010100000001',
        '100000000101101111',
        '101101111100100001',
        '101001000000101001',
        '101101111111101001',
        '101000000000001001',
        '101011110100101001',
        '101000010111111001',
        '111011110100000001',
        '101000000101111111',
        '101011110101010101',
        '1000000101000000#1',
        '111111111111111111']
        
for i, row in enumerate(maze):
    for j, symbol in enumerate(row):
        if symbol == 'x':
            print('Start point: ' + str(i) + ', ' + str(j))
            start_point = (i, j)
        elif symbol == '#':
            print('End point: ' + str(i) + ', ' + str(j))
            end_point = (i, j)

was = {}
q = queue.Queue()

q.put(start_point)
was[start_point] = None

while q:
    current_point = q.get()
    if current_point == end_point:
        break

    if maze[current_point[0] - 1][current_point[1]] != '1':
        if (current_point[0] - 1, current_point[1]) not in was.keys():
            was[(current_point[0] - 1, current_point[1])] = current_point
            q.put((current_point[0] - 1, current_point[1]))
    if maze[current_point[0]][current_point[1] - 1] != '1':
        if (current_point[0], current_point[1] - 1) not in was.keys():
            was[(current_point[0], current_point[1] - 1)] = current_point
            q.put((current_point[0], current_point[1] - 1))
    if maze[current_point[0] + 1][current_point[1]] != '1':
        if (current_point[0] + 1, current_point[1]) not in was.keys():
            was[(current_point[0] + 1, current_point[1])] = current_point
            q.put((current_point[0] + 1, current_point[1]))
    if maze[current_point[0]][current_point[1] + 1] != '1':
        if (current_point[0], current_point[1] + 1) not in was.keys():
            was[(current_point[0], current_point[1] + 1)] = current_point
            q.put((current_point[0], current_point[1] + 1))

path = [end_point, ]
point = end_point
while was[point] is not None:
    path.append(was[point])
    point = was[point]

print("PATH:")
for i, p in enumerate(path[::-1], start = 1):
    print('Step ' + str(i) + ': ' + str(p))
