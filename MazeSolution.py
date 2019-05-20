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

was = set()
q = queue.Queue()

start = (1, 1)
current = (1, 1)
end = '#'
end_point = (0, 0)

q.put(item=start)
was.add(start)
q.get()

pathDict = collections.OrderedDict()
step = 1
end_point = (0, 0)
while maze[current[0]][current[1]] != '#':
    print("---")
    print('Step ' + str(step) + ': (' + str(current[0]) + ', ' + str(current[1]) + ')')

    if maze[current[0] - 1][current[1]] == '0' or maze[current[0] - 1][current[1]] == '#':
        if (current[0] - 1, current[1]) not in was:
            q.put(item=(current[0] - 1, current[1]))
        if maze[current[0] - 1][current[1]] == '#':
            end_point = (maze[current[0] - 1], [current[1]])
    if maze[current[0]][current[1] - 1] == '0'or maze[current[0]][current[1] - 1] == '#':
        if (current[0], current[1] - 1) not in was:
            q.put(item=(current[0], current[1] - 1))
        if maze[current[0]][current[1] - 1] == '#':
            end_point = (maze[current[0]], [current[1] - 1])
    if maze[current[0] + 1][current[1]] == '0'or maze[current[0] + 1][current[1]] == '#':
        if (current[0] + 1, current[1]) not in was:
            q.put(item=(current[0] + 1, current[1]))
        if maze[current[0] + 1][current[1]] == '#':
            end_point = (maze[current[0] + 1], [current[1]])
    if maze[current[0]][current[1] + 1] == '0' or maze[current[0]][current[1] + 1] == '#':
        if (current[0], current[1] + 1) not in was:
            q.put(item=(current[0], current[1] + 1))
        if maze[current[0]][current[1] + 1] == '#':
            end_point = (current[0], current[1] + 1)

    prev = current
    current = q.get()

    pathDict[current] = prev
    was.add(current)
    step += 1

print('\nthe end')
print(end_point)

# TODO: print path
