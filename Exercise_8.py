def spy_game(nums):
    nem = []
    for x in nums:
        if int(x) == 0 or int(x) == 7:
            nem.append(int(x))
    print(nem)

    for i in range(len(nem) - 2):
        if nem[i] == 0 and nem[i + 1] == 0 and nem[i + 2] == 7:
            print("True")
            return
    print("False")



