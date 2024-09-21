import Root.models.transaction
from Root.db_conection.pool_cursor import PoolCursor
from Root.utils.base_logger import log
import datetime


class TransactionDao:
    _NEW_TRANSACTION = '''
        INSERT INTO      
        transactions(user_id, transaction_type, category_id, amount, transaction_date,description)
        VALUES
        ( %s, %s, %s, %s, %s, %s)
    '''

    _DELETE = '''
            DELETE FROM transactions WHERE transaction_id = %s
    '''

    _UPDATE_TRANSACTION = '''
            UPDATE transactions 
            SET transaction_type= %s, category_id= %s, amount= %s, description= %s 
            WHERE transaction_id= %s
    '''

    _SELECT = '''
        SELECT transaction_type, category_name, amount, transaction_date, description
        FROM transactions
        INNER JOIN categories ON transactions.category_id = categories.category_id
        WHERE transaction_id= %s
        
    '''

    @classmethod
    def new_transaction(cls, transaction):
        with PoolCursor() as cursor:
            new_transaction = (transaction.user_id,
                                transaction.transaction_type,
                                transaction.category_id,
                                transaction.amount,
                                transaction.transaction_date,
                                transaction.text_description)
            cursor.execute(cls._NEW_TRANSACTION, new_transaction)
            log.debug(f'Nueva transaction realizada con exito {new_transaction}')

    @classmethod
    def delete_transaction(cls, transaction):
        with PoolCursor() as cursor:
            cursor.execute(cls._DELETE,transaction.transaction_id)
            log.debug(f'Transaction eliminada con exito')

    @classmethod
    def update_transaction(cls, transaction):
        with PoolCursor() as cursor:
            update_transaction = (transaction.transaction_type,
                                  transaction.category_id,
                                  transaction.amount,
                                  transaction.text_description,
                                  transaction.transaction_id)
            cursor.execute(cls._UPDATE_TRANSACTION, update_transaction)
            log.debug(f'Transaction Actualizad correctamente {update_transaction}')

    @classmethod
    def select_transaction(cls, transaction_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT, transaction_id)
            registro = cursor.fetchone()
            print(registro)


if __name__ == '__main__':

        new_transaction = Root.models.transaction.Transaction(user_id=1, transaction_type='gasto',
                                                              category_id=1,
                                                              amount=500,
                                                              transaction_date=datetime.datetime.now(),
                                                              text_description='Compra de lavaplatos')

        # TransactionDao.new_transaction(new_transaction)
        new_transaction2 = Root.models.transaction.Transaction(transaction_id='5')
        # TransactionDao.delete_transaction(new_transaction2)

        update_transaction = Root.models.transaction.Transaction(transaction_id=4,
                                                                 transaction_type='ingreso',
                                                                 category_id=2,
                                                                 amount=1500,
                                                                 text_description='Prueba')
        # TransactionDao.update_transaction(update_transaction)

        TransactionDao.select_transaction('4')