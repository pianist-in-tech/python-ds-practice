def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    return phrase.capitalize()

print('Python:',capitalize('python') )
print('Only first word:',capitalize('only first word'))