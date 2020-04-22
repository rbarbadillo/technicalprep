def insertionsort(array):
    length = len(array)
    end = array[0]
    for i in range(1, length):
        if array[i] < end:
            x = array.pop(i)
            for j in range(0, i):
                if x < array[j]:
                    array.insert(j, x)
                    break
        end = array[i]
    return array

arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(insertionsort(arr))

