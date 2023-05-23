def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    set1 = set(l1)
    set2 = set(l2)
    new_set = set1.intersection(set2)
    inter_list = list(new_set)

    return inter_list

print('[2, 3]', intersection([1, 2, 3], [2, 3, 4])) 
print('[1, 2, 3]', intersection([1, 2, 3], [1, 2, 3, 4])) 
print(' []', intersection([1, 2, 3], [4, 5, 6])) 