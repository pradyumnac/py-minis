from typing import List
from functools import reduce
# 
def singleNumberMyImplementation(nums: List[int]) -> int:
    '''
    >>> singleNumberUsingReduce([2,2,1])
    1
    >>> singleNumberUsingReduce([4,1,2,1,2])
    4
    >>> singleNumberUsingReduce([1])
    1
    '''
    duplicates = {}
    
    for num in nums:
        if num in duplicates.keys():
            duplicates[num] = duplicates[num] + 1
        else:
            duplicates[num] = 1
            
    for num, count in duplicates.items():
        if count == 1:
            return num
    
    # No non duplicates
    return None


def singleNumberUsingReduce(nums: List[int]) -> int:
    '''
    >>> singleNumberUsingReduce([2,2,1])
    1
    >>> singleNumberUsingReduce([4,1,2,1,2])
    4
    >>> singleNumberUsingReduce([1])
    1
    '''


    return reduce(lambda total, el: total ^ el ,nums)