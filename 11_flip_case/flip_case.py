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
    flipped = ""

    for char in phrase:
        if to_swap == char.lower():
            char = char.swapcase()
        flipped += char
    return flipped




