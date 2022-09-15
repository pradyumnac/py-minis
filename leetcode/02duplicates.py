from typing import List
def containsDuplicate(nums: List[int]) -> List[int]:
    '''
    >>> containsDuplicate(list(range(65536))+[536])
    True
    '''

    nums_sorted = sorted(nums)
    for num1,num2 in zip(nums_sorted[:-1],nums_sorted[1:]):
        if num1==num2:
            return True
    
    return False


containsDuplicate(list(range(65536))+[536])

