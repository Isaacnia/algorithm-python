def selection_sort(array):
    temp = array.copy()
    for x in range(0,len(temp)-1):
        index = x
        for y in range(x+1,len(temp)):
            if temp[index]>=temp[y]:
                index = y
        if x != index :
            t = temp[index]
            temp[index] = temp[x]
            temp[x] = t       
    return temp
