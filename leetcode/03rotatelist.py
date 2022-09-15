from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    >>> rotate([1,2,3,4,5,6,7,8], 5)
    [4, 5, 6, 7, 8, 1, 2, 3]
    >>> rotate([1,2,3,4,5,6,7], 3)
    [5, 6, 7, 1, 2, 3, 4]
    >>> rotate([-1,-100,3,99], 2)
    [3, 99, -1, -100]
    
    """
    # Low memory, 
    while(k>0):
        nums.insert(0, nums.pop())
        k-=1


    '''
    The following solution is not in place
    # fast exec
    n = len(nums)
    nums[:]=nums[-1*k%n:]+nums[:(n-k)%n]
    
    '''

    print(nums)

rotate([1,2,3,4,5,6,7,8], 5)