from PySide6.QtWidgets import QDialog, QLabel, QComboBox, QTreeWidget, QTreeWidgetItem, QPushButton, QLineEdit, QVBoxLayout, \
    QHBoxLayout, QMessageBox
from Root.models.categories import Categories
from Root.db_conection.transaction_dao import TransactionDao
from Root.models.transaction import Transaction


class ModifyTransactionDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Modify')
        self.setFixedSize(700,500)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.transaction_id = 0
        self.list_current_item = []
        transactions_table = QTreeWidget()
        transactions_table.setHeaderLabels(['Transaction Type', 'Category Name', 'Amount',
                                          'Transaction Date', 'Description'])

        transactions_list = TransactionDao().select_all_transactions('1')
        for i in transactions_list:
            QTreeWidgetItem(transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

        transactions_table.clicked.connect(lambda: self.transaction_selected(transactions_table))

        self.main_layout.addWidget(transactions_table)

        new_category = QLabel('Nueva categoria')
        self.main_layout.addWidget(new_category)

        self.new_category_entry = QComboBox()
        self.new_category_entry.addItems(Categories().CATEGORIES.keys())
        self.new_category_entry.setCurrentIndex(-1)
        self.main_layout.addWidget(self.new_category_entry)

        new_amount = QLabel('Nuevo monto')
        self.main_layout.addWidget(new_amount)

        self.new_amount_entry = QLineEdit()
        self.main_layout.addWidget(self.new_amount_entry)

        new_description = QLabel('Nueva description')
        self.main_layout.addWidget(new_description)

        self.new_description_entry = QLineEdit()
        self.main_layout.addWidget(self.new_description_entry)

        modify_button = QPushButton('MODIFICAR')
        modify_button.clicked.connect(self.modify_button_action)
        self.main_layout.addWidget(modify_button)

        cancel_button = QPushButton('CANCEL')
        cancel_button.clicked.connect(self.cancel_button_action)
        self.main_layout.addWidget(cancel_button)

    def modify_button_action(self):
        msg = QMessageBox(self)
        msg.setWindowTitle('Atencion')
        msg.informativeText()
        msg.setText('Estas seguro de queres modificar este movimiento?')
        msg.setStandardButtons(msg.StandardButton.Yes | msg.StandardButton.No)
        msg.exec()
        if 'Yes' in msg.clickedButton().text():
            update_transaction = Transaction(transaction_id=self.transaction_id,
                                             transaction_type=self.list_current_item[0].lower(),
                                             category_id=Categories().CATEGORIES.get(self.new_category_entry.currentText()),
                                             amount=self.new_amount_entry.text(),
                                             text_description=self.new_description_entry.text())
            # TransactionDao().update_transaction(update_transaction)
            self.close()

    def cancel_button_action(self):
        self.close()

    def transaction_selected(self, table):
        current_item = table.currentItem()
        index = 0
        self.transaction_id = current_item.toolTip(7)
        for item in range(5):
            self.list_current_item.append(current_item.text(index))
            index += 1