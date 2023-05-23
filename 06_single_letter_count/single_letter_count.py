def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    word_lower = word.lower()
    return (word_lower.count(letter.lower()))

print ('should be 1',single_letter_count('Hello World', 'h') )
print ('should be 0',single_letter_count('Hello World', 'z') )