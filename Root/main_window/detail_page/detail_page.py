from PySide6.QtWidgets import QApplication,QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTreeWidget, \
    QTreeWidgetItem

from Root.login.session import Session
from Root.main_window.detail_page.add_transaction_dialog import AddTransactionDialog
from Root.main_window.detail_page.modify_transaction_dialog import ModifyTransactionDialog
from Root.main_window.detail_page.delete_transaction_dialog import DeleteTransactionDialog
from Root.main_window.detail_page.transaction_services import TransactionServices


class DetailPage(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        # self.setFixedSize(700,500)
        main_label = QLabel('DETAILS')
        self.main_layout.addWidget(main_label)
        self.resume_tables_layout = QHBoxLayout()
        self.main_layout.addLayout(self.resume_tables_layout)

        self.expensives_table = QTreeWidget()
        self.expensives_table.setHeaderLabels(['Transaction Type', 'Category Name', 'Amount',
                                         'Transaction Date','Description'])

        expensive_list = TransactionServices().get_expensives(Session.get_current_user_id())
        for i in expensive_list:
            QTreeWidgetItem(self.expensives_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

        self.resume_tables_layout.addWidget(self.expensives_table)

        self.incomes_table = QTreeWidget()
        self.incomes_table.setHeaderLabels(['Transaction Type', 'Category Name', 'Amount',
                                      'Transaction Date','Description'])

        incomes_list = TransactionServices().get_incomes('1')
        for i in incomes_list:
            QTreeWidgetItem(self.incomes_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

        self.resume_tables_layout.addWidget(self.incomes_table)

        add_transaction_button = QPushButton('ADD TRANSACTION')
        add_transaction_button.clicked.connect(self.add_transaction)
        self.main_layout.addWidget(add_transaction_button)

        modify_transaction_button = QPushButton('MODIFY TRANSACTION')
        modify_transaction_button.clicked.connect(self.modify_transaction)
        self.main_layout.addWidget(modify_transaction_button)

        delete_transaction_button = QPushButton('DELETE TRANSACTION')
        delete_transaction_button.clicked.connect(self.delete_transaction)
        self.main_layout.addWidget(delete_transaction_button)

    def add_transaction(self):
        AddTransactionDialog(self).exec()

    def modify_transaction(self):
        ModifyTransactionDialog(self).exec()
        self.expensives_table.repaint()
        self.incomes_table.repaint()

    def delete_transaction(self):
        DeleteTransactionDialog(self).exec()

    def update_tables(self):
        self.expensives_table.clear()
        self.incomes_table.clear()

        expensive_list = TransactionServices.get_expensives(Session.get_current_user_id())
        for i in expensive_list:
            QTreeWidgetItem(self.expensives_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

        incomes_list = TransactionServices.get_incomes(Session.get_current_user_id())
        for i in incomes_list:
            QTreeWidgetItem(self.incomes_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

        self.incomes_table.repaint()
        self.expensives_table.repaint()

if __name__ == '__main__':

    app = QApplication()
    w = DetailPage()
    w.show()
    app.exec()