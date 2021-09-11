# source https://sumit-ghosh.com/articles/demystifying-decorators-python/
import requests
import time


def benchmark(func):
	def wrapper():
		start = time.time()
		func()
		end = time.time()
		print(f'Execution time: {end - start} seconds.')
	return wrapper


@benchmark
def fetch_webpage():
	page = requests.get('https://google.com')


if __name__ == '__main__':
	fetch_webpage()