import matplotlib.pyplot as plt
import numpy as np
from function_parser import evaluate_function

def plot_graph(function, min_value, max_value, error_callback):
    """
    Plots a graph of the given function over a specified range of x values.

    Args:
        function (str): The function string to plot.
        min_value (float): The minimum value of x.
        max_value (float): The maximum value of x.
        error_callback (callable): A callback function to handle errors during function evaluation.

    Returns:
        None
    """
    # Generate a list of x values evenly spaced between min_value and max_value
    x_values = np.linspace(min_value, max_value, 100)
    y_values = []

    for x in x_values:
        try:
            # Evaluate the function at each x value
            y = evaluate_function(function, x)
            y_values.append(y)
        except Exception as e:
            # Call the error callback function and pass the error message
            error_callback(str(e))
            return

    # Plot the graph
    plt.figure(figsize=(6, 4))
    plt.plot(x_values, y_values, color='blue', linewidth=2.5)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Function Plot', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
