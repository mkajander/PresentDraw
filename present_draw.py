import random
import sys


def draw_pair(givers, receivers):
    while len(receivers) > 1:
        # Randomly select a giver and a receiver where receiver can't be the same as giver.
        wait_input = input("Press Enter to draw.")
        giver = random.choice(givers)
        receiver = random.choice(receivers)
        while receiver == giver:
            receiver = random.choice(receivers)
        # Remove the giver and receiver from the list.
        givers.remove(giver)
        receivers.remove(receiver)
        # Print the pair.
        print(f"{giver} gives a present to {receiver}.")
    # Print the last pair.
    print("Finally:")
    print(f"{givers[0]} gives a present to {receivers[0]}.")
    input("Press Enter to close.")


def main():
    # If no arguments are given prompt the user for the names space separated.
    if len(sys.argv) == 1:
        try:
            names = input("Enter the names of the people: ").split()
        except EOFError:
            print("No names given.")
            return -1
    else:
        names = sys.argv[1:]

    # If there are less than 2 names, there is no point in running the program.
    if len(names) < 2:
        print("Not enough names given.")
        # print usage
        return -1
    else:
        givers = names[:]
        receivers = names[:]
        draw_pair(givers, receivers)
    return 0


if __name__ == "__main__":
    sys.exit(main())
