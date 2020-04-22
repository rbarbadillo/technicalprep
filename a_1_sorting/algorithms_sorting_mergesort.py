# As found here: https://github.com/theja-m/Data-Structures-and-Algorithms/blob/master/Sorting/Merge%20sort.py
arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def mergesort(array):
    length = len(array)
    # Define base case
    if length == 1:
        return array
    mid = length // 2
    left = array[:mid]
    right = array[mid:]
    print('                               Dividing')
    print('Left {}'.format(left))
    print('Right {}'.format(right))
    return merge(mergesort(left), mergesort(right))


def merge(left, right):
    result = []
    leftindex = 0
    rightindex = 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1
    result = result + left[leftindex:] + right[rightindex:]
    print('                                Merging')
    print(left, right)
    print(result)
    return result


x = mergesort(arr)
print(x)
