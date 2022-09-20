from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    >>> moveZeroes([0,1,0,3,12])
    [1, 3, 12, 0, 0]
    >>> moveZeroes([0])
    [0]
    """
    index = 0
    no_of_zeroes = 0 # no of 0s inserted
    list_len = len(nums)

    if not 0 in nums:
        return nums
    try:
        while(index < len(nums)):
            ''' each time loop runs means, 1 "0" gets moved
            start ignoring the inserted 0s
            '''   
            nums.remove(0) # ignoring the inserted 0s
            nums.append(0) 
            no_of_zeroes += 1 #
            index+=1
    except ValueError:
        # return nums # No more zeroes left
        return nums
    
moveZeroes([0,1,0,3,12])