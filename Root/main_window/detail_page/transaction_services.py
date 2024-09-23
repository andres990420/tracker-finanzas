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
    def get_expensives(cls, user_id):
        return TransactionDao().select_all_expensives(user_id)

    @classmethod
    def get_incomes(cls, user_id):
        return TransactionDao().select_all_incomes(user_id)

    @classmethod
    def get_all_transactions(cls, user_id):
        return TransactionDao().select_all_transactions(user_id)

    @classmethod
    def get_max_and_min_expensives(cls, user_id):
        return TransactionDao().max_and_min_expensives_amounts(user_id)

    @classmethod
    def get_max_and_min_expensives_categories(cls, user_id):
        pass

    @classmethod
    def get_max_and_min_incomes(cls, user_id):
        return TransactionDao().max_and_min_incomes_amounts(user_id)

    @classmethod
    def get_max_and_min_incomes_categories(cls, user_id):
        pass

    @classmethod
    def get_all_expensive_datetime(cls, user_id):
        return TransactionDao.select_all_expensives_datetime(user_id)


if __name__ == "__main__":

    print(TransactionServices().get_expensives('1'))