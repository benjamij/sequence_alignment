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

