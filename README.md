# Plotify
This is a Python GUI program that allows users to plot arbitrary mathematical functions. It provides a simple and beautiful graphical interface for inputting the function, specifying the range of x values, and displaying the plotted graph using Matplotlib. The program utilizes the Pyside2 library for the GUI and integrates the Matplotlib figure within the application.

## Requirements

To run this program, make sure you have the following requirements met:

1. Python 3.11 installed on your machine.
2. Pyside2 library installed. You can install it using `pip install pyside6`.
3. Matplotlib library installed. You can install it using `pip install matplotlib`.
4. pytest and pytest-qt libraries installed for running automated tests. You can install them using `pip install pytest pytest-qt`.

## Usage

1. Clone this repository to your local machine or download the source code.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to start the program:

```shell
python plotify.py
```
1. The program will launch, displaying a graphical user interface.
2. Enter your mathematical function in the provided input field. For example, you can enter 5*x^3 + 2*x. The following operators are supported: + - / * ^.
3. Specify the minimum and maximum values of x in their respective input fields.
4. Click the "Plot" button to generate the graph.
5. The graph will be displayed in the application window.
## Input Validation
The program applies appropriate input validation to ensure that the user input is correct. It performs the following validations:

- Checks if the function is syntactically valid.
- Verifies that the minimum and maximum values of x are valid numeric inputs.
- Displays error messages to the user if any of the validations fail, explaining the issue.
## Automated Tests
This repository includes automated tests to verify the correctness of the program's main features. The tests are implemented using pytest and pytest-qt libraries. To run the tests, follow these steps:

1. Make sure you have installed pytest and pytest-qt as mentioned in the Requirements section.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to execute the tests:
```shell
pystest test_plotify.py
```
The tests will be executed, and the results will be displayed in the terminal.
## Code Organization and Documentation
The code is organized into multiple files to maintain modularity and readability. Here's an overview of the code structure:

- `plotify.py`: Contains the main entry point of the program.
- `function_plotter.py`: Implements the GUI and handles user interactions.
- `function_parser.py`: Parses and evaluates the user-entered function.
- `plotter.py`: Handles the plotting of the graph using Matplotlib.
- `test_plotify.py`: Contains automated tests for the program.

The code is documented using inline comments to explain the purpose and functionality of each component. Additionally, the repository includes this README file to provide instructions and explanations about the program.

## Snapshots from Plotify
### Valid Input and Output 
![Example on Valid input](https://github.com/Ibrahim-Ehab/micro-master-task-answer/blob/main/screenshots/v_input_output.png)

### Invalid Inputs 
![](https://github.com/Ibrahim-Ehab/micro-master-task-answer/blob/main/screenshots/not_valid_input.png)

### Incomplete Inputs
![](https://github.com/Ibrahim-Ehab/micro-master-task-answer/blob/main/screenshots/not_complete_input.png)

### Features in Plotify
![](https://github.com/Ibrahim-Ehab/micro-master-task-answer/blob/main/screenshots/features.png)
1. `Resete Original View`.
2. `Back to the previous view`.
3. `Forward to next view`.
4. `move around with plot`.
5. `Zoom to rectangle`.
6. `Configure subplots`.
8. `Figure options`.
10. `Save the figure`.
    
#### Configure Subplots
![](https://github.com/Ibrahim-Ehab/micro-master-task-answer/blob/main/screenshots/configure_subplot.png)

#### Figure options:
![](https://github.com/Ibrahim-Ehab/micro-master-task-answer/blob/main/screenshots/figure_options_1.png)

![](https://github.com/Ibrahim-Ehab/micro-master-task-answer/blob/main/screenshots/figure_options_2.png)


Feel free to explore the source code and modify it according to your needs. If you encounter any issues or have suggestions for improvements, please submit an issue or a pull request in this repository.

Happy plotting!
