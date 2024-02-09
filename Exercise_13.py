import random


def guess():
    name = input("Hello! What is your name?\n")
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    randnum = random.randint(1, 20)
    print("Take a guess.")
    x = input()
    x = int(x)
    cnt = 1
    while x != randnum:
        if x > randnum:
            print("Your guess is too high.")
        elif x < randnum:
            print("Your guess is too low.")
        cnt += 1
        print("Take a guess.")
        x = input()
        x = int(x)
    if cnt == 1:
        print("Good job, " + name + "! You guessed my number in", cnt, "guess!")
    else:
        print("Good job, " + name + "! You guessed my number in", cnt, "guesses!")


