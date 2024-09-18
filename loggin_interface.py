from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication, QWidget
import sys
from sign_up_page import SignUpPage
from user_dao import UserDao
from users import Users


class LoginInterface(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle('Login')
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

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
            users_values = Users(username=user_entry.text(), password=password_entry.text())
            if UserDao.login(users_values) is True:
                print('LOGEAR EN LA APP')
                self.close()

        sing_in_button.clicked.connect(signIn)

    def signUp(self):
        SignUpPage(self)

    def recoverPassword(self):
        pass


if __name__ == "__main__":
    app = QApplication()
    window = LoginInterface()
    window.show()
    sys.exit(app.exec())
