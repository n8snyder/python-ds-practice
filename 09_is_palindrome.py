def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lowercase_phrase = phrase.lower()
    no_space_phrase = lowercase_phrase.replace(" ", "")
    i = len(no_space_phrase) - 1
    for letter in no_space_phrase:
        if i > len(no_space_phrase)/2 and letter is not no_space_phrase[i]:
            return False
        i -= 1   
    return True

    # enumerate 

    # for i, fruit in enumerate(fruits)