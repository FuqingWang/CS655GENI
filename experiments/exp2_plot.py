import matplotlib.pyplot as plt
import numpy as np
import argparse

# command parser
parser = argparse.ArgumentParser(description='Experiment 2 for GENI project: latency as a function of hit rate')
parser.add_argument('--size', '-s', help='File size, required', type=int, required=True)
args = parser.parse_args()

size = args.size

def readResult():
    hitrate_latency = [[], []]
    with open("./result/latency_hitrate_{}.txt".format(size), "r") as f:
        for line in f.readlines():
            hitrate, latency = list(map(float, line.split('\t')))
            hitrate_latency[0].append(hitrate)
            hitrate_latency[1].append(latency)
    return hitrate_latency


def plot(X, Y):
    # for file of 30MB, latency without cache is Y[0], and Y[-1] with cache
    plt.plot(X, Y, color='blue', label='measured')

    # draw the estimated line
    x = np.linspace(0, 1, num=50)
    y = Y[-1] * x + (1-x) * Y[0]
    plt.plot(x, y, color='red', linestyle='--', label='estimated')

    plt.title('Latency as a function of hitrate for file size {}MB'.format(size))
    plt.xlabel('hitrate')
    plt.ylabel('latency / second')

    plt.ylim(0, 10)
    plt.xlim(0, 1)

    plt.grid(True)
    plt.legend()

    plt.savefig('./result/exp2_{}MB.png'.format(size))

hitrate_latency = readResult()
plot(hitrate_latency[0], hitrate_latency[1])