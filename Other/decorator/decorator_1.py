#!/usr/bin/env python


def enclose(fun):

    def wrapper(*args, **kwargs):

        print("***************************")
        fun(*args, **kwargs)
        print("***************************")

    return wrapper


@enclose
def myfun(name, age):
    print(f'{name} is {age} years old')

if __name__ == '__main__':
    myfun(name='Peter', age=32)
    myfun('Roman', 29)