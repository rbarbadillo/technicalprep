numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubblesort(array):
    notSorted = True
    while notSorted:
        notSorted = False
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                aux = array[i]
                array[i] = array[i + 1]
                array[i + 1] = aux
                notSorted = True
    return array

print(bubblesort(numbers))
