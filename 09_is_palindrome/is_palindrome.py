def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    the_phrase = phrase.lower()
    if len(the_phrase.split()) > 1:
        the_phrase = the_phrase.replace(" ", "")

    if the_phrase == the_phrase[::-1]:
        return True
    else: 
        return False

print('True:', is_palindrome('tacocat'))
print('True:', is_palindrome('noon'))
print('False:', is_palindrome('robert'))
print('True:', is_palindrome('taco cat'))
print('True:', is_palindrome('Noon'))