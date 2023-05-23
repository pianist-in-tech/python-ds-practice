def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap = to_swap.lower()
    updated_phrase = ''
    for letter in phrase:
        if letter.lower() == to_swap:
            letter = letter.swapcase()
        updated_phrase += letter
    return updated_phrase
        
print('aAAAhhh:',flip_case('Aaaahhh', 'a'))
print('aAAAhhh:',flip_case('Aaaahhh', 'A'))
print('AaaaHHH:',flip_case('Aaaahhh', 'h'))