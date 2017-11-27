import threading
import time


def g(y, x):
    print(y)
    print(x)


def t(**kwargs):
    print(kwargs)
    g(**kwargs)

t(x=7, y=1)

t(y=7, x=2)

