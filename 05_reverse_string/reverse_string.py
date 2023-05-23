def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    return (phrase[::-1])

print ('should be emosewa:', reverse_string('awesome'))
print ('should be ecuas:', reverse_string('sauce'))