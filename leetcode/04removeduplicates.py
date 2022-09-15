from typing import List
def removeDuplicates(nums: List[int]) -> int:
    '''
    Non decreasing
    Avoiding pop saved a lot of time
    75%ile Time Comp
    65%ile space comp
    >>> removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    5
    >>> removeDuplicates([1,1,2])
    2
    >>> removeDuplicates([0, 5, 5, 5, 5, 5, 5])
    2
    
    '''
    
    list_len: int = len(nums)
    last_used_idx = 0
    if list_len>1:
        idx = 0
        while idx<list_len-1:
            if nums[idx] != nums[(idx+1)]:
                last_used_idx+=1
                nums[last_used_idx] = nums[(idx+1)]
            idx+=1
    else:
        return len(nums)
    nums=nums[:last_used_idx+1]
    return len(nums)

removeDuplicates([0,0,1,1,1,2,2,3,3,4])