from itertools import permutations
def permut(str):
    p = permutations(str)
    for j in list(p):
        print("".join(j))


