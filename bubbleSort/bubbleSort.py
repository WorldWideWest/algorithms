### PSEUDO CODE ###

# for i in range(array:length):
#   for j in range(0, array:length - i - 1):
#       if array[j] > array[j + 1]:
#           swap(array[j], array[j + 1])
# array[j], array[j + 1] = array[j + 1], array[j]


def sort(array:list) -> list:

    for i in range(len(array)):

        for j in range(0, len(array) - i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            
    return array


array = [3, 5, 1, 8, 5, 4, 7, 6, 9, 0]
print(sort(array))