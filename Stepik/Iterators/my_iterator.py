from random import random


class RandomIterator:

    def __init__(self, max_iter):
        # maximum number of iterations
        self.max_iter = max_iter
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._count < self.max_iter:
            self._count += 1
            return random()
        else:
            raise StopIteration


x = RandomIterator(10)

for i in x:
    print(i)