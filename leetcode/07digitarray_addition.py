from typing import List

def plusOne(digits: List[int]) -> List[int]:
    '''
    >>> plusOne([3,9,9,9])
    [4, 0, 0, 0]
    >>> plusOne([1,0,0,0])
    [1, 0, 0, 1]
    >>> plusOne([9])
    [1, 0]
    '''
    result_list = []
    carry = 0 
    increment_lsb_val=1
    
    for i in range(len(digits)-1, -1, -1):  # from last to 0 index
        sum_digit = (digits[i]+carry+increment_lsb_val) % 10
        carry = (digits[i]+carry+increment_lsb_val) // 10
        increment_lsb_val = 0
        result_list.append(sum_digit)
    if carry!=0: 
        result_list.append(carry)
        
    return list(reversed(result_list))

# print(plusOne([9]))

'''
18%ile time comp Runtime: 66 ms
Memory Usage: 13.9 MB

'''

def plusOneBetter(digits: List[int]) -> List[int]:
    '''
    >>> plusOneBetter([3,9,9,9])
    [4, 0, 0, 0]
    >>> plusOneBetter([1,0,0,0])
    [1, 0, 0, 1]
    >>> plusOneBetter([9])
    [1, 0]
    '''
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]

def plusOneRecursive(digits):
    '''
    :type digits: List[int]
    :rtype: List[int]

    >>> plusOneRecursive([3,9,9,9])
    [4, 0, 0, 0]
    >>> plusOneRecursive([1,0,0,0])
    [1, 0, 0, 1]
    >>> plusOneRecursive([9])
    [1, 0]
    '''
    if len(digits) == 1 and digits[0] == 9:
        return [1, 0]

    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    else:
        digits[-1] = 0
        digits[:-1] = plusOneRecursive(digits[:-1])
        return digits  

    digits.re