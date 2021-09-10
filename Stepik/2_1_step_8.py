

class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            list.append(self, x)
        else:
            raise NonPositiveError


list_ = PositiveList([1, 2, 3, 4])
print(f'Initial list = {list_}')
while True:
    try:
        list_.append(int(input("Please enter a number: ")))
    except NonPositiveError:
        print("Only positive numbers are allowed to append! Try again...")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    else:
        print("The number was appended")
        break  # leave the circle

print(f'Updated list = {list_}')