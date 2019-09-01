#!/bin/python3

import math
from collections import defaultdict


# Default error message
def error():
    print("\nWhoops! Something went wrong. Please check if your input was valid.")


# Handler for Ctrl+C forced exit
def inputHandler(text):
    try:
        return input(text)
    except KeyboardInterrupt:
        print("\nClosing the program...")
        quit()


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
    while True:
        # Cleanly getting the values:
        while True:
            try:
                maxDmg = int(inputHandler("\nPlease input the damage needed for lethal: "))
                dmg = int(inputHandler("Starting at how much damage? (default is 1): ") or 1)
            except ValueError:
                error()
            else:
                break

        print(f"\n>> You will need {findTrapezoidalNumber(maxDmg, dmg)} fatigue turns for that sweet lethal")


# Mode 2: calculates cumulative fatigue damage
def calcMode():
    while True:
        # Cleanly getting the values:
        while True:
            try:
                turns = int(inputHandler("\nPlease input the fatigue turns: "))
                dmg = int(inputHandler("Starting at how much damage? (default is 1): ") or 1)
            except ValueError:
                error()
            else:
                break

        print(f"\n>> It will deal {trapezoidalNumber(turns, dmg)} damage")


def main():
    # The input is obtained with a dictionary containing the mode functions
    modesDict = defaultdict(lambda: error, {"1": lethalMode, "2": calcMode})

    print("~ Hearthstone Fatigue Calculator by Mario O.M. ~")
    while True:
        mode = inputHandler("\n1. Lethal mode: turns needed for X damage"
                            "\n2. Calculator mode: damage dealt in X turns"
                            "\nPlease type the desired mode (1 or 2): ")
        modesDict[mode]()


if __name__ == '__main__':
    main()
