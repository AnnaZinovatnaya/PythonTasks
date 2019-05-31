from multiprocessing.connection import Listener
import random

# field = [['0' for x in range(10)] for x in range(10)]
field = [[' ' for x in range(10)] for x in range(10)]

def print_field():
    print('  A B C D E F G H I J')
    print('0 ' + ' '.join(field[0]))
    print('1 ' + ' '.join(field[1]))
    print('2 ' + ' '.join(field[2]))
    print('3 ' + ' '.join(field[3]))
    print('4 ' + ' '.join(field[4]))
    print('5 ' + ' '.join(field[5]))
    print('6 ' + ' '.join(field[6]))
    print('7 ' + ' '.join(field[7]))
    print('8 ' + ' '.join(field[8]))
    print('9 ' + ' '.join(field[9]))

def check_space(field, size_of_ship, is_vertical, x, y):
    if is_vertical:
        for i in range(x - 1, x + size_of_ship + 1):
            for j in range(y - 1, y + 2):
                if i >= 0 and j >= 0:
                    try:
                        if field[i][j] == '1':
                            return False
                    except IndexError:
                        continue 
    else:
        x, y = y, x

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + size_of_ship + 1):
                if i >= 0 and j >= 0:
                    try:
                        if field[i][j] == '1':
                            return False
                    except IndexError:
                        continue 

    return True


def generate_a_ship(size):

    is_space_ok = False

    while not is_space_ok:
        is_vertical = random.randint(0, 1)  # 0 - horizontal, 1 - vertical

        x = random.randint(0, (10 - size))
        y = random.randint(0, 9)

        is_space_ok = check_space(field, size, is_vertical, x, y)

    if is_vertical:
        for i in range(size):
            field[x + i][y] = '1'
    else:
        x, y = y, x

        for i in range(size):
            field[x][y + i] = '1'


generate_a_ship(4)
generate_a_ship(3)
generate_a_ship(3)
generate_a_ship(2)
generate_a_ship(2)
generate_a_ship(2)
generate_a_ship(1)
generate_a_ship(1)
generate_a_ship(1)
generate_a_ship(1)

print_field()



# address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
# listener = Listener(address, authkey='secret password')
# conn = listener.accept()
# print 'connection accepted from', listener.last_accepted
# while True:
#     msg = conn.recv()
#     print(msg)
#     # do something with msg
#     if msg == 'close':
#         conn.close()
#         break
# listener.close()
