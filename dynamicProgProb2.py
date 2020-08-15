'''
In this problem, we are given an array of coin denominations and a target sum and we need to find the number of ways the target sum can be achieved.
Note that, the number of coins per denomination is unlimited.

The approach here is that, we initialize an array 'ways' with 0s from 1st element to targetAmount element. 0th array element is initialized to 1, since there's only 
one way to make 0 with any number of denominations, and that is, the absence of all denomination coins.

We use the approach:
if denom<amount: ways[amount] = ways[amount] + ways[amount-denom] 
The last element of the ways array, gives the maximum number of ways, the target element can be broken into by the given denominations.


'''
def waysToMakeChange(n = 6,denoms = [1,5]):
    denoms = sorted(denoms)
    ways = [1]
    for i in range(1,n+1):
        ways.append(0)

    
    for denom in denoms:
        for amount in range(1,n+1):
            if denom<=amount:
                ways[amount] = ways[amount] + ways[amount-denom]

        
    return ways[-1]




print(waysToMakeChange())
