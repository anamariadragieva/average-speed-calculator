from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QApplication, QComboBox
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # create widgets
        distance_label = QLabel("Distance: ")
        self.distance_input = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(['Metric (km)', 'Imperial (miles)'])

        time_label = QLabel("Time (Hours): ")
        self.time_input = QLineEdit()

        calculate_button = QPushButton("Calculate Average Speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_input.text())
        time = float(self.time_input.text())
        if self.unit_combo.currentText() == 'Metric (km)':
            distance_km = distance / time
            self.output_label.setText(f"The average speed is {distance_km} km/h.")
        if self.unit_combo.currentText() == 'Imperial (miles)':
            distance_km = distance / time
            self.output_label.setText(f"The average speed is {distance_km} mph.")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())


