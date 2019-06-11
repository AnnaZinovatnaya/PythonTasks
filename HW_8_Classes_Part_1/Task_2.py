class BracketsCheck(object):
    def __init__(self):
        self.data = input()

    def check(self):
        brackets_buffer = []
        brackets = {'[': ']', '{': '}', '<': '>', '(': ')'}
        result = True

        for ch in self.data:
            if ch not in brackets.keys() and ch not in brackets.values():
                result = False
                break
            elif ch in brackets:
                brackets_buffer.append(ch)
                continue
            elif len(brackets_buffer) != 0 and ch == brackets[brackets_buffer[-1]]:
                brackets_buffer.pop(-1)
                continue
            else:
                result = False
                break

        if len(brackets_buffer) != 0:
            result = False

        return result


b = BracketsCheck()
print(b.check())

