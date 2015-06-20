__author__ = 'benjaminjakobus'

import copy

def sequence_alignment(m, n, x, y, d, a):
    """ Determines optimal sequence alignment for two strings (x and y) in linear time.

            Args:
                m   - Number of characters in x
                n   - Number of characters in y
                x   - First string
                y   - Second string
                d
                a

    """
    CURRENT = []
    LAST = []
    for i in range(0, m):
        CURRENT[i] = i * d

    for j in range(0, n):
        LAST = copy.copy(CURRENT)
        CURRENT[0] = j * a
        for i in range(m):
            _a = 0 if (x[i] == x[j]) else a
            CURRENT[i] = min(_a + LAST[i - 1], d + LAST[i], d + CURRENT[i - 1])

    return CURRENT[m]


def find_sequence(i, j, x, y, d, a, M):
    s = [[], []]
    if i == 0 or j == 0:
        return
    _a = 0 if (x[i] == x[j]) else a
    if M[i][j] == _a * M[i - 1][j - 1]:
        s[0] = x[i]
        s[1] = y[j]
        return s + find_sequence(i - 1, j - 1, x, y, d, a, M)
    elif M[i][j] == d + M[i - 1][j]:
        return find_sequence(i - 1, j, x, y, d, a, M)
    else:
        return find_sequence(i, j - 1, x, y, d, a, M)

from copy import deepcopy
import sys


sys.setrecursionlimit(200000)


def sequence_alignemt(x, y, g, a):
    """ Determines optimal sequence alignment for two strings (x and y) with\
        O(m.n) space and time complexity.
            Args:
                x   - First string
                y   - Second string
                g   - Gap penalty
                a   - Mismatch penalty
    """
    m = len(x)  # Number of characters in x
    n = len(y)  # Number of characters in y
    M = [[0 for i in range(n)] for j in range(m)]

    # Fills the first line of the matrix
    for i in range(m):
        M[i][0] = i*g
    # Fills the first column of the matrix
    for j in range(n):
        M[0][j] = j*g

    for i in range(1, m):
        for j in range(1, n):
            _a = 0 if x[i] == y[j] else a
            M[i][j] = min(_a + M[i - 1][j - 1],
                          g + M[i - 1][j],
                          g + M[i][j - 1])
    return M, M[m-1][n-1]


def get_sequence(x, y, g, a, M):
    """ Recovers the sequence alignment based on the matrix of cost.
            Args:
                x   - First string
                y   - Second string
                g   - Gap penalty
                a   - Mismatch penalty
                M   - Matrix of cost
    """
    diff = [[], []]
    find_sequence(len(x) - 1, len(y) - 1, x, y, g, a, M, diff)
    diff[0].reverse()
    diff[1].reverse()
    return "".join(diff[0]), "".join(diff[1])


def find_sequence(i, j, x, y, g, a, M, diff):
    if i > 0 or j > 0:
        _a = 0 if x[i] == y[j] else a
        if M[i][j] == _a + M[i - 1][j - 1]:
            if _a == a:
                _add_to_diff(diff, "<%s>" % x[i], "<%s>" % y[j])
            _add_to_diff(diff, x[i], y[j])
            return find_sequence(i - 1, j - 1, x, y, g, a, M, diff)
        elif M[i][j] == g + M[i - 1][j]:
            _add_to_diff(diff, x[i], "*")
            return find_sequence(i - 1, j, x, y, g, a, M, diff)
        else:
            _add_to_diff(diff, "*", y[j])
            return find_sequence(i, j - 1, x, y, g, a, M, diff)
    elif j == 0 and i == 0:
        _add_to_diff(diff, x[i], y[j])


def _add_to_diff(diff, x, y):
    diff[0].append(x)
    diff[1].append(y)


def linear_sequence_alignment(x, y, g, a):
    """ Determines optimal sequence alignment for two strings (x and y) with\
        linear space.
            Args:
                x   - First string
                y   - Second string
                g   - Gap penalty
                a   - Mismatch penalty
    """
    print("input:", x, y)
    m = len(x)  # Number of characters in x
    n = len(y)  # Number of characters in y
    CURRENT = [i * g for i in range(m + 1)]

    for j in range(1, n):
        LAST = deepcopy(CURRENT)
        CURRENT[0] = j * a
        for i in range(1, m):
            _a = 0 if (x[i] == y[j]) else a
            CURRENT[i] = min(_a + LAST[i - 1], g + LAST[i], g + CURRENT[i - 1])

    return CURRENT, CURRENT[m - 1]


def divide_and_conquer_alignment(x, y, g, a):
    m = len(x)
    n = len(y)
    if m <= 2 or n <= 2:
        print("mn ", m, n)
        v, _ = linear_sequence_alignment(x, y, g, a)

    if m > 0 and n > 0:
        _f, _ = linear_sequence_alignment(x, y[:int(n/2 - 1)], g, a)
        _g, _ = linear_sequence_alignment(x, y[int(n/2):], g, a)
        r = [_f[i] + _g[i] for i in range(len(_f))]
        q = r.index(min(r))


        divide_and_conquer_alignment(x[:(q - 1)], y[:int(n/2 - 1)], g, a)
        divide_and_conquer_alignment(x[q:(n-1)], y[int(n / 2):], g, a)



x = "AB"
y = "BA"
g = 0.7
a = 1

V, cost = linear_sequence_alignment(x, y, g, a)


print(divide_and_conquer_alignment(x, y, g, a))

