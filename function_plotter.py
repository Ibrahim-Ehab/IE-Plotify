from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QFont
from function_parser import validate_function
from plotter import plot_graph

class PlotterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 600, 400)

        font = QFont("Arial", 12)

        # Create labels and input fields for function, min value, and max value
        self.function_label = QLabel("Enter a function of x:")
        self.function_label.setFont(font)
        self.function_input = QLineEdit()
        self.function_input.setFont(font)

        self.min_label = QLabel("Enter min value of x:")
        self.min_label.setFont(font)
        self.min_input = QLineEdit()
        self.min_input.setFont(font)

        self.max_label = QLabel("Enter max value of x:")
        self.max_label.setFont(font)
        self.max_input = QLineEdit()
        self.max_input.setFont(font)

        # Create a button to trigger the plot action
        self.plot_button = QPushButton("Plot")
        self.plot_button.setFont(font)
        self.plot_button.clicked.connect(self.plot)

        # Create a vertical layout and add the labels, input fields, and button to it
        layout = QVBoxLayout()
        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(self.min_label)
        layout.addWidget(self.min_input)
        layout.addWidget(self.max_label)
        layout.addWidget(self.max_input)
        layout.addWidget(self.plot_button)

        # Create a central widget and set the layout on it
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def validate_input(self):
        # Retrieve the function, min value, and max value from the input fields
        function = self.function_input.text()
        min_value = self.min_input.text()
        max_value = self.max_input.text()

        # Check if any of the input fields are empty
        if not function or not min_value or not max_value:
            self.show_error("Please enter all values.")
            return False

        # Validate the function using the validate_function function from function_parser module
        if not validate_function(function):
            self.show_error("Invalid function. Please use numbers, x, +, -, *, /, ^, and parentheses.")
            return False

        try:
            # Check if min_value and max_value can be converted to floats
            float(min_value)
            float(max_value)
        except ValueError:
            self.show_error("Invalid min/max values. Please enter valid numbers.")
            return False

        return True

    def show_error(self, message):
        # Create an error label with the given message
        error_label = QLabel(message)
        error_label.setStyleSheet("color: red; font-weight: bold;")

        # Add the error label to the layout of the central widget
        layout = self.centralWidget().layout()
        layout.addWidget(error_label)

    def plot(self):
        # Validate the input before proceeding with plotting
        if not self.validate_input():
            return

        # Retrieve the function, min value, and max value from the input fields
        function = self.function_input.text()
        # Replace '^' with '**' to match Python's exponentiation operator
        function = function.replace('^', '**')
        min_value = float(self.min_input.text())
        max_value = float(self.max_input.text())

        # Call the plot_graph function from the plotter module to plot the graph
        plot_graph(function, min_value, max_value, self.show_error)
