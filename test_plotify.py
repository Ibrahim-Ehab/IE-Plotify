import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt
from plotify import PlotterWindow


@pytest.fixture(scope="session")
def qapp(request):
    app = QApplication([])
    yield app
    app.exit()


def test_plot_button(qapp, qtbot):
    window = PlotterWindow()
    window.show()
    qtbot.addWidget(window)

    function_input = window.function_input
    min_input = window.min_input
    max_input = window.max_input
    plot_button = window.plot_button

    # Enter input values
    qtbot.keyClicks(function_input, "3*x^2 + 2*x")
    qtbot.keyClicks(min_input, "-5")
    qtbot.keyClicks(max_input, "5")

    # Click the plot button
    qtbot.mouseClick(plot_button, Qt.LeftButton)

    # You can add assertions to check the plot or other expected behavior

    window.close()


def test_empty_input(qapp, qtbot):
    window = PlotterWindow()
    window.show()
    qtbot.addWidget(window)

    function_input = window.function_input
    min_input = window.min_input
    max_input = window.max_input
    plot_button = window.plot_button

    # Enter empty input values
    qtbot.keyClicks(function_input, "")
    qtbot.keyClicks(min_input, "")
    qtbot.keyClicks(max_input, "")

    # Click the plot button
    qtbot.mouseClick(plot_button, Qt.LeftButton)

    # You can add assertions to check the error message or other expected behavior

    window.close()


def test_invalid_function(qapp, qtbot):
    window = PlotterWindow()
    window.show()
    qtbot.addWidget(window)

    function_input = window.function_input
    min_input = window.min_input
    max_input = window.max_input
    plot_button = window.plot_button

    # Enter invalid function
    qtbot.keyClicks(function_input, "3*x^2 + 2*x +")
    qtbot.keyClicks(min_input, "-5")
    qtbot.keyClicks(max_input, "5")

    # Click the plot button
    qtbot.mouseClick(plot_button, Qt.LeftButton)

    # You can add assertions to check the error message or other expected behavior

    window.close()


def test_invalid_min_max(qapp, qtbot):
    window = PlotterWindow()
    window.show()
    qtbot.addWidget(window)

    function_input = window.function_input
    min_input = window.min_input
    max_input = window.max_input
    plot_button = window.plot_button

    # Enter invalid min and max values
    qtbot.keyClicks(function_input, "3*x^2 + 2*x")
    qtbot.keyClicks(min_input, "a")
    qtbot.keyClicks(max_input, "b")

    # Click the plot button
    qtbot.mouseClick(plot_button, Qt.LeftButton)

    # You can add assertions to check the error message or other expected behavior

    window.close()
