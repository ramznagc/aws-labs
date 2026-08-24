from random import randint


ROMAN_SYMBOLS = (
    "M", "CM", "D", "CD", "C", "XC", "L",
    "XL", "X", "IX", "V", "IV", "I",
)
ROMAN_VALUES = (
    1000, 900, 500, 400, 100, 90, 50,
    40, 10, 9, 5, 4, 1,
)


def to_roman(number: int) -> str:
    """Convert a positive integer to Roman numerals."""
    result = []

    for symbol, value in zip(ROMAN_SYMBOLS, ROMAN_VALUES):
        while number >= value:
            number -= value
            result.append(symbol)

    return "".join(result)


def lambda_handler(event, context):
    number = randint(1, 3999)
    return f"Roman Representation of the {number} is {to_roman(number)}"
