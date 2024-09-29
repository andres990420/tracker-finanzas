import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QStackedWidget, QStackedLayout, QSizePolicy, QGridLayout
from PySide6.QtCore import Qt

from Root.login.session import Session
from Root.main_window.dashboard.dashboard_page import DashboardPage
from Root.main_window.detail_page.detail_page import DetailPage
from Root.main_window.side_menu_bar_contract import ContractMenuBar
from Root.main_window.side_menu_bar_expanded import ExpandedMenuBar


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.resize(800, 300)
        self.move(200,0)

        self.base_layout = QHBoxLayout()
        self.main_widget.setLayout(self.base_layout)

        widget1 = QStackedWidget()
        widget1.addWidget(ExpandedMenuBar())
        widget1.addWidget(ContractMenuBar())
        widget1.setFixedWidth(150)
        self.base_layout.addWidget(widget1)

        self.layout2 = QStackedLayout()
        self.base_layout.addLayout(self.layout2)

        self.layout2.addWidget(DashboardPage())
        self.layout2.addWidget(DetailPage())
        self.layout2.currentIndex()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())