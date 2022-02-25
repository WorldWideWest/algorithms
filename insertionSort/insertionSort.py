array = [5, 4, 12, 5, 7, 1, 3, 7]

### PSEUDO CODE ###

# for i in range(1, array:length)
#   j = i
#   while j > 0  and  array[j - 1] > array[j]
#       swap array[j - 1], array[j]
#       j -= 1


def sort(array:list) -> list:

    for i in range(1, len(array)):

        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array

print(sort(array))