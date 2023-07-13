import sys
from PySide6.QtWidgets import QApplication
from function_plotter import PlotterWindow

if __name__ == '__main__':
    # Create a QApplication instance to manage the GUI application
    app = QApplication(sys.argv)

    # Create an instance of the PlotterWindow class
    window = PlotterWindow()

    # Show the window
    window.show()

    # Start the application event loop
    sys.exit(app.exec())
