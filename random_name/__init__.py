import random

from dictionaries import ADJECTIVES, COLORS, ANIMALS


def generate_name(repeat_parts=False, separator='-',
                  lists=(ADJECTIVES, COLORS, ANIMALS)):
    """ Generates a single random name.

    :type repeat_parts: bool
    :param repeat_parts: If set, do not ensure that each part of the name
                         is unique to the name itself.

    :type separator: str
    :param separator: The string that is used to join each part of the name.

    :type lists: list of lists
    :param lists: A list of dictionary lists that will be used for each
                  part of the name. One word is chosen from each list in
                  order.
    """
    name = []
    for l in lists:
        part = None
        while not part or (part in name and not repeat_parts):
            part = random.choice(l)
        name.append(part)
    return separator.join(name)


def generate(count=1, repeat_parts=False, unique_list=True, separator='-',
             lists=(ADJECTIVES, COLORS, ANIMALS)):
    """ Generates a list of random names.

    :type count: int
    :param count: The number of names to generate.

    :type repeat_parts: bool
    :param repeat_parts: If set, do not ensure that each part of the name
                         is unique to the name itself.

    :type unique_list: bool
    :param unique_list: If True, ensures that each name in the list is unique.

    :type separator: str
    :param separator: The string that is used to join each part of the name.

    :type lists: list of lists
    :param lists: A list of dictionary lists that will be used for each
                  part of the name. One word is chosen from each list in
                  order.
    """
    names = []
    for i in range(count):
        name = None
        while not name or (name in names and not unique_list):
            name = generate_name(repeat_parts, separator, lists)
        names.append(name)
    return names
