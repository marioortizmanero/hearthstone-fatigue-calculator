def error():
    print("Whoops, something went wrong. Please try again.")


def calc_mode(t, s):
    d = 0
    for i in range(s, t+s):
        d = d + i
    return d


def lethal_mode(d_input, s):
    d_calc = 0
    i = 1
    t = 0
    while d_calc < d_input:
        d_calc = d_calc + i
        i += 1
        t += 1
    return t


print("~~~~ HEARTHSTONE FATIGUE CALCULATOR by Glow8 ~~~~")

while True:  # Checks if the mode input is valid
    try:
        mode = int(input("\nMODES: "
                         "\n* '1' to get the turns needed for X damage "
                         "\n* '2' to get the damage dealt in X turns "
                         "\nPlease type to select your mode: "))
    except ValueError:
        error()
        continue
    else:
        while True:
            if mode == 1:  # Checks if the input after the mode is valid
                while True:
                    try:
                        damageInput = int(input("\nPlease input the damage needed for lethal: "))
                        startInput = int(input("Starting at how much damage? (default is 1): "))
                    except ValueError:
                        error()
                        continue
                    else:

                        print("\n>> You will need %d fatigue turns for that sweet lethal"
                              % lethal_mode(damageInput, startInput))
                        continue

            if mode == 2:
                while True:
                    try:
                        turnsInput = int(input("\nPlease input the fatigue turns: "))
                        startInput = int(input("Starting at how much damage? (default is 1): "))
                    except ValueError:
                        error()
                        continue
                    else:
                        print("\n>> It will deal %d damage" % calc_mode(turnsInput, startInput))
                        continue

            else:
                error()
                break
