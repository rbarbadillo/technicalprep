
def selectionsort(array):
  length = len(array)
  for i in range(0, length):
    smallest = array[i]
    index = i
    for j in range(i+1, length):
      if array[j] < smallest:
        index = j
        smallest = array[j]
    array[i], array[index] = array[index], array[i]
  return array

array = [100, 89, 12312, 1, 0, -1]
print(selectionsort(array))
