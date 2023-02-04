from tools import *


def run():
    dice_one = dice()
    dice_two = dice()
    dice_three = dice()
    dice_four = dice()
    dice_five = dice()
    dice_six = dice()
    dices = [dice_one, dice_two, dice_three, dice_four, dice_five, dice_six]
    print("Dices:")
    print(*dices)
    dices_str = str(dices)
    dices_int = dices_str.replace(" ", "")
    dices_int = dices_int.replace(",", "")
    dices_int = dices_int.replace("[", "")
    dices_int = dices_int.replace("]", "")

    for i in range(6):
        print(count_dice(dices_int, i))
