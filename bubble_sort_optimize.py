def bubble_sort_optimize(a):
    array = a.copy()
    flag = True #O(n) swap for sorted array
    for x in range(0,len(array)):
        if flag:
            flag = False
            for y in range(0,len(array)-(1+x)):
                if array[y]>array[y+1]:
                    temp = array[y+1]
                    array[y+1] = array[y]
                    array[y] = temp
                    flag = True
        else :
            break
    return array
