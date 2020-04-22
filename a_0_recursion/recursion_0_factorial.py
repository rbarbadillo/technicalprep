def factorialRecursive(num):
    if num == 1:
        return 1
    return num * factorialRecursive(num-1)


def factorialIterative(num):
    result = 1
    for i in range(1, num + 1):
        result = result*i
    return result


print(factorialRecursive(3))
