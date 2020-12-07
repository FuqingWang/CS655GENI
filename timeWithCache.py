import wget
import time

logPath = "timeWithCache.txt"

for size in range(5, 101, 5):
	fname = "file.{}M".format(size)
	url = "http://10.10.1.1:8080/static/{}".format(fname)

	start = time.time()
	wget.download(url)
	end = time.time()

	latency = round(end-start, 2)

	with open(logPath, "a+") as f:
		f.write("{}\t{}\n".format(size, latency))