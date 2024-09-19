from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QCheckBox
import pyqtgraph as pg

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        tittle_label = QLabel('DASHBOARD')
        self.main_layout.addWidget(tittle_label)

        self.filter_layout = QHBoxLayout()
        self.main_layout.addLayout(self.filter_layout)

        self.createFilterComponents()
        self.createGraphs()

    def createFilterComponents(self):
        year_label = QLabel('Year')
        self.filter_layout.addWidget(year_label)

        year_checkbox = QCheckBox()
        self.filter_layout.addWidget(year_checkbox)

        month_label = QLabel('Month')
        self.filter_layout.addWidget(month_label)

        month_checkbox = QCheckBox()
        self.filter_layout.addWidget(month_checkbox)

    def createGraphs(self):
        plot_graph = pg.PlotWidget()
        plot_graph.plot([1,2,3,4,5,6], [20,21,22,23,24,25])
        self.main_layout.addWidget(plot_graph)


if __name__ == "__main__":
    app = QApplication()
    window = DashboardPage()
    window.show()
    app.exec()