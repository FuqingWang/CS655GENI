# measure the latency to fetch all files
import requests
import time
import os
import random
import argparse

# command parser
parser = argparse.ArgumentParser(description='Experiment 2 for GENI project: latency as a function of hit rate')
parser.add_argument('--loop', '-l', help='Loop time, required', type=int, required=True)
parser.add_argument('--size', '-s', help='File size, required', type=int, required=True)
args = parser.parse_args()

# create folder 'result' if not exist
if not os.path.exists('result'):
    os.makedirs('result')

cacheIP = "10.10.1.2"
loop = args.loop
size = args.size
logPath = "./result/latency_hitrate_{}.txt".format(size)

for hitrate in range(0, 11):
	latency = 0
	for _ in range(loop):
		num = random.randint(1, 10)
		if num > hitrate:
			fname = "file.{}M.nocache".format(size)
			url = "http://{}:8080/static/nocache/{}".format(cacheIP, fname)

			start = time.time()
			requests.get(url, headers={'Cache-Control': 'no-cache'})
			end = time.time()
			latency += end-start
		else:
			fname = "file.{}M".format(size)
			url = "http://{}:8080/static/cache/{}".format(cacheIP, fname)

			start = time.time()
			requests.get(url)
			end = time.time()
			latency += end-start

	with open(logPath, "a+") as f:
		f.write("{}\t{}\n".format(hitrate/10, round(latency/loop, 2)))