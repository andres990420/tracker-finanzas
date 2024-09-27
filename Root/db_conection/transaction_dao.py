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
            DELETE FROM 
                transactions 
            WHERE 
                transaction_id = %s
    '''

    _UPDATE_TRANSACTION = '''
            UPDATE 
                transactions 
            SET 
                transaction_type= %s, category_id= %s, amount= %s, description= %s 
            WHERE 
                transaction_id= %s
    '''

    _SELECT_ONE = '''
        SELECT 
            transaction_type, category_name, amount, transaction_date, description
        FROM 
            transactions
        INNER JOIN 
            categories ON transactions.category_id = categories.category_id
        WHERE 
            transaction_id= %s
        
    '''
    _SELECT_ALL_TRANSACTIONS = '''
        SELECT 
            transaction_id, transaction_type, category_name, amount, transaction_date, description
        FROM 
            transactions
        INNER JOIN 
            categories ON transactions.category_id = categories.category_id
        WHERE 
            user_id = %s
    '''

    _SELECT_EXPENSIVES = '''
        SELECT 
            transaction_id, transaction_type, category_name, amount, transaction_date, description
        FROM 
            transactions
        INNER JOIN 
            categories ON transactions.category_id = categories.category_id
        WHERE 
            user_id = %s AND transaction_type= 'gasto'
    '''

    _SELECT_INCOMES = '''
            SELECT 
                transaction_id,transaction_type, category_name, amount, transaction_date, description
            FROM 
                transactions
            INNER JOIN 
                categories ON transactions.category_id = categories.category_id
            WHERE 
                user_id = %s AND transaction_type = 'ingreso'
        '''

    # POSIBLEMENTE REMOVE ESTA
    _MAX_AND_MIN_EXPENSIVES = '''
            SELECT 
                MAX(amount), MIN(amount) 
            FROM 
                transactions 
            WHERE 
                user_id= %s AND transaction_type= 'gasto'
    '''
    # POSIBLEMENTE REMOVE ESTA
    _MAX_AND_MIN_INCOMES = '''
            SELECT 
                MAX(amount), MIN(amount) 
            FROM 
                transactions 
            WHERE 
                user_id= %s AND transaction_type= 'ingreso'
    '''

    _SELECT_ALL_EXPENSIVES_DATETIME = '''
            SELECT 
                SUM(amount), EXTRACT (MONTH FROM(transaction_date))
            FROM 
                transactions
            WHERE 
                transaction_type = 'gasto' AND user_id= %s AND date_part ('year', transaction_date)= %s
            GROUP BY 
                EXTRACT(MONTH FROM (transaction_date))
    '''

    _SELECT_EXPENSIVES_AND_CATEGORIES = '''
            SELECT 
                SUM(amount), EXTRACT (MONTH FROM(transaction_date)) as "Mes", category_name
            FROM 
                transactions
            INNER JOIN 
                categories ON transactions.category_id= categories.category_id
            WHERE 
                transaction_type = 'gasto' AND user_id= %s AND date_part ('year', transaction_date)= '2024'
                GROUP BY 
                    EXTRACT (MONTH FROM (transaction_date)), category_name
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
            transaction_id = (transaction.transaction_id,)
            cursor.execute(cls._DELETE, transaction_id)
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
    def select_all_transactions(cls, user_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_ALL_TRANSACTIONS, user_id)
            transactions_list = []
            for item in cursor.fetchall():
                x = (item[0], item[1], item[2], str(item[3]), str(item[4]), item[5])
                transactions_list.append(x)
            return transactions_list

    @classmethod
    def select_one_transaction(cls, transaction_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_ONE, transaction_id)
            registro = cursor.fetchone()
            print(registro)

    @classmethod
    def select_all_expensives(cls, user_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_EXPENSIVES, user_id)
            expensive_list = []
            for item in cursor.fetchall():
                x = (item[0], item[1], item[2], str(item[3]), str(item[4]), item[5])
                expensive_list.append(x)
            return expensive_list

    @classmethod
    def select_all_incomes(cls, user_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_INCOMES, user_id)
            incomes_list = []
            for item in cursor.fetchall():
                x = (item[0], item[1], item[2], str(item[3]), str(item[4]), item[5])
                incomes_list.append(x)
            return incomes_list

    # POSIBLEMENTE REMOVE ESTA
    @classmethod
    def max_and_min_expensives_amounts(cls, user_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._MAX_AND_MIN_EXPENSIVES, user_id)
            return cursor.fetchone()

    # POSIBLEMENTE REMOVE ESTA
    @classmethod
    def max_and_min_incomes_amounts(cls, user_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._MAX_AND_MIN_INCOMES, user_id)
            return cursor.fetchone()

    @classmethod
    def select_all_expensives_datetime(cls, user_id, year):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_ALL_EXPENSIVES_DATETIME, [user_id ,year])
            list_expensive_datetime = []
            for item in cursor.fetchall():
                list_expensive_datetime.append(list(item))
            return list_expensive_datetime

    @classmethod
    def select_expensives_and_categories(cls, user_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_EXPENSIVES_AND_CATEGORIES, user_id)
            list_expensive_categories = []
            for item in cursor.fetchall():
                list_expensive_categories.append(list(item))
            return list_expensive_categories


if __name__ == '__main__':

        # TESTING INSERT
        new_transaction = Root.models.transaction.Transaction(user_id=1, transaction_type='gasto',
                                                              category_id=1,
                                                              amount=500,
                                                              transaction_date=datetime.datetime.now(),
                                                              text_description='Compra de lavaplatos')

        # TransactionDao.new_transaction(new_transaction)

        # TESTING DELETE
        # delete_transaction2 = Root.models.transaction.Transaction(transaction_id='5')
        # TransactionDao.delete_transaction(delete_transaction2)

        # TESTING UPDATE
        update_transaction = Root.models.transaction.Transaction(transaction_id=4,
                                                                 transaction_type='ingreso',
                                                                 category_id=2,
                                                                 amount=1500,
                                                                 text_description='Prueba')
        # TransactionDao.update_transaction(update_transaction)

        # TransactionDao.select_one_transaction('4')
        # TransactionDao.select_all_expensives('1')

        (TransactionDao.select_all_expensives_datetime('1','2024'))