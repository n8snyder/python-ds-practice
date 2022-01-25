def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    reverse_case_string = ""

    for letter in phrase:
        if letter.lower() != to_swap.lower():
            reverse_case_string += letter
        elif letter.islower():
            reverse_case_string += letter.upper()
        elif letter.isupper():
            reverse_case_string += letter.lower()    
        
    return reverse_case_string