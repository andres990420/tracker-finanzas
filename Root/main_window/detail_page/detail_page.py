from PySide6.QtWidgets import QApplication,QWidget, QPushButton, QLabel, QListView, QVBoxLayout, QHBoxLayout, QTreeWidget, \
    QTreeWidgetItem
from Root.db_conection.transaction_dao import TransactionDao
from add_transaction_dialog import AddTransactionDialog

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

        self.create_tables_components()
        self.create_buttons()

    def create_tables_components(self):
        expensives_table = QTreeWidget()
        expensives_table.setHeaderLabels(['Transaction Type', 'Category Name', 'Amount',
                                         'Transaction Date','Description'])

        expensive_list = TransactionDao().select_all_expensives('1')
        for i in expensive_list:
            QTreeWidgetItem(expensives_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

        self.resume_tables_layout.addWidget(expensives_table)

        incomes_table = QTreeWidget()
        incomes_table.setHeaderLabels(['Transaction Type', 'Category Name', 'Amount',
                                      'Transaction Date','Description'])

        incomes_list = TransactionDao().select_all_incomes('1')
        for i in incomes_list:
            QTreeWidgetItem(incomes_table, list(i))

        self.resume_tables_layout.addWidget(incomes_table)

        def select_item(table):
            current_item = table.currentItem()
            list_current_item = []
            index = 0
            print(current_item.toolTip(7))
            for item in range(5):
                list_current_item.append(current_item.text(index))
                index += 1
            print(list_current_item)

        expensives_table.clicked.connect(lambda: select_item(expensives_table))
        incomes_table.clicked.connect(lambda: select_item(incomes_table))

    def create_buttons(self):
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
        pass

    def delete_transaction(self):
        pass

if __name__ == '__main__':

    app = QApplication()
    w = DetailPage()
    w.show()
    app.exec()