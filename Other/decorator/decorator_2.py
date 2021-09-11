def logging(func):
    def log_function_called():
        print(f'Function {func.__name__} is called')
        func()
    return log_function_called


@logging
def print_zero():
    print('0')


if __name__ == '__main__':
    print_zero()
