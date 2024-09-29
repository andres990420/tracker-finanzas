from PySide6.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QSpacerItem, QMainWindow
from Root.login.session import Session


class ExpandedMenuBar(QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.setFixedWidth(150)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setStyleSheet('background: "Green"')

       # Label con la photo de perfil
        profile_pict_label = QLabel('[PROFILE PHOTO]')
        self.main_layout.addWidget(profile_pict_label)

        # Username Label
        user_label = QLabel(Session.get_current_user().username)
        self.main_layout.addWidget(user_label)

        # Dashboard Icon Button
        dashboard_icon_expanded = QPushButton('DASHBOARD')
        dashboard_icon_expanded.setFlat(True)
        dashboard_icon_expanded.clicked.connect(self.dashboard_page_button)
        self.main_layout.addWidget(dashboard_icon_expanded)

        #Detail page icon button
        detail_page_icon_expanded = QPushButton('DETAIL PAGE')
        detail_page_icon_expanded.setFlat(True)
        detail_page_icon_expanded.clicked.connect(self.detail_page_button)
        self.main_layout.addWidget(detail_page_icon_expanded)

        spacer = QSpacerItem(10, 370)
        self.main_layout.addItem(spacer)

        # Settings button
        settings_icon_expanded = QPushButton('SETTINGS')
        settings_icon_expanded.setFlat(True)
        self.main_layout.addWidget(settings_icon_expanded)

        self.main_layout.setSpacing(30)
        self.show()

    def dashboard_page_button(self):
        self.parent().parent().layout().children()[0].setCurrentIndex(0)

    def detail_page_button(self):
        t = QLabel('lol')
        self.parent().parent().layout().children()[0].setCurrentIndex(1)
