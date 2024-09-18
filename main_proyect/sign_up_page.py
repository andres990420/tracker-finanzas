from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication, QMainWindow
from users import Users
from authentificador import Authentificador
from base_logger import log


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
            valid_email = Authentificador().authen_email(email_entry.text())
            valid_password = Authentificador().authen_password(username_entry.text(), password_entry.text())
            valid_data = 0
            if valid_email is True:
                valid_data += 1
            if valid_password is True:
                valid_data += 1
            if valid_data == 2:
                new_user = Users(username=username_entry.text(),
                                 password=password_entry.text(),
                                 email=email_entry.text())
                # UserDao.add_user(new_user)
                # self.close()





        register_button = QPushButton('REGISTER')
        register_button.clicked.connect(sent_registration)
        self.main_layout.addWidget(register_button)


if __name__ == '__main__':
    app = QApplication()
    window = QMainWindow()
    window.show()
    sign_up = SignUpPage(window)
    app.exec()