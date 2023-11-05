#TIME COMPLEXITY O(n*p), where n is the number of objects and p is the weight I can carry
"""
 This is an algorithm of the 0/1 backpack problem - it means that we either take a given item or not based on given criteria, namely:
    There is a given number of maximum kilograms that a thief cannot carry, as well as the prices of given items and their weight.
    We want to earn as much as possible, without exceeding the maximum amount we can handle.

    We will define the function f(i,act_kilos), which means that we can take items from the <i-th,n-th> with the current number of kilos we have left,
    For such arguments, the function returns the maximum amount that we can steal.
"""

cashe={}
def f(position,act_kilos,weigh_tab,price_tab):
    if (position,act_kilos) in cashe: return cashe[(position,act_kilos)]
    if position==len(weigh_tab)-1:
        if act_kilos - weigh_tab[position] >= 0: return price_tab[position]
        else: return 0
    sol=float('-inf')
    if act_kilos-weigh_tab[position]>=0:
        temp1=f(position+1,act_kilos-weigh_tab[position],weigh_tab,price_tab)+price_tab[position]
        sol=max(sol,temp1)
    temp2=f(position+1,act_kilos,weigh_tab,price_tab)
    sol=max(sol,temp2)
    cashe[(position, act_kilos)]=sol
    return sol

def knapsack_dp(W,P,k): #O(n*p), gdzie n to ilosc przedmiotw, a p to waga jaka jestem w stanie uniesc
    n=len(W)
    DP=[[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,k+1): #aktualny stan naszych kilogramow jakie jestesmy ze soba w stanie wziasc
            if W[i-1]>j: #spradzam czy jestesmy w stanie uniesc aktualnie przegladany przedmiot
                DP[i][j]=max(DP[i-1][j],DP[i][j-1])
            else: #znaczy to ze jestesmy wstanie go uniesc W[i]<=j
                rest_weight=j-W[i-1]
                DP[i][j]=max(DP[i-1][j],DP[i][j-1],DP[i-1][rest_weight]+P[i-1])
    return DP[n][k]

if __name__ == '__main__':
    W=[8,7,5]
    P=[3,2,4]
    k=15
    print(knapsack_dp(W,P,k))
