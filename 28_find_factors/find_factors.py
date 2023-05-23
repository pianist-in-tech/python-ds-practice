def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    num_factors = [];
    numbers = range(1,num // 2+1); 
    for factor in numbers:
        print (factor);
        if num % factor == 0:
            num_factors.append(factor);
    num_factors.append(num);
    return num_factors;

print('[1, 2, 5, 10]', find_factors(10))