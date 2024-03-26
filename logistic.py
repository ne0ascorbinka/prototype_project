import math

def logistic_function(x, initial, L, k = 0.3, x_0 = 25):
    return L / (1 + math.exp(-k * (x - x_0))) + initial

def main() -> None:
    # initial = int(input("initial: "))
    # final = int(input("final: "))

    initial = 5
    final = 240
    print(f"Your parameters: init - {initial.__str__()}, final - {final.__str__()}")

    k = 0.3  # Growth rate, adjust based on desired progression
    x_0 = 25  # Midpoint of the curve



    while True:
        day = int(input("day: "))
        # print(logistic_function(day, initial, final, ))

        from utils import geometric_progression_value
        print(geometric_progression_value(initial, final, day))
        

        # progress_bar = "▓" * (day - 1) + "▒" + "░" * (final - day)
        # print(progress_bar)

if __name__ == "__main__":
    main()