def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    lst = []
    for char in parens:
        if char == '(':
            lst.append(char)
        elif char == ')':
            if len(lst) == 0:
                return False
            lst.pop()
    return len(lst) == 0
    
