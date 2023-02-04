from random import randint


def dice():
    return randint(1, 6)


def count_dice(numbers, integer):
    out = []
    count = numbers.count(str(integer))
    for i in range(count):
        out.append(integer)
        if len(out) != 1 or len(out) != 0:
            return out
