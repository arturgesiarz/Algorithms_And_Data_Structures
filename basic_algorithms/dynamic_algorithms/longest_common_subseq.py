#TIME COMPLEXITY O(N^2),  where n is the size of table
"""
	The longest common subsequence algorithm. To create it, we first create a recursive function f(i), which will be
    calculated the longest common subsequence starting at index i, which means that if it starts at index i, then element i is also taken.
"""
cashe={}
def f(position,A): #O(N)
    if (position) in cashe: return cashe[(position)]
    if position>=len(A): return float('-inf')
    if position==len(A)-1: return 1
    sol=float('-inf')
    getted=False
    for i in range(position+1,len(A)):
        if A[i]>A[position]:
            getted=True
            temp1=f(i,A)+1
            sol=max(sol,temp1)
        if i==len(A)-1 and not getted: return 0 #sytuacja kiedy nie ma eleemntu do wybrania a wiec zwracam 0, bo innej opcji nie moge nic zrobic
    cashe[(position)]=sol
    return sol

def lognest_com_sub(A):
    n=len(A)
    max_sub=float('-inf')
    for i in range(n): #O(N^2)
        act_sub=f(i,A)+1 #O(N) - dlatego +1, ponieaz biore elemnet ktory jest na pozycji i-tej
        if act_sub>max_sub: max_sub=act_sub
    cashe.clear()
    return max_sub

def lognest_com_sub_dp(A):
    n=len(A)
    DP=[1 for _ in range(n)] #tablica oznaczjaca najdluszzy rosnacy podciag zaczynajacy sie w punkcie i-tym a konczy sie na pounkcie n-1-tym, co oznacza ze museze wziasc element i-ty
    for i in range(n-2,-1,-1):
        for j in range(n-1,i,-1):
            if A[i]<A[j]:
                DP[i]=DP[j]+1
    return max(DP)

if __name__ == '__main__':
    A=[2,1,4,3,1,5,2,7,8,3]
    #print(f(0,A[0],A))
    #print(lognest_com_sub(A))
    print(lognest_com_sub_dp(A))
