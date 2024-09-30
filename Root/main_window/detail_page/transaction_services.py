from Root.db_conection.transaction_dao import TransactionDao
from Root.models.transaction import Transaction
import datetime


class TransactionServices:

    @classmethod
    def add_transaction(cls, user_id, transaction_type,category_id, amount, text_description):
        new_transaction = Transaction(user_id=user_id,
                                      transaction_type=transaction_type,
                                      category_id=category_id,
                                      amount=amount,
                                      transaction_date=datetime.datetime.now(),
                                      text_description=text_description)

        TransactionDao().new_transaction(new_transaction)

    @classmethod
    def update_transaction(cls, transaction_id, transaction_type, category_id, amount, text_description):
        update_transaction = Transaction(transaction_id=transaction_id,
                                         transaction_type=transaction_type,
                                         category_id=category_id,
                                         amount=amount,
                                         text_description=text_description)
        TransactionDao().update_transaction(update_transaction)


    @classmethod
    def delete_transaction(cls, transaction_id):
        delete_transaction = Transaction(transaction_id=transaction_id)
        TransactionDao().delete_transaction(delete_transaction)

    @classmethod
    def get_all_transactions(cls, user_id, year):
        return TransactionDao().select_all_transactions_datetime(user_id, year)

    @classmethod
    def selected_by_transaction_type(cls, user_id, transaction_type, year):
        return TransactionDao().select_by_transaction_type(user_id, transaction_type, year)

    @classmethod
    def get_all_expensive_datetime_detailpages(cls, user_id, year):
        return TransactionDao.select_all_expensives_datetime_detailpage(user_id, year)

    @classmethod
    def get_all_incomes_datetime_detailpage(cls, user_id, year):
        return TransactionDao.select_all_incomes_datetime_detailpage(user_id, year)

    @classmethod
    def get_expensives_categories_detailpages(cls, user_id, year, category):
        return TransactionDao.select_expensives_and_categories_detailpages(user_id, year, category)

    @classmethod
    def get_incomes_categories_detailpage(cls, user_id, year, category):
        return TransactionDao.select_incomes_and_categories_detailpages(user_id, year, category)

    # DASHBOARD METHODS

    @classmethod
    def get_all_expensives_dashboard(cls, user_id, year):
        return TransactionDao.select_all_expensives_datetime_dashboard(user_id, year)

    @classmethod
    def get_all_incomes_dashboard(cls, user_id, year):
        return TransactionDao.select_all_incomes_dashboard(user_id, year)

    @classmethod
    def get_expensives_categories_dashboard(cls, user_id, year):
        return TransactionDao.select_expensives_and_categories_dashboard(user_id, year)


if __name__ == "__main__":

    print(TransactionServices().get_all_expensives_dashboard('1'))