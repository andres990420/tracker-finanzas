from PySide6.QtWidgets import QDialog, QLabel, QComboBox, QTreeWidget, QTreeWidgetItem, QPushButton, QLineEdit, QVBoxLayout, \
    QHBoxLayout, QMessageBox

from Root.login.session import Session
from Root.models.categories import Categories
from Root.main_window.detail_page.transaction_services import TransactionServices


class ModifyTransactionDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Modify')
        self.setFixedSize(700,500)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.year_filter = QComboBox()
        self.year_filter.addItems(['2024', '2023', '2022'])
        self.year_filter.currentTextChanged.connect(lambda: self.apply_filter())
        self.main_layout.addWidget(self.year_filter)

        self.transaction_type = QComboBox()
        self.transaction_type.addItems(['Ingreso', 'Gasto'])
        self.transaction_type.setCurrentIndex(-1)
        self.transaction_type.currentTextChanged.connect(lambda: self.apply_filter())
        self.main_layout.addWidget(self.transaction_type)

        self.category_filter = QComboBox()
        self.category_filter.addItems(Categories.CATEGORIES.keys())
        self.category_filter.setCurrentIndex(-1)
        self.category_filter.setDisabled(True)
        self.category_filter.currentTextChanged.connect(lambda: self.apply_filter())
        self.main_layout.addWidget(self.category_filter)

        clean_button = QPushButton('CLEAN FILTERS')
        clean_button.clicked.connect(self.clean_filters)
        self.main_layout.addWidget(clean_button)

        self.transaction_id = 0
        self.list_current_item = []
        self.transactions_table = QTreeWidget()
        self.transactions_table.setHeaderLabels(['Transaction Type', 'Category Name', 'Amount',
                                          'Transaction Date', 'Description'])

        transactions_list = TransactionServices().get_all_transactions(
            Session.get_current_user_id(), self.year_filter.currentText())
        for i in transactions_list:
            QTreeWidgetItem(self.transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

        self.transactions_table.clicked.connect(lambda: self.transaction_selected(self.transactions_table))

        self.main_layout.addWidget(self.transactions_table)

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
            TransactionServices().update_transaction(
                transaction_id=self.transaction_id,
                transaction_type=self.list_current_item[0].lower(),
                category_id=Categories().CATEGORIES.get(self.new_category_entry.currentText()),
                amount=self.new_amount_entry.text(),
                text_description=self.new_description_entry.text())
            self.parent().update_tables()
            self.close()

    def cancel_button_action(self):
        self.close()

    def transaction_selected(self, table):
        current_item = table.currentItem()

        self.new_category_entry.clear()
        if current_item.text(0) == "ingreso":
            self.new_category_entry.addItems(['Sueldo', 'Cheque', 'Transferencia'])
            self.new_category_entry.setPlaceholderText(current_item.text(1))
        elif current_item.text(0) == 'gasto':
            self.new_category_entry.addItems(Categories.CATEGORIES.keys())
            self.new_category_entry.setPlaceholderText(current_item.text(1))

        self.new_amount_entry.setPlaceholderText(current_item.text(2))
        self.new_description_entry.setPlaceholderText(current_item.text(4))
        self.transaction_id = current_item.toolTip(7)
        for item in range(5):
            self.list_current_item.append(current_item.text(item))

    def apply_filter(self):
        self.transactions_table.clear()

        if self.transaction_type.currentIndex() != -1 and self.category_filter.currentIndex() != -1:
            if self.transaction_type.currentText() == 'Gasto':
                print(self.category_filter.currentText().lower())
                transactions_list = TransactionServices().get_expensives_categories_detailpages(
                    Session.get_current_user_id(), self.year_filter.currentText(), self.category_filter.currentText())
                for i in transactions_list:
                    QTreeWidgetItem(self.transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')
            else:
                transactions_list = TransactionServices().get_incomes_categories_detailpage(
                    Session.get_current_user_id(), self.year_filter.currentText(), self.category_filter.currentText())
                for i in transactions_list:
                    QTreeWidgetItem(self.transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

            self.category_filter.setEnabled(True)

        elif self.transaction_type.currentIndex() != -1:
            transactions_list = TransactionServices().selected_by_transaction_type(
                Session.get_current_user_id(), self.transaction_type.currentText().lower(), self.year_filter.currentText())
            for i in transactions_list:
                QTreeWidgetItem(self.transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

            self.category_filter.setEnabled(True)
        else:
            transactions_list = TransactionServices().get_all_transactions(
                Session.get_current_user_id(), self.year_filter.currentText())
            for i in transactions_list:
                QTreeWidgetItem(self.transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

        self.transactions_table.repaint()

    def clean_filters(self):
        self.category_filter.setCurrentIndex(-1)
        self.transaction_type.setCurrentIndex(-1)
        self.category_filter.setDisabled(True)