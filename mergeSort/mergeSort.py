def sort(array:list) -> list:

    if len(array) > 1:

        mid = len(array)//2
        left, right = array[:mid], array[mid:]
        
        # Recursion
        sort(left), sort(right)

        # Mergin
        i, j, k = 0, 0, 0 
        # i - left index array
        # j - right index array
        # k - merged index array


        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array

array = [1320, 1503, 2067, 1116, 533]
print(sort(array))