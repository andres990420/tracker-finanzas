from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QTreeWidget, \
    QTreeWidgetItem, QVBoxLayout, QComboBox, QMessageBox, QCheckBox, QHBoxLayout, QCalendarWidget
from PySide6.QtCore import Qt
from Root.login.session import Session
from Root.main_window.detail_page.transaction_services import TransactionServices


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

        transaction_type_filter_label = QLabel('Transaction Type')
        self.main_layout.addWidget(transaction_type_filter_label)

        transaction_type_filter_entry = QComboBox()
        transaction_type_filter_entry.addItems(['Ingreso', 'Gasto'])
        transaction_type_filter_entry.setCurrentIndex(-1)
        transaction_type_filter_entry.currentTextChanged.connect(
            lambda : self.filter_by_transaction(transaction_type_filter_entry.currentText()))
        self.main_layout.addWidget(transaction_type_filter_entry)

        data_filter_label = QLabel('DATES')
        self.main_layout.addWidget(data_filter_label)

        year_month_layout = QHBoxLayout()
        year_month_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addLayout(year_month_layout)

        self.year_month_checkbox = QCheckBox()
        self.year_month_checkbox.setObjectName('check1')
        self.year_month_checkbox.checkStateChanged.connect(
            lambda : self.checkbox_selected(self.year_month_checkbox.objectName(), self.year_month_checkbox.checkState()))
        year_month_layout.addWidget(self.year_month_checkbox)

        self.year_filter = QComboBox()
        self.year_filter.addItems(['2024', '2023', '2022', '2021'])
        self.year_filter.setCurrentIndex(-1)
        year_month_layout.addWidget(self.year_filter)

        self.month_filter = QComboBox()
        self.month_filter.addItems(['ENERO', 'FEBRERO', 'MARZO'])
        self.month_filter.setCurrentIndex(-1)
        year_month_layout.addWidget(self.month_filter)

        self.year_month_button = QPushButton('SEARCH')
        self.year_month_button.clicked.connect(
            lambda : self.filter_by_year_month(self.year_filter.currentText(), self.month_filter.currentText()))
        year_month_layout.addWidget(self.year_month_button)

        between_dates_layout = QHBoxLayout()
        between_dates_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addLayout(between_dates_layout)

        self.between_dates_checkbox = QCheckBox()
        self.between_dates_checkbox.setObjectName('check2')
        self.between_dates_checkbox.checkStateChanged.connect(
            lambda : self.checkbox_selected(self.between_dates_checkbox.objectName(), self.between_dates_checkbox.checkState()))
        between_dates_layout.addWidget(self.between_dates_checkbox)

        date1_label = QLabel('DATE 1')
        between_dates_layout.addWidget(date1_label)
        self.date1_year_filter_entry = QComboBox()
        self.date1_year_filter_entry.addItems(['2024', '2023', '2022', '2021'])
        self.date1_year_filter_entry.setCurrentIndex(-1)
        between_dates_layout.addWidget(self.date1_year_filter_entry)

        self.date1_month_filter_entry = QComboBox()
        self.date1_month_filter_entry.addItems(['ENERO', 'FEBRERO', 'MARZO'])
        self.date1_month_filter_entry.setCurrentIndex(-1)
        between_dates_layout.addWidget(self.date1_month_filter_entry)

        date2_label = QLabel('Date 2')
        between_dates_layout.addWidget(date2_label)

        self.date2_year_filter_entry = QComboBox()
        self.date2_year_filter_entry.addItems(['2024', '2023', '2022', '2021'])
        self.date2_year_filter_entry.setCurrentIndex(-1)
        between_dates_layout.addWidget(self.date2_year_filter_entry)

        self.date2_month_filter_entry = QComboBox()
        self.date2_month_filter_entry.addItems(['ENERO', 'FEBRERO', 'MARZO'])
        self.date2_month_filter_entry.setCurrentIndex(-1)
        between_dates_layout.addWidget(self.date2_month_filter_entry)

        self.between_dates_button = QPushButton('SEARCH')
        between_dates_layout.addWidget(self.between_dates_button)

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

    def checkbox_selected(self, name, state):
        if name == 'check1' and state == state.Checked:
            self.between_dates_checkbox.setDisabled(True)
            self.date2_year_filter_entry.setDisabled(True)
            self.date2_month_filter_entry.setDisabled(True)
            self.date1_month_filter_entry.setDisabled(True)
            self.date1_year_filter_entry.setDisabled(True)
            self.between_dates_button.setDisabled(True)
        elif name == 'check2' and state == state.Checked:
            self.year_month_checkbox.setDisabled(True)
            self.year_month_button.setDisabled(True)
            self.month_filter.setDisabled(True)
            self.year_filter.setDisabled(True)
        else:
            self.year_month_checkbox.setEnabled(True)
            self.year_month_button.setEnabled(True)
            self.month_filter.setEnabled(True)
            self.year_filter.setEnabled(True)
            self.between_dates_checkbox.setEnabled(True)
            self.date2_year_filter_entry.setEnabled(True)
            self.date2_month_filter_entry.setEnabled(True)
            self.date1_month_filter_entry.setEnabled(True)
            self.date1_year_filter_entry.setEnabled(True)
            self.between_dates_button.setEnabled(True)

    def filter_by_transaction(self, transaction_type):
        self.transactions_table.clear()
        transaction_list = TransactionServices.selected_by_transaction_type(
            Session.get_current_user_id(), transaction_type.lower(), '2024')
        for i in transaction_list:
            QTreeWidgetItem(self.transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')
        self.transactions_table.repaint()

    def filter_by_year_month(self, year, month):
        pass

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