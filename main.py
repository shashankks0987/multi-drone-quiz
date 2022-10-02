import math
import time
from result import *
import numpy as np


def calc_distance(x, i, y, g):
    return math.floor(np.square(x - i) + np.square(g[i][y]))


def sep(i, u, res, y):
    return math.floor((np.square(u) - np.square(i) + np.square(res[u][y]) - np.square(res[i][y])) / (2 * (u - i)))


def esdf(M, N, obstacle_list):
    """
    :param M: Row number
    :param N: Column number
    :param obstacle_list: Obstacle list
    :return: An array. The value of each cell means the closest distance to the obstacle
    """
    grid = np.array([[0.0 for _ in range(N)] for _ in range(M)])
    for k in obstacle_list:
        grid[k[0]][k[1]] = 1.0
    res = get_euc(M, N, grid)
    return res


def get_euc(M, N, grid):
    g = np.array([[None for _ in range(N)] for _ in range(M)])
    res1 = np.array([[None for _ in range(N)] for _ in range(M)])
    for i in range(M):
        if grid[i][0] - 1.0 == 0:
            g[i][0] = 0.0
        else:
            g[i][0] = (M + N) * 1.0
        for j in range(1, N):
            if grid[i][j] - 1.0 == 0:
                g[i][j] = 0.0
            else:
                g[i][j] = 1 + g[i][(j - 1)]
        for j in range(N - 1, -1, -1):
            if j + 1 < N:
                if g[i][(j + 1)] < g[i][j]:
                    g[i][j] = 1 + g[i][j + 1]
    s = [0] * M
    t = [0] * M
    for j in range(N):
        q = 0
        s[0] = 0
        t[0] = 0
        for u in range(1, M):
            while q >= 0 and (calc_distance(t[q], s[q], j, g) > calc_distance(t[q], u, j, g)):
                q = q - 1
            if q < 0:
                q = 0
                s[0] = u
            else:
                w = 1 + sep(s[q], u, g, j)
                if w < M:
                    q = q + 1
                    s[q] = u
                    t[q] = w

        for u in range(M - 1, -1, -1):
            res1[u, j] = math.sqrt(calc_distance(u, s[q], j, g))
            if u == t[q]:
                q = q - 1
    return res1


if __name__ == '__main__':
    st = time.time()
    for _ in range(int(2e4)):
        assert np.array_equal(esdf(M=3, N=3, obstacle_list=[[0, 1], [2, 2]]), res_1)
        assert np.array_equal(esdf(M=4, N=5, obstacle_list=[[0, 1], [2, 2], [3, 1]]), res_2)

    et = time.time()
    print(et-st)
