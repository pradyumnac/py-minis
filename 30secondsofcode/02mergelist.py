'''
lessons: 
list comp if it has if else , put the conditional before iterator
'''

def merge(*args, fill_value = None):
    '''
    merge two lists of unequal length
    >>> merge(['a', 'b'], [1, 2], [True, False]) 
    [['a', 1, True], ['b', 2, False]]
    >>> merge(['a'], [1, 2], [True, False])
    [['a', 1, True], [None, 2, False]]
    >>> merge(['a'], [1, 2], [True, False], fill_value = '_')
    [['a', 1, True], ['_', 2, False]]
    '''

    # max_length = max([len(lst) for lst in args])
    # result = []
    # for i in range(max_length):
    #     result.append([
    #         args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    #     ])
    # return result

    max_length = max([len(lst) for lst in args])
    result = []
    for i in range(max_length):
        result.append([
            args[j][i] if i < len(args[j]) else fill_value for j in range(len(args)) 
        ])
    return result

