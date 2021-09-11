# source https://sumit-ghosh.com/articles/demystifying-decorators-python/
import requests
import time


def benchmark(func):

	def wrapper(*args, **kwargs):
		start = time.time()
		return_value = func(*args, **kwargs)
		end = time.time()
		print('{} Execution time: {} seconds.'.format(args, end - start))
		return return_value

	return wrapper


@benchmark
def fetch_webpage(url):
	webpage = requests.get(url)
	return webpage.text


if __name__ == '__main__':
	pages = ['https://www.youtube.com/', 'https://google.com']
	for page in pages:
		webpage = fetch_webpage(page)
		#print(webpage)