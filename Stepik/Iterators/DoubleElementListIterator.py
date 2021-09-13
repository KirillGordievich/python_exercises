class DoubleElementListIterator:
    def __init__(self, list):
        self.list = list
        self.count = 0

    def __next__(self):
        if self.count < len(self.list):
            self.count += 2
            try:
                return self.list[self.count - 2], self.list[self.count - 1]
            except IndexError:
                return self.list[self.count - 2], None
        else:
            raise StopIteration


class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    my_list = MyList(list)
    for i in my_list:
        print(i)