import re


def validate_function(function):
    """
    Validates if a function is well-formed and contains only valid characters.

    Args:
        function (str): The function string to validate.

    Returns:
        bool: True if the function is valid, False otherwise.
    """
    return bool(re.match(r'^([+-/*\d\(\)x\s^]+)$', function))


def evaluate_function(function, x):
    """
    Evaluates a function at a given value of x.

    Args:
        function (str): The function string to evaluate.
        x (float): The value of x to substitute into the function.

    Returns:
        float: The result of evaluating the function at x.

    Raises:
        Exception: If there is an error evaluating the function.
    """
    try:
        # Replace 'x' with the string representation of x and evaluate the function
        return eval(function.replace('x', str(x)))
    except ZeroDivisionError:
        # Handle division by zero error separately
        pass
    except:
        # Raise an exception if there is any other error during evaluation
        raise Exception("Error evaluating the function.")
