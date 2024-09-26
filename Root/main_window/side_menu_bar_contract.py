from PySide6.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QMainWindow, QSpacerItem
from PySide6.QtGui import Qt
from Root.login.session import Session


class ContractMenuBar(QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setFixedWidth(40)

        # Label para la foto de perfil
        profile_photo_label = QLabel('[P]')
        self.main_layout.addWidget(profile_photo_label)

        # Label para el nombre del usurio
        profile_username_label = QLabel('[U]')
        profile_username_label.setGeometry(20,20,20,20)
        profile_username_label.setToolTip(Session.get_current_user().username)
        self.main_layout.addWidget(profile_username_label)

        # Icono del dashboard page
        dashboard_page_icon = QPushButton('[D]')
        dashboard_page_icon.setFlat(True)
        self.main_layout.addWidget(dashboard_page_icon)

        #Icono del detail page
        detail_page_icon = QPushButton('[DP]')
        detail_page_icon.setFlat(True)
        self.main_layout.addWidget(detail_page_icon)

        # Agregando un Spacer
        spacer = QSpacerItem(30, 400)
        self.main_layout.addItem(spacer)

        #Icono de settings
        settings_page_icon = QPushButton('[ST]')
        settings_page_icon.setFlat(True)
        self.main_layout.addWidget(settings_page_icon)

        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.setSpacing(30)
        self.setStyleSheet('background:"Blue"')
        self.show()