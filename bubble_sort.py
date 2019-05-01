def bubble_sort(a):
    array = a.copy()
    for x in range(0,len(array)):
        for y in range(0,len(array)-(1+x)):
            if array[y]>array[y+1]:
                temp = array[y+1]
                array[y+1] = array[y]
                array[y] = temp
    return array
