from random import randint


def dice():
    return randint(1, 6)


def count_dice(a):
    a_count = a.count(1)
