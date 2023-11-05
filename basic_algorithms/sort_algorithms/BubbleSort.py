#TIME COMPLEXITY O(N^2), where n is the number of size array.
"""
BubbleSort - bubble sorting, we walk around the board and compare subsequent elements,
    we replace the larger one with the smaller one
"""


def BubbleSort(array):
    n=len(array)
    print(array)
    for i in range(0,n):
        for j in range(0,n-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
            print(array)
    return array

if __name__ == '__main__': #test
    array=[2,4,4,0,0,2938,583,1202,2,-1]
    print(BubbleSort(array))
