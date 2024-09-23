from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication, QWidget, QMessageBox
import sys
from Root.login.session import Session
from sign_up_page import SignUpPage
from Root.db_conection.user_dao import UserDao
from Root.models.users import Users
from Root.main_window.main_window import MainWindow


class LoginInterface(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle('Login')
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_window = None

        self.createComponents()

    def createComponents(self):
        title_label = QLabel('TRACKER DE FINANZAS PERSONALES')
        self.main_layout.addWidget(title_label)

        user_label = QLabel('Username')
        user_entry = QLineEdit()

        self.main_layout.addWidget(user_label)
        self.main_layout.addWidget(user_entry)

        password_label = QLabel('Password')
        password_entry = QLineEdit()
        password_entry.setEchoMode(QLineEdit.EchoMode.Password)

        self.main_layout.addWidget(password_label)
        self.main_layout.addWidget(password_entry)

        sing_in_button = QPushButton('Sign In')

        self.main_layout.addWidget(sing_in_button)

        sing_up_button = QPushButton('Sign Up')
        sing_up_button.clicked.connect(self.signUp)
        self.main_layout.addWidget(sing_up_button)

        recover_password = QPushButton('Recover Password')
        recover_password.setFlat(True)
        recover_password.clicked.connect(self.recoverPassword)

        self.main_layout.addWidget(recover_password)

        def signIn():
            username = user_entry.text()
            password = password_entry.text()
            user_values = Users(username=username, password=password)
            user = UserDao.login(user_values)
            if user:
                Session.login(user)
                self.close()
                self.open_main_window()
            else:
                QMessageBox.warning(self, 'Error', 'Credenciales Incorrectas')

        sing_in_button.clicked.connect(signIn)

    def signUp(self):
        SignUpPage(self)

    def recoverPassword(self):
        pass

    def open_main_window(self):
        if not self.main_window:
            self.main_window = MainWindow()
        self.main_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginInterface()
    window.show()
    sys.exit(app.exec())
