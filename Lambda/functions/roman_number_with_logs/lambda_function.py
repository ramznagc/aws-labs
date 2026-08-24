import logging

from random import randint


logger = logging.getLogger()
logger.setLevel(logging.INFO)

ROMAN_SYMBOLS = (
    "M", "CM", "D", "CD", "C", "XC", "L",
    "XL", "X", "IX", "V", "IV", "I",
)
ROMAN_VALUES = (
    1000, 900, 500, 400, 100, 90, 50,
    40, 10, 9, 5, 4, 1,
)


def lambda_handler(event, context):
    logger.info("Lambda handler started")
    logger.info("Incoming event: %s", event)

    number = randint(1, 3999)
    logger.info("Generated random number: %s", number)

    remaining = number
    roman_value = ""

    for symbol, value in zip(ROMAN_SYMBOLS, ROMAN_VALUES):
        while remaining >= value:
            remaining -= value
            roman_value += symbol
            logger.info(
                "Matched %s, remaining=%s, current_roman=%s",
                value,
                remaining,
                roman_value,
            )

    logger.info(
        "Final Roman result for %s: %s",
        number,
        roman_value,
    )

    return {
        "statusCode": 200,
        "body": f"Roman Representation of the {number} is {roman_value}",
    }
