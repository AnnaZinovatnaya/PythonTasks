import traceback


class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def log_to_file(self, path):
        with open(path, 'w') as f:
            f.write(f'Exception: {self.message}\n')
            for line in traceback.format_tb(self.__traceback__):
                f.write(line)


try:
    raise CustomException("custom exception")
except CustomException as e:
    e.log_to_file('log.txt')
