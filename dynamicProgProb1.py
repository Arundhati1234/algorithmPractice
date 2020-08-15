'''
In this question, we are given an array of integers and we need to calculate the maximum sum that can be generated, without including adjacent elements.
This is a problem of dynamic programming.

The approach will be to make another array maxSum which includes the maximum sum of non-adjacent elements, up till the given index.
The formula we can apply here can be

maxSum[i] = max(maxSum[i-1], maxSum[i-2] + array[i])
Note that, we need to initialize maxSum[0] = array[0] and maxSum[1] = max(array[0],array[1])

'''

def calculateMaxSum(array=[7,10,12,7,9,14]):

    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return max(array[0],array[1])
    else:
        maxSum = [array[0],max(array[0],array[1])]
        for i in range(2,len(array)):
            maxSum.append(max(maxSum[i-1],maxSum[i-2]+array[i]))

    return(maxSum[len(maxSum)-1])








print(calculateMaxSum())
