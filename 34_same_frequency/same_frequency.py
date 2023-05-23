def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_digits = str(num1)
    num2_digits = str(num2)
    
    for digit in num1_digits:
        if num1_digits.count(digit) != num2_digits.count(digit):
            return False
    return True