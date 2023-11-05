#TIME COMPLEXITY O(N^2), n is the number of elements in the list
"""
SelectionSort consists in searching for the smallest element and swapping places with the first element
   """

def SelectSort(array):
    n=len(array)
    min_local=0
    min_local_id=0
    min_temporary=0
    for i in range(0,n):
        min_local = array[i]
        min_local_id = i
        min_temporary=0
        for j in range(i,n):
            if array[j]<min_local:
                min_local=array[j]
                min_local_id = j
        array[i],array[min_local_id]=array[min_local_id],array[i]
    return array

if __name__ == '__main__': #test
    array=[1,5,4,0,-1,234,9,7,523]
    print(SelectSort(array))



