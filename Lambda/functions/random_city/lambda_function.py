from random import choice


CITIES = [
    "Berlin",
    "London",
    "Athens",
    "New York",
    "Istanbul",
    "Ankara",
    "Brussels",
    "Paris",
    "Cape Town",
]


def lambda_handler(event, context):
    """Return a random city."""
    return choice(CITIES)
