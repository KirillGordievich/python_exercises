# source https://sumit-ghosh.com/articles/demystifying-decorators-python/
import requests
import time


def benchmark(iters):

	def actual_decorator(func):

		def wrapper(*args, **kwargs):
			total = 0
			# list for save execution time
			time_list = []
			for i in range(iters):
				start = time.time()
				return_value = func(*args, **kwargs)
				end = time.time()
				# save execution time
				time_list.append(end - start)
				# count the total amount of execution time
				total = total + (end - start)
			print(f'Average execution time: {total / iters} seconds, time list:')
			for time_ in time_list:
				print(time_list.index(time_)+1,' - ', time_)
			return return_value

		return wrapper

	return actual_decorator


@benchmark(iters=10)
def fetch_webpage(url):
	webpage = requests.get(url)
	return webpage.text


if __name__ == '__main__':
	webpage = fetch_webpage('https://google.com')