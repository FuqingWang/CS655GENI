import requests
import time
import os

# create folder 'result' if not exist
if not os.path.exists('result'):
    os.makedirs('result')

logPath = "./result/timeWithCache.txt"
cacheIP = "10.10.1.2"

for size in range(5, 101, 5):
	fname = "file.{}M".format(size)
	url = "http://{}:8080/static/cache/{}".format(cacheIP, fname)

	start = time.time()
	requests.get(url)
	end = time.time()

	latency = round(end-start, 2)

	with open(logPath, "a+") as f:
		f.write("{}\t{}\n".format(size, latency))