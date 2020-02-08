#!/bin/python3

import math
from collections import defaultdict


# Gets the trapezoidal number starting at k
# a.k.a. getting the total fatigue damage for calc mode
# See README.md for more info about the formula
def trapezoidalNumber(l, k):
    return int(l*(2*(k-1)+l+1)/2) if (l >= 0 and k >= 0) else 0


# Finds valid l in the previous formula (for lethal mode)
# a.k.a. getting the number of turns to reach a fatigue damage
# See README.md for more info about the formula
def findTrapezoidalNumber(n, k):
    return int(0.5 * (math.sqrt(4*k**2-4*k+8*n+1) - 2*k + 1)) \
        if (n >= 0 and k >= 0) else 0


# Mode 1: calculates turns needed for X cumulative fatigue damage
def lethalMode():
    # Cleanly getting the values:
    while True:
        try:
            maxDmg = int(input("Please input the damage needed for lethal: "))
            dmg = int(input("Starting at how much damage? (default is 1): ")
                      or 1)
        except ValueError:
            print("ERROR: Your input value was invalid.\n")
        else:
            break

    print(f">> You will need {findTrapezoidalNumber(maxDmg, dmg)} fatigue"
           " turn(s) for that sweet lethal\n")


# Mode 2: calculates cumulative fatigue damage
def calcMode():
    # Cleanly getting the values:
    while True:
        try:
            turns = int(input("Please input the fatigue turns: "))
            dmg = int(input("Starting at how much damage? (default is 1): ")
                      or 1)
        except ValueError:
            print("ERROR: Your input value was invalid.\n")
        else:
            break

    print(f">> It will deal {trapezoidalNumber(turns, dmg)} damage\n")


def main():
    print("~ Hearthstone Fatigue Calculator by Mario O.M. ~")
    while True:
        print("1. Lethal mode: turns needed for X damage\n"
              "2. Calculator mode: damage dealt in X turns")
        mode = input("Please type the desired mode (1 or 2): ").strip()
        if mode == "1":
            lethalMode()
        elif mode == "2":
            calcMode()
        else:
            print("ERROR: Please select a valid mode.\n")


if __name__ == '__main__':
    main()
