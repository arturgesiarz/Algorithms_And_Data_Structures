#TIME COMPLEXITY AVERGE O(N+K), 
#TIME COMEXITY WORST O(N^2),  where n is the number of size array, and k is the number of buckets.
"""
	Using bucketsort makes sense when we have evenly distributed data.
"""

def countingsort_words(array,digit_nr): #k-the upper range of our numbers, of course we assume that we can sort integers here from 1 to k inclusive!
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
        arrayC[arrayB[real_letter-97]-1]=array[i] #we compare this with our main number
        arrayB[real_letter-97]-=1
    print(arrayC)
    return arrayC

def bucketsort(array):
    n=len(array)
    top_range=max(array)
    field=top_range+1 #the number of our buckets, we add 1 to account for 0
    buckets=[ 0 for _ in range(field)]
    counter=0
    for i in range(n):
        buckets[array[i]]+=1
    for i in range(field):
        while buckets[i]>0:
            array[counter]=i
            buckets[i]-=1
            counter+=1
    return array

def radixsort_words(array,d): #radixsortCS - counting sort is used here
    for i in range(d): # 0 1 2
        array=countingsort_words(array,i)
    return array

def bucketsort_string(array): #we sort subtitles
    n=len(array)
    top_range = max([len(n) for n in array])
    field=top_range+1
    buckets=[ [] for _ in range(field)]
    counter=0
    marker=0
    for i in range(n):
        buckets[len(array[i])].append(array[i]) #this is where additional sorting should occur, buckets
    for i in range(field):
        buckets[i]=radixsort_words(buckets[i],top_range)
    for i in range(field):
        counter=len(buckets[i])
        while counter>0:
            array[marker]=buckets[i][len(buckets[i])-counter]
            counter-=1
            marker+=1
    return array

def bucketsort_word(word):
    n=len(word)
    buckets=[ 0 for _ in range(26)]
    new_word=""
    for i in range(n):
        buckets[ord(word[i])-97]+=1
    for i in range(26):
        while buckets[i]>0:
            new_word+=chr(i+97)
            buckets[i]-=1
    return new_word

if __name__ == '__main__':  #test
    tab = ["pies", "siep", "kot", "tok", "pies", "kupa"]
    print(bucketsort_string(tab))
