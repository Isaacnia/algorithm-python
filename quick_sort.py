def partition(array,lb,ub):
    pivot = array[lb]
    l = lb
    r = ub
    while l<r:
         while pivot >= array[l] and l<ub:
            l += 1
         while pivot < array[r]:
            r -= 1
         if l<r :
            t = array[r]
            array[r] = array[l]
            array[l] = t
    array[lb] = array[r]
    array[r] = pivot
    return r
def quick(array,lb,ub):
    j = 0
    if lb<ub:
         j = partition(array,lb,ub)
         quick(array,lb,j-1)
         quick(array,j+1,ub)
            
def quick_sort(array):
    lb = 0
    ub = len(array)-1
    quick(array,lb,ub)
