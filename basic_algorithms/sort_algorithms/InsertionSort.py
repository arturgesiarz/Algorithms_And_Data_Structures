#TIME COMPLEXITY O(N^2), where n is the number of size array.
"""
IntsertionSort is insertion sort, which means that we treat our array more or less as a deck of cards.
    the first thing we do is set our first element as the second one and compare it to the position of this element at the very beginning
    array, and if any element is larger than it, we move our element to the left.
    We do this until the compared elements are greater or equal, or the array runs out.
    It is a stable algorithm - it does not change elements that have the same number.
"""
def InsertionSort(array):
    n=len(array)
    element=0
    for i in range(1,n):
        element=array[i]
        j=i-1
        while array[j]>array[j+1] and j>=0: #we go backwards until we encounter a value smaller than our element
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
            j-=1
    return array
if __name__ == '__main__':
    tab=[10,5,-10,-10,80,2,4,3]
    print(InsertionSort(tab))
