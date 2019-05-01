def insertion_sort(a):
    array = a.copy()
    size = len(array)
    for x in range(1,size):
        y = array[x]
        z = x-1
        while y<array[z]:
            array[z+1] = array[z]
            z -= 1
            if z<0 :
                break
        array[z+1]=y
    return array

                
            
