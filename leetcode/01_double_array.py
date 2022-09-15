from typing import List
from collections import Counter

def findOriginalArray(changed: List[int]) -> List[int]:
    '''
    >>> findOriginalArray([1,3,4,2,6,8])
    [1, 3, 4]
    >>> findOriginalArray([1,3,4,2,6])
    []
    >>> findOriginalArray([6,3,0,1])
    []
    >>> findOriginalArray([6000,32,1578889,64,3157778, 12000])
    [32, 6000, 1578889]
    >>> findOriginalArray([34,1,5,2,4,2,8,17,16, 10])
    [1, 2, 5, 8, 17]
    >>> findOriginalArray([6,3,6,3,444,888,99,198])
    [3, 3, 99, 444]
    >>> findOriginalArray([1,2,3,2,4,6,2,4,6,4,8,12])
    [1, 2, 2, 3, 4, 6]
    '''

    # Odd no of elemsn cant be double array
    # Empty can be a double array but uin that case an empty will be returned itself
    lst_length = len(changed)
    if lst_length == 0 or lst_length%2!=0:
        return []

    ctr  = Counter(changed)
    lst_ans = []

    for i in sorted(changed):        
        if ctr[i] == 0 :
            # accounted for doubles
            pass
        elif ctr[2*i] < ctr[i]:
            # Doubles count atleast equal to singles 
            # More may be possible, see "> clause"
            return []
        elif ctr[2*i] == ctr[i]:
            # Pairs are accounted for, 
            # Remove tracking count for both, 
            ctr[2*i] -= 1
            ctr[i] -= 1 # unnecessary, written for readability
            lst_ans.append(i)
        elif ctr[2*i] > ctr[i]:
            # Remove the doubles for which singles are present #accounedfor
            ctr[2*i] -= 1
            ctr[i] -= 1 # unnecessary, written for readability
            lst_ans.append(i)

    return lst_ans


# findOriginalArray([34,1,5,2,4,2,8,17,16,10])
# findOriginalArray([6,3,6,3,444,888,99,198])


