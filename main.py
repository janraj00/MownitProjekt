import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from random import randint

from numpy import ndarray


def Median_filter(data, window_size):
    output = np.zeros((len(data), len(data[0])))
    width = len(data[0])
    height = len(data)
    for i in range(len(data)):
        for j in range(len(data[0])):
            W = []
            for w in range(window_size // 2):
                left, right = j - w, j + w
                down, up = i + w, i - w
                if left >= 0 and down < height:
                    W.append(data[left][down])
                if left >= 0 and up >= 0:
                    W.append(data[left][up])
                if right < width and down < height:
                    W.append(data[right][down])
                if right < width and up >= 0:
                    W.append(data[right][up])
            output[i][j] = np.median(W)
            print(output[i][j])
    return output


def Wiener_filter(data, windowX, windowY, szum):
    output = np.zeros((len(data), len(data[0])))
    hor = (windowX-1)//2
    ver = (windowY-1)//2
    for i in range(len(data)):
        for j in range(len(data[0])):
            W = []
            startX, endX = max(0, i-hor), min(len(data), i+hor)
            startY, endY = max(0, j-ver), min(len(data[0]), j+ver)
            for p in range(startX, endX):
                for q in range(startY, endY):
                    W.append(data[p][q])
            mu = np.average(W)
            sigma = np.var(W)
            output[i][j] = mu + (data[i][j] - mu)*(sigma-szum)//sigma
    return output