def compute() -> int:
    '''

    Returns:

        The counterweight to be removed in grams (a number).
    '''
    first_element = 23
    second_element = 42
    vitruvian = [first_element, second_element]
    count = 50
    while count > 0:
        result = first_element + second_element
        if result%2 == 0:
            result -= 1
        vitruvian.append(result)
        first_element = second_element
        second_element = result
        count -= 1
    return vitruvian