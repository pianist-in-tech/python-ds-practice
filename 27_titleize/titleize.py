def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    cap_prase = [];
    updated_prase = '';
    phrase = phrase.lower();
    words_in_phrase = phrase.split();
    for word in words_in_phrase:
        cap_prase.append(word.capitalize());
    updated_prase = " ".join(cap_prase)

    return updated_prase; 

print('This Is Awesome', titleize('this is awesome'))

