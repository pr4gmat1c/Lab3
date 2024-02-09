def prime(numbers):
    result = []
    for x in numbers:
        i = 2
        x = int(x)
        if x <= 1:
            continue
        while x % i != 0:
            i += 1
        if i == x:
            result.append(x)
    return result



