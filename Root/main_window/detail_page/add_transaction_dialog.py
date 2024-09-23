from PySide6.QtWidgets import QDialog, QLabel, QPushButton,QMessageBox,QTextEdit, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout

from Root.login.session import Session
from Root.models.categories import Categories
from Root.main_window.detail_page.transaction_services import TransactionServices


class AddTransactionDialog(QDialog):

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Agregacion de transaccion')
        self.setFixedSize(300, 400)
        self.transaction_services = TransactionServices()

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        transaction_type = QLabel('Tipo de Transaction')
        self.main_layout.addWidget(transaction_type)

        self.transaction_type_entry = QComboBox()
        self.transaction_type_entry.addItems(['Ingreso', 'Gasto'])
        self.transaction_type_entry.setCurrentIndex(-1)
        self.main_layout.addWidget(self.transaction_type_entry)

        category_type = QLabel('Categoria')
        self.main_layout.addWidget(category_type)

        self.category_type_entry = QComboBox()
        self.category_type_entry.addItems(Categories().CATEGORIES.keys())
        self.category_type_entry.setCurrentIndex(-1)

        self.main_layout.addWidget(self.category_type_entry)

        amount = QLabel('Monto')
        self.main_layout.addWidget(amount)

        self.amount_entry = QLineEdit()
        self.main_layout.addWidget(self.amount_entry)

        transaction_description = QLabel('Description de la transaccion')
        self.main_layout.addWidget(transaction_description)

        self.transaction_description_entry = QLineEdit()
        self.transaction_description_entry.setPlaceholderText('Describa los detalles de la transaccion...')
        self.main_layout.addWidget(self.transaction_description_entry)

        add_button = QPushButton('ADD')
        add_button.clicked.connect(self.add_button_action)
        self.main_layout.addWidget(add_button)

        cancel_button = QPushButton('CANCEL')
        cancel_button.clicked.connect(self.cancel_button_action)
        self.main_layout.addWidget(cancel_button)

    def add_button_action(self):
        msg = QMessageBox(self)
        msg.setWindowTitle('Atencion')
        msg.informativeText()
        msg.setText('Estas seguro de queres agregar este movimiento?')
        msg.setStandardButtons(msg.StandardButton.Yes | msg.StandardButton.No)
        msg.exec()
        if 'Yes' in msg.clickedButton().text():
            self.transaction_services.add_transaction(
                user_id=Session.get_current_user_id(),
                transaction_type=self.transaction_type_entry.currentText().lower(),
                category_id=Categories().CATEGORIES.get(self.category_type_entry.currentText()),
                amount=self.amount_entry.text(),
                text_description=self.transaction_description_entry.text())

            self.parent().update_tables()
            self.close()
        else:
            msg.close()

    def cancel_button_action(self):
        self.close()