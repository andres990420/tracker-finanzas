from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QTreeWidget, \
    QTreeWidgetItem, QVBoxLayout, QComboBox, QMessageBox, QCheckBox, QHBoxLayout, QCalendarWidget
from PySide6.QtCore import Qt
from Root.login.session import Session
from Root.main_window.detail_page.transaction_services import TransactionServices
from Root.models.categories import Categories


class DeleteTransactionDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(700, 500)
        self.setWindowTitle('Eliminar Movimiento')
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.transaction_id = 0

        filter_label = QLabel('FIlTERS')
        self.main_layout.addWidget(filter_label)

        self.year_filter = QComboBox()
        self.year_filter.addItems(['2024', '2023', '2022'])
        self.year_filter.currentTextChanged.connect(lambda: self.apply_filters())
        self.main_layout.addWidget(self.year_filter)

        transaction_type_filter_label = QLabel('Transaction Type')
        self.main_layout.addWidget(transaction_type_filter_label)

        self.transaction_type_filter_entry = QComboBox()
        self.transaction_type_filter_entry.addItems(['Ingreso', 'Gasto'])
        self.transaction_type_filter_entry.setCurrentIndex(-1)
        self.transaction_type_filter_entry.currentTextChanged.connect(lambda: self.apply_filters())
        self.main_layout.addWidget(self.transaction_type_filter_entry)

        self.categories_filter = QComboBox()
        self.categories_filter.addItems(Categories.CATEGORIES.keys())
        self.categories_filter.setCurrentIndex(-1)
        self.categories_filter.setDisabled(True)
        self.categories_filter.currentTextChanged.connect(lambda: self.apply_filters())
        self.main_layout.addWidget(self.categories_filter)

        self.clean_button_filters = QPushButton('CLEAN FILTERS')
        self.clean_button_filters.clicked.connect(lambda: self.clean_filters())
        self.main_layout.addWidget(self.clean_button_filters)

        self.transactions_table = QTreeWidget()
        self.transactions_table.setHeaderLabels(['Transaction Type', 'Category Name', 'Amount',
                                            'Transaction Date','Description'])

        self.main_layout.addWidget(self.transactions_table)
        transactions_list = TransactionServices().get_all_transactions(Session.get_current_user_id(), '2024')
        for i in transactions_list:
            QTreeWidgetItem(self.transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

        self.transactions_table.clicked.connect(lambda: self.selected_transaction(self.transactions_table))

        delete_button = QPushButton('DELETE')
        self.main_layout.addWidget(delete_button)

        cancel_button = QPushButton('CANCEL')
        self.main_layout.addWidget(cancel_button)

        delete_button.clicked.connect(self.delete_transaction)
        cancel_button.clicked.connect(self.cancel_button_action)


    def clean_filters(self):
        self.categories_filter.setCurrentIndex(-1)
        self.categories_filter.setDisabled(True)
        self.transaction_type_filter_entry.setCurrentIndex(-1)

    def apply_filters(self):
        self.transactions_table.clear()
        if self.transaction_type_filter_entry.currentIndex() and self.categories_filter.currentIndex() != -1:
            if self.transaction_type_filter_entry.currentText() == 'Gasto':
                print(self.categories_filter.currentText().lower())
                transactions_list = TransactionServices().get_expensives_categories_detailpages(
                    Session.get_current_user_id(), self.year_filter.currentText(),
                    self.categories_filter.currentText())
                for i in transactions_list:
                    QTreeWidgetItem(self.transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')
            else:
                transactions_list = TransactionServices().get_incomes_categories_detailpage(
                    Session.get_current_user_id(), self.year_filter.currentText(),
                    self.categories_filter.currentText())
                for i in transactions_list:
                    QTreeWidgetItem(self.transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

        elif self.transaction_type_filter_entry.currentIndex() != -1:
            transaction_list = TransactionServices.selected_by_transaction_type(
                Session.get_current_user_id(), self.transaction_type_filter_entry.currentText().lower(),
                self.year_filter.currentText())
            for i in transaction_list:
                QTreeWidgetItem(self.transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')
            self.categories_filter.setEnabled(True)
        else:
            transaction_list = TransactionServices.get_all_transactions(
                Session.get_current_user_id(),
                self.year_filter.currentText())
            for i in transaction_list:
                QTreeWidgetItem(self.transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')
        self.transactions_table.repaint()

    def selected_transaction(self, table):
        current_item = table.currentItem()
        self.transaction_id = current_item.toolTip(7)

    def delete_transaction(self):
        msg = QMessageBox(self)
        yes_button = msg.StandardButton.Yes
        no_button = msg.StandardButton.No
        result = msg.warning(self,'advertencia',
                             'Seguro de querer eliminar la transaccion? No se podra recuperar luego',
                             yes_button | no_button)
        if 'Yes' in str(result):
            TransactionServices().delete_transaction(self.transaction_id)
            self.parent().update_tables()
            self.close()

    def cancel_button_action(self):
        self.close()