def has_33(nums):
    cnt = 0
    flag = 0
    for x in nums:
        x = int(x)
        if x == 3:
            cnt += 1
        elif x != 3:
            cnt = 0
        if cnt == 2:
            flag = 1
    if flag == 1:
        print("True")
    else:
        print("False")



