def fibonacciRecursive(n):
    if n < 2:
        return n
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n-2)


for i in range(0, 10):
    print(fibonacciRecursive(i))


def fibonacciIterative(n):
    result = 0
    aux = 1
    secondAux = 1
    for i in range(0, n):
        secondAux = result
        result = result + aux
        aux = secondAux
    return result


for i in range(1, 10):
    print(fibonacciIterative(i))
