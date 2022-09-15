#!/usr/bin/env python

def snip01():
    '''
    >>> snip01()
    42 apples
    num_val=42 str_val='apples'
    num_val % 2 = 0
    'apples'
    6.13
    price_val = 6.13
    Hi apples. Your weight is 42 kgs. Your price is 6.12658.
    
    '''
    str_val = 'apples'
    num_val = 42
    price_val = 6.12658

    print(f'{num_val} {str_val}') # values only

    print(f'{num_val=} {str_val=}') # variable names

    print(f'{num_val % 2 = }') # num_val % 2 = 0

    print(f'{str_val!r}') # 'apples'

    print(f'{price_val:.2f}') # 6.13

    print(f'{price_val = :.2f}') # 6.13

    message = (
        f"Hi {str_val}. "
        f"Your weight is {num_val} kgs. "
        f"Your price is {price_val}."
    ) #  you need to place an f in front of each line of a multiline string
    print(message)

    

def snip02():
    '''
    >>> snip02()
    '\n        Hi apples.\n        Your weight is 42 kgs.\n        Your price is 6.12658.\n    \n'

    '''
    str_val = 'apples'
    num_val = 42
    price_val = 6.12658

    message = f"""
    Hi {str_val}. 
    Your weight is {num_val} kgs. 
    Your price is {price_val}.
    """ # This does not work due to newline chars. See line 13
    print(message)