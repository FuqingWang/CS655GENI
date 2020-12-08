# measure the latency to fetch all files
import requests
import time
import os
import random

logPath = "./result/latency_hitrate.txt"
loop = 20

for hitrate in range(1, 10):
	latency = 0
	size = 30
	for _ in range(loop):
		num = random.randint(1,11)
		if num > hitrate:
			fname = "file.{}M.nocache".format(size)
			url = "http://10.10.1.1:8080/static/nocache/{}".format(fname)

			start = time.time()
			requests.get(url, headers={'Cache-Control': 'no-cache'})
			end = time.time()
			latency += end-start
		else:
			fname = "file.{}M".format(size)
			url = "http://10.10.1.1:8080/static/cache/{}".format(fname)

			start = time.time()
			requests.get(url)
			end = time.time()
			latency += end-start

	with open(logPath, "a+") as f:
		f.write("{}\t{}\n".format(hitrate/10, round(latency/loop, 2)))