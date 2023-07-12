import sys
import re
import math
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QFont


class PlotterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 600, 400)

        font = QFont("Arial", 12)

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

        self.plot_button = QPushButton("Plot")
        self.plot_button.setFont(font)
        self.plot_button.clicked.connect(self.plot)

        layout = QVBoxLayout()
        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(self.min_label)
        layout.addWidget(self.min_input)
        layout.addWidget(self.max_label)
        layout.addWidget(self.max_input)
        layout.addWidget(self.plot_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def validate_input(self):
        function = self.function_input.text()
        min_value = self.min_input.text()
        max_value = self.max_input.text()

        if not function or not min_value or not max_value:
            self.show_error("Please enter all values.")
            return False

        # Check if the function is valid
        valid_function = re.match(r'^([+-/*\d\(\)x\s^]+)$', function)
        if not valid_function:
            self.show_error("Invalid function. Please use numbers, x, +, -, *, /, ^, and parentheses.")

        # Check if min and max values are valid numbers
        try:
            float(min_value)
            float(max_value)
        except ValueError:
            self.show_error("Invalid min/max values. Please enter valid numbers.")
            return False

        return True

    def show_error(self, message):
        error_label = QLabel(message)
        error_label.setStyleSheet("color: red; font-weight: bold;")
        layout = self.centralWidget().layout()
        layout.addWidget(error_label)

    def plot(self):
        if not self.validate_input():
            return

        function = self.function_input.text()
        function = function.replace('^', '**')  # Replace ^ with **
        min_value = float(self.min_input.text())
        max_value = float(self.max_input.text())

        x_values = []
        y_values = []

        step = (max_value - min_value) / 100
        x = min_value

        while x <= max_value:
            try:
                y = eval(function.replace('x', str(x)))
                x_values.append(x)
                y_values.append(y)
            except ZeroDivisionError:
                pass
            except:
                self.show_error("Error evaluating the function.")
                return

            x += step

        plt.figure(figsize=(6, 4))
        plt.plot(x_values, y_values, color='blue', linewidth=2.5)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.title('Function Plot', fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlotterWindow()
    window.show()
    sys.exit(app.exec())
