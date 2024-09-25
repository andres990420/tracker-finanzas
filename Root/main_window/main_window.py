import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QStackedWidget, QStackedLayout

from Root.login.session import Session
from Root.main_window.dashboard.dashboard_page import DashboardPage
from Root.main_window.detail_page.detail_page import DetailPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(700,600)
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.base_layout = QHBoxLayout()
        self.main_widget.setLayout(self.base_layout)

        self.side_menu_bar_layout = QVBoxLayout()
        self.base_layout.addLayout(self.side_menu_bar_layout)

        self.stacked_layout = QStackedLayout()
        self.base_layout.addLayout(self.stacked_layout)

        self.stackedLayoutComponents()
        self.createSideMenuComponents()

    def stackedLayoutComponents(self):
        dashboard_view_page = DashboardPage()
        detail_view_page = DetailPage()

        self.stacked_layout.addWidget(dashboard_view_page)
        self.stacked_layout.addWidget(detail_view_page)

    def createSideMenuComponents(self):
        self.profile_photo_label = QLabel('PROFILE PHOTO')
        self.side_menu_bar_layout.addWidget(self.profile_photo_label)

        username_label = QLabel(Session.get_current_user().username)
        self.side_menu_bar_layout.addWidget(username_label)

        dashboard_button = QPushButton('Dashboard')
        dashboard_button.setFlat(True)
        dashboard_button.clicked.connect(self.activeDashboardPage)
        self.side_menu_bar_layout.addWidget(dashboard_button)

        detail_expensive_button = QPushButton('Detail Expensives')
        detail_expensive_button.setFlat(True)
        self.side_menu_bar_layout.addWidget(detail_expensive_button)
        detail_expensive_button.clicked.connect(self.activeDetailPage)

        settings_button = QPushButton('Settings')
        settings_button.setFlat(True)
        settings_button.clicked.connect(self.settingsPage)
        self.side_menu_bar_layout.addWidget(settings_button)

    def activeDashboardPage(self):
        self.stacked_layout.setCurrentIndex(0)

    def activeDetailPage(self):
        self.stacked_layout.setCurrentIndex(1)

    def settingsPage(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())