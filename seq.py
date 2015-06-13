__author__ = 'benjaminjakobus'

import copy

def sequence_alignment(m, n, x, y, d, a):
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

