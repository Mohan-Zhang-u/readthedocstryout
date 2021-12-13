"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]

def a_new_func(a, b=1):
    """[summary]

    Args:
        a ([type]): [description]
        b (int, optional): [description]. Defaults to 1.

    Raises:
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    return a + b
