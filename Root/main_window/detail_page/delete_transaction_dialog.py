from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QTreeWidget, \
    QTreeWidgetItem, QVBoxLayout, QComboBox, QMessageBox
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

        categories_filter_label = QLabel('Categories')
        self.main_layout.addWidget(categories_filter_label)

        categories_filter_entry = QComboBox()
        self.main_layout.addWidget(categories_filter_entry)

        data_filter_label = QLabel('DATE')
        self.main_layout.addWidget(data_filter_label)

        date_filter_entry = QComboBox()
        self.main_layout.addWidget(date_filter_entry)

        transactions_table = QTreeWidget()
        transactions_table.setHeaderLabels(['Transaction Type', 'Category Name', 'Amount',
                                            'Transaction Date','Description'])

        self.main_layout.addWidget(transactions_table)
        transactions_list = TransactionServices().get_all_transactions('1')
        for i in transactions_list:
            QTreeWidgetItem(transactions_table, list(i[1:6])).setToolTip(7, f'{i[0]}')

        transactions_table.clicked.connect(lambda: self.selected_transaction(transactions_table))

        delete_button = QPushButton('DELETE')
        self.main_layout.addWidget(delete_button)

        cancel_button = QPushButton('CANCEL')
        self.main_layout.addWidget(cancel_button)

        delete_button.clicked.connect(self.delete_transaction)
        cancel_button.clicked.connect(self.cancel_button_action)

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