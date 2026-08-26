from functions.random_city.lambda_function import lambda_handler


def test_random_city_returns_string():
    result = lambda_handler({}, {})
    assert isinstance(result, str)
