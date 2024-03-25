import time


class ParserDecorators:
    @staticmethod
    def infinite(f):
        def wrapper(*args, **kwargs):
            while True:
                f(*args, **kwargs)
                time.sleep(1000)

        return wrapper

    @staticmethod
    def count_time(f):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            f(*args, **kwargs)
            end_time = time.time()

        return wrapper
