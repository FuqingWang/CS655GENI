import matplotlib.pyplot as plt
import numpy as np

def readResult():
    hitrate_latency = [[], []]
    with open("./result/latency_hitrate.txt", "r") as f:
        for line in f.readlines():
            hitrate, latency = list(map(float, line.split('\t')))
            hitrate_latency[0].append(hitrate)
            hitrate_latency[1].append(latency)
    return hitrate_latency


def plot(X, Y):
    # for file of 30MB, latency without cache is 6.74s, and 2.85s with cache
    plt.plot(X, Y, color='blue', label='measured')

    # draw the estimated line
    x = np.linspace(0, 1, num=50)
    y = 2.85 * x + (1-x) * 6.74
    plt.plot(x, y, color='red', linestyle='--', label='estimated')

    plt.title('Latency as a function of hitrate for file size 30MB')
    plt.xlabel('hitrate')
    plt.ylabel('latency / second')

    plt.ylim(0, 8)
    plt.xlim(0, 1)

    plt.grid(True)
    plt.legend()

    plt.savefig('./result/exp2.png')
    plt.show()

hitrate_latency = readResult()
plot(hitrate_latency[0], hitrate_latency[1])