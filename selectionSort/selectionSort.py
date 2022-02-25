
### PSEUDO CODE ###
# for i in range(array:length)
#   minIndex = i
#       for j in range(i + 1, array:length)
#           if array[minIndex] > array[j]
#               minIndex = j
#       swap(array[i], array[minIndex])


def sort(array:list) -> list:

    for i in range(len(array)):

        minIndex = i
        
        for j in range(i + 1, len(array)):
            if array[minIndex] > array[j]: minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]

    return array


array = [3, 5, 1, 8, 5, 4, 7, 6, 9, 0]
print(sort(array))