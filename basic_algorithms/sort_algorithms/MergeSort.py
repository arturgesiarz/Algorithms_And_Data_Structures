#TIME COMPLEXITY O(NlogN), where n is the number of size array.
#MEMORY COMPLEXITY O(N)

import math

def Merge(array1,array2): #merge function, two sorted arrays
    n1=len(array1)
    n2=len(array2)
    new_array=[]
    i=0 #pointer to 1 array
    j=0#pointer to 2 array
    while i<n1 or j<n2: #condition not to go beyond the table
        if i<n1 and j<n2: #the case when no board has ended
            if array1[i]<=array2[j]:
                new_array.append(array1[i])
                i+=1
            else:
                new_array.append(array2[j])
                j+=1
        elif i<n1 and j>=n2: #case when 1 of the boards has run out
            new_array.append(array1[i])
            i += 1
        elif i>=n1 and j<n2: #analogous case
            new_array.append(array2[j])
            j += 1
        else:
            break

    return new_array

def Split(array): #function separating an array into two subarrays of the same length, it will be an equal value for the odd one, otherwise
    n=len(array)
    tab1=[]
    tab2=[]
    for i in range(0,n):
        if i<=math.floor((n-1)/2):
            tab1.append(array[i])
        else:
            tab2.append(array[i])
    return tab1,tab2

def MergeSort(array):
    if len(array)==1: #a single-element array is always ordered
        return array

    left,right=Split(array) #dividing arrays
    left=MergeSort(left) #I keep calling the left one until I get a sorted single-element array
    right=MergeSort(right)

    return Merge(left,right)

if __name__ == '__main__': #test
    tab=[3,7,0,33,40,2,1,-10,500,47]
    print(MergeSort(tab))







