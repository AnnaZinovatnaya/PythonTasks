import traceback


class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def log_to_file(self, path):
        with open(path, 'a') as file:
            file.write(f'Exception: {self.message}\n')
            for line in traceback.format_tb(self.__traceback__):
                file.write(line)


try:
    raise CustomException('Some exception')
except CustomException as e:
    e.log_to_file('log.txt')
