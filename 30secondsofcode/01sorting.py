#!/usr/bin/env python



def test_sorted():
    ''' 
    Returns new list which is sorted
    >>> test_sorted()
    ['Albatross', 'Barking Deer', 'Lemur', 'Monkey', 'Zebra', 'lionTiger', 'penguins']
    ['Monkey', 'Zebra', 'Lemur', 'lionTiger', 'Barking Deer', 'penguins', 'Albatross']
    '''

    animal_names = [
        "Monkey",
        "Zebra",
        "Lemur",
        "lion"
        "Tiger",
        "Barking Deer",
        "penguins",
        "Albatross"
    ]

    new_list_sorting = sorted(animal_names)
    print(new_list_sorting)
    print(animal_names)

def test_dotsort():
    ''' 
    Returns None, Sorts inplace
    >>> test_dotsort()
    None
    ['Albatross', 'Barking Deer', 'Lemur', 'Monkey', 'Zebra', 'lionTiger', 'penguins']
    '''
    animal_names = [
        "Monkey",
        "Zebra",
        "Lemur",
        "lion"
        "Tiger",
        "Barking Deer",
        "penguins",
        "Albatross"
    ]

    new_list_dotsort = animal_names.sort()
    print(new_list_dotsort)
    print(animal_names)

