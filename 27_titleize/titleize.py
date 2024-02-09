def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    
    # Built-in Title Method
    return phrase.title()

    # Long Way
    # return ' '.join([word.capitalize() for word in phrase.split(' ')])