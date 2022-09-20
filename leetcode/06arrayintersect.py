
from typing import List
import collections

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    '''
    >>> intersect([1,2,2,1],[2,2])
    [2, 2]
    >>> intersect([4,9,5], [9,4,9,8,4])
    [4, 9]

    '''
    ctr1 = collections.Counter(nums1)
    ctr2 = collections.Counter(nums2)
    
    intersect_list = []
    
    for num in ctr1:
        # if not in ctr2, min will return 0 and array does not get extended
        intersect_list.extend( [num] * min(ctr1[num], ctr2[num]) ) 
            
    return intersect_list

print(intersect([4,9,5], [9,4,9,8,4]))

'''
95%ile in time: 49 ms
50%ile in space: 14.1 mb
'''