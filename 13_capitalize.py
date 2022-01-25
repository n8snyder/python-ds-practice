def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

    >>> capitalize('python')
    'Python'

    >>> capitalize('only first word')
    'Only first word'
    """
    first_letter = phrase[0]
    return first_letter.upper() + phrase[1:]
