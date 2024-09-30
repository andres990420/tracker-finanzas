from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTreeWidget, \
    QTreeWidgetItem, QComboBox

from Root.login.session import Session
from Root.main_window.detail_page.add_transaction_dialog import AddTransactionDialog
from Root.main_window.detail_page.modify_transaction_dialog import ModifyTransactionDialog
from Root.main_window.detail_page.delete_transaction_dialog import DeleteTransactionDialog
from Root.main_window.detail_page.transaction_services import TransactionServices
from Root.models.categories import Categories


class DetailPage(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        main_label = QLabel('DETAILS')
        self.main_layout.addWidget(main_label)

        self.year_filter = QComboBox()
        self.year_filter.addItems(['2024', '2023', '2022'])
        self.year_filter.currentIndexChanged.connect(lambda : self.update_tables())
        self.main_layout.addWidget(self.year_filter)

        self.category_filter = QComboBox()
        self.category_filter.addItems(Categories.CATEGORIES.keys())
        self.category_filter.setCurrentIndex(-1)
        self.category_filter.currentTextChanged.connect(lambda: self.update_tables())
        self.main_layout.addWidget(self.category_filter)

        clean_filter_button = QPushButton('CLEAN FILTER')
        clean_filter_button.clicked.connect(lambda: self.clean_filters())
        self.main_layout.addWidget(clean_filter_button)

        self.resume_tables_layout = QHBoxLayout()
        self.main_layout.addLayout(self.resume_tables_layout)

        self.expensives_table = QTreeWidget()
        self.expensives_table.setHeaderLabels(['Transaction Type', 'Category Name', 'Amount',
                                         'Transaction Date','Description'])

        expensive_list = TransactionServices().get_all_expensive_datetime_detailpages(
            Session().get_current_user_id(), self.year_filter.currentText())
        for i in expensive_list:
            QTreeWidgetItem(self.expensives_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

        self.resume_tables_layout.addWidget(self.expensives_table)

        self.incomes_table = QTreeWidget()
        self.incomes_table.setHeaderLabels(['Transaction Type', 'Category Name', 'Amount',
                                      'Transaction Date','Description'])

        incomes_list = TransactionServices().get_all_incomes_datetime_detailpage(
            Session.get_current_user_id(), self.year_filter.currentText())
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

    def clean_filters(self):
        self.category_filter.setCurrentIndex(-1)

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

        if self.category_filter.currentIndex() == -1:
            expensive_list = TransactionServices.get_all_expensive_datetime_detailpages(
                Session.get_current_user_id(),self.year_filter.currentText())
            for i in expensive_list:
                QTreeWidgetItem(self.expensives_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

            incomes_list = TransactionServices.get_all_incomes_datetime_detailpage(
                Session.get_current_user_id(), self.year_filter.currentText())
            for i in incomes_list:
                QTreeWidgetItem(self.incomes_table, list(i[1:6])).setToolTip(7, f'{i[0]}')
        else:
            expensive_list = TransactionServices.get_expensives_categories_detailpages(
                Session.get_current_user_id(), self.year_filter.currentText(), self.category_filter.currentText())
            for i in expensive_list:
                QTreeWidgetItem(self.expensives_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

            incomes_list = TransactionServices.get_incomes_categories_detailpage(
                Session.get_current_user_id(), self.year_filter.currentText(), self.category_filter.currentText())
            for i in incomes_list:
                QTreeWidgetItem(self.incomes_table, list(i[1:6])).setToolTip(7, f'{i[0]}')


        self.incomes_table.repaint()
        self.expensives_table.repaint()


if __name__ == '__main__':

    app = QApplication()
    w = DetailPage()
    w.show()
    app.exec()