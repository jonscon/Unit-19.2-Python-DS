def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    >>> reverse_vowels("aeiou")
    'uoiea'

    >>> reverse_vowels("why try, shy fly?")
    'why try, shy fly?'
    """

    vowels = "aeiouAEIOU"
    storage = []
    characters = list(s)
    
    # If character is a vowel, add index of vowel and vowel in storage as a tuple 
    for i in range(len(characters)):
        if characters[i] in vowels:
            storage.append((i, characters[i]))
    
    # Swap vowels
    for i in range(len(storage) // 2):
        characters[storage[i][0]], characters[storage[-1 - i][0]] = storage[-1 - i][1], storage[i][1]
    
    return ''.join(characters)

    # Another way to swap vowels: Comma Assignment
    # characters[i], characters[j] = characters[j], characters[i]