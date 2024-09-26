import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QStackedWidget, QStackedLayout

from Root.login.session import Session
from Root.main_window.dashboard.dashboard_page import DashboardPage
from Root.main_window.detail_page.detail_page import DetailPage
from Root.main_window.side_menu_bar_contract import ContractMenuBar
from Root.main_window.side_menu_bar_expanded import ExpandedMenuBar


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 600)
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.base_layout = QHBoxLayout()
        self.main_widget.setLayout(self.base_layout)

        self.side_menu_bar_base_layout = QVBoxLayout()
        self.side_menu_bar_layout_components = QStackedLayout()
        self.base_layout.addLayout(self.side_menu_bar_base_layout)

        self.contract_expand_button = QPushButton('<--')
        self.contract_expand_button.clicked.connect(self.contract_expand_button_action)
        # self.side_menu_bar_base_layout.addWidget(self.contract_expand_button)
        # self.side_menu_bar_base_layout.addLayout(self.side_menu_bar_layout_components)

        self.base_layout.addWidget(ContractMenuBar())
        self.base_layout.addWidget(ExpandedMenuBar())

        self.stacked_layout = QStackedLayout()
        self.base_layout.addLayout(self.stacked_layout)


        self.stacked_layout_components()

    def stacked_layout_components(self):
        dashboard_view_page = DashboardPage()
        detail_view_page = DetailPage()

        self.stacked_layout.addWidget(dashboard_view_page)
        self.stacked_layout.addWidget(detail_view_page)

    def contract_expand_button_action(self):
        if self.side_menu_bar_layout_components.currentIndex() == 0:
            self.side_menu_bar_layout_components.setCurrentIndex(1)
            self.contract_expand_button.setText('<-')
        elif self.side_menu_bar_layout_components.currentIndex() == 1:
            self.side_menu_bar_layout_components.setCurrentIndex(0)
            self.contract_expand_button.setText('<--')

    def active_dashboard_page(self):
        self.stacked_layout.setCurrentIndex(0)

    def active_detail_page(self):
        self.stacked_layout.setCurrentIndex(1)

    def settings_page(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())