from random import randint
import time


def create_random_list(n, x0=0, xn=100):
    # create list (x0, x1, ... , xn)
    random_list = []
    for i in range(n):
        x = randint(x0, xn + 1)
        count = 0
        while x in random_list and count < 25:
            x = randint(x0, xn + 1)
            count += 1
        random_list.append(x)
    return random_list


def swap(list, i, j):
    # swap two elements in a list
    list[i], list[j] = list[j], list[i]
    return list


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Execution time: {end - start} seconds.')

    return wrapper


@benchmark
def bubble_sort(list):
    length = len(list)
    num_of_iterations = 0
    num_of_swaps = 0
    unsorted = True

    while unsorted:
        # assume that the list is sorted
        unsorted = False
        for i in range(length - num_of_iterations - 1):
            if list[i] > list[i+1]:
                # Swap
                swap(list, i, i+1)
                # if we swapped elements, list is unsorted
                unsorted = True
                num_of_swaps += 1
        num_of_iterations += 1
    print('The number of swaps: %s' % num_of_swaps)
    return list


desired_length = 20
list = create_random_list(desired_length)
list = [i for i in range(desired_length, 0, -1)]
print('Unsorted list: %s' % list)
bubble_sort(list)
print('Sorted list: %s' % list)
