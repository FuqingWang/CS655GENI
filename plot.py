import matplotlib.pyplot as plt

def readResult():
    timeWithoutCache = [[], []]
    timeWithCache = [[], []]
    with open("./result/timeWithoutCache.txt", "r") as f:
        for line in f.readlines():
            size, latency = list(map(float, line.split('\t')))
            timeWithoutCache[0].append(size)
            timeWithoutCache[1].append(latency)

    with open("./result/timeWithCache.txt", "r") as f:
        for line in f.readlines():
            size, latency = list(map(float, line.split('\t')))
            timeWithCache[0].append(size)
            timeWithCache[1].append(latency)
    return timeWithoutCache, timeWithCache

def plot(X1, Y1, X2, Y2):
    plt.plot(X1, Y1, color='blue', label='without cache')
    plt.plot(X2, Y2, color='green', label='with cache')

    plt.xlabel('file size / MB')
    plt.ylabel('latency / second')

    plt.grid(True)
    plt.legend()

    plt.savefig('withOrWithoutCache.png')
    plt.show()
    

if __name__=='__main__':
    timeWithoutCache, timeWithCache = readResult()

    plot(timeWithoutCache[0], timeWithoutCache[1], timeWithCache[0], timeWithCache[1])