#TIME COMPLEXITY O(d*(n+k)), when d is the number of digits in the given list, n is the number of elements in the list, k the number of different values ​​it can take
"""
RadixSort is sorting from the least significant digit to the most significant, it can be interpreted this way.
To use it, we must use a stable sort, which can be, for example, coutingsort.
Radix Sort is worth using when we want to sort strings of the same length or numbers of the same width.
"""

def countingsort(array,digit_nr):  #k - the upper range of our numbers, of course we assume that we can sort integers here from 1 to k inclusive!
    n=len(array)
    arrayB=[0]*10 
    arrayC=[0]*n
    for i in range(n):
        m=len(str(array[i]))
        if m<digit_nr+1:
            real_digit = 0
        else:
            digit=str(array[i])[m-1-digit_nr]
            real_digit=int(digit)
        arrayB[real_digit]+=1
    for i in range(1,10):
        arrayB[i]=arrayB[i-1]+arrayB[i]
    for i in range(n-1,-1,-1):
        m = len(str(array[i]))
        if m<digit_nr+1:
            real_digit = 0
        else:
            digit=str(array[i])[m-1-digit_nr]
            real_digit=int(digit)
        arrayC[arrayB[real_digit]-1]=array[i]  #we compare this to our main number
        arrayB[real_digit]-=1
    print(arrayC)
    return arrayC
def radixsort(array,d): 
    for i in range(d): 
        array=countingsort(array,i)
    return array

def countingsort_words(array,digit_nr): 
    n=len(array)
    arrayB=[0]*26 
    arrayC=[0]*n
    for i in range(n):
        m=len(array[i])
        if m<digit_nr+1:
            real_letter = 97
        else:
            digit=array[i][m-1-digit_nr]
            real_letter=ord(digit)
        arrayB[real_letter-97]+=1
    for i in range(1,26):
        arrayB[i]=arrayB[i-1]+arrayB[i]
    for i in range(n-1,-1,-1):
        m = len(array[i])
        if m<digit_nr+1:
            real_letter = 97
        else:
            digit=(array[i])[m-1-digit_nr]
            real_letter=ord(digit)
        arrayC[arrayB[real_letter-97]-1]=array[i] 
        arrayB[real_letter-97]-=1
    print(arrayC)
    return arrayC

def radixsort_words(array,d): 
    for i in range(d): 
        array=countingsort_words(array,i)
    return array


if __name__ == '__main__': #
    tab=["cat","dog","sun","eat","fun"]
    print(radixsort_words(tab,3))


