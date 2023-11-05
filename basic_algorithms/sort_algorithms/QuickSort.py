#TIME COMPLEXITY O(NlogN),  where n is the number of size array.
"""
The time complexity may also be O(N^2), in the worst case when the elements at the start are sorted opposite to the obtained result or something like that. Although the better complexity is still given.
"""
def partition(array,p,r):
    x=array[p]
    i=p
    j=r
    while True:
        while array[i]<x: #we are looking for the first element that does not satisfy this property
            i+=1
        while array[j]>x:
            j-=1
        if i<j: #means that we have to replace both of these elements
            array[i],array[j]=array[j],array[i]
        else:
            return j #means that we will loop so we finish executing the program
        i+=1 #after each successful replacement operation, I move my pointers by next positions so that subsequent elements can be compared
        j-=1

def quicksort(array,p,r):
    if p<r:
        q=partition(array,p,r)
        quicksort(array,p,q)
        quicksort(array,q+1,r)
    return array

if __name__ == '__main__': #test
    array=[0,5,4,3,450,3,2,9,0,2]
    quicksort(array,0,len(array)-1)
    print(array)
