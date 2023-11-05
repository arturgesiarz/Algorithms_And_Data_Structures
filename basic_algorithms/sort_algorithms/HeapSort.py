#TIME COMPLEXITY O(NlogN), where n is the number of size array.

from math import floor

def heapsort(A):
    n=len(A)

    def left(i):  #function returning the index number of the child located on the left in the heap
        return 2*i+1
    def right(i): #function returning the index number of the child located on the right side in the heap
        return 2*i+2
    def parent(i):
        return floor((i-1)/2)

    def heapify(A,i,n): #function to fix invalid heap, assuming the error is only "on one side"
        l=left(i)
        r=right(i)
        max_ind=i
        if l<n and A[l]>A[max_ind]:
            max_ind=l
        if r<n and A[r]>A[max_ind]:
            max_ind=r
        if max_ind!=i: #means that one of two ifs must have happened
            A[i],A[max_ind]=A[max_ind],A[i]
            heapify(A,max_ind,n)

    def buildheap(A):
        for i in range(parent(n-1),-1,-1):
            heapify(A,i,n)

    buildheap(A)

    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,0,i)

    return A

if __name__ == '__main__':
    array=[2,4,2,35,23,53,4,9999,-1]
    print(heapsort(array))

