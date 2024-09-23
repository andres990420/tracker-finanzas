from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QApplication, QMainWindow

from Root.db_conection.user_dao import UserDao
from Root.models.users import Users
from Root.auth.authentificador import Authentificador


class SignUpPage(QDialog):

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Registration')
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.createComponents()
        self.exec()

    def createComponents(self):
        username_labe = QLabel('Username')
        username_entry = QLineEdit()

        self.main_layout.addWidget(username_labe)
        self.main_layout.addWidget(username_entry)

        password_label = QLabel('Password')
        password_entry = QLineEdit()

        self.main_layout.addWidget(password_label)
        self.main_layout.addWidget(password_entry)

        email_label = QLabel('Email')
        email_entry = QLineEdit()

        self.main_layout.addWidget(email_label)
        self.main_layout.addWidget(email_entry)

        def sent_registration():
            username = username_entry.text()
            password = password_entry.text()
            email = email_entry.text()
            valid_data = Authentificador().valid_data(username, password, email)
            if valid_data is True:
                new_user = Users(username=username,
                                 password=password,
                                 email=email)
                UserDao.add_user(new_user)
                self.close()
            else:
                print('Datos invalidos')

        register_button = QPushButton('REGISTER')
        register_button.clicked.connect(sent_registration)
        self.main_layout.addWidget(register_button)


if __name__ == '__main__':
    app = QApplication()
    window = QMainWindow()
    window.show()
    sign_up = SignUpPage(window)
    app.exec()