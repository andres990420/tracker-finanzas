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
    _SELECT_ALL_TRANSACTIONS_DATETIME_DETAILPAGE = '''
        SELECT 
            transaction_id, transaction_type, category_name, amount, transaction_date, description
        FROM 
            transactions
        INNER JOIN 
            categories ON transactions.category_id = categories.category_id
        WHERE 
            user_id = %s AND 
            date_part ('year', transaction_date)= %s
        ORDER BY
                transaction_date DESC
    '''

    _SELECT_ALL_INCOMES_DATETIME_DETAILPAGE = '''
        SELECT 
            transaction_id,transaction_type, category_name, amount, transaction_date, description
        FROM 
            transactions
        INNER JOIN 
            categories ON transactions.category_id = categories.category_id
        WHERE 
            user_id = %s AND 
            transaction_type = 'ingreso'
            AND date_part ('year', transaction_date)= %s
        ORDER BY
            transaction_date DESC
                '''

    _SELECT_ALL_EXPENSIVES_DATETIME_DETAILPAGE = '''
        SELECT 
            transaction_id,transaction_type, category_name, amount, transaction_date, description
        FROM 
            transactions
        INNER JOIN 
            categories ON transactions.category_id = categories.category_id
        WHERE 
            transaction_type = 'gasto' 
            AND user_id= %s 
            AND date_part('year', transaction_date)= %s
        ORDER BY
            transaction_date DESC
    
    '''
    _SELECT_EXPENSIVES_AND_CATEGORIES_DETAILPAGE = '''
        SELECT 
            transaction_id,transaction_type, category_name, amount, transaction_date, description
        FROM 
            transactions
        INNER JOIN 
            categories ON transactions.category_id= categories.category_id
        WHERE 
            transaction_type = 'gasto' 
            AND user_id= %s 
            AND date_part ('year', transaction_date)= %s
            AND category_name = %s
        ORDER BY
            transaction_date DESC
        '''
    _SELECT_INCOMES_AND_CATEGORIES_DETAILPAGE = '''
        SELECT 
            transaction_id,transaction_type, category_name, amount, transaction_date, description
        FROM 
            transactions
        INNER JOIN 
            categories ON transactions.category_id= categories.category_id
        WHERE 
            transaction_type = 'ingreso' 
            AND user_id= %s 
            AND date_part ('year', transaction_date)= %s
            AND category_name = %s
        ORDER BY
            transaction_date DESC
        '''


    _SELECT_EXPENSIVES_AND_CATEGORIES = '''
            SELECT 
                SUM(amount), EXTRACT (MONTH FROM(transaction_date)) as "Mes", category_name
            FROM 
                transactions
            INNER JOIN 
                categories ON transactions.category_id= categories.category_id
            WHERE 
                transaction_type = 'gasto' 
                AND user_id= %s 
                AND date_part ('year', transaction_date)= '2024'
            GROUP BY 
                EXTRACT (MONTH FROM (transaction_date)), category_name
    '''

    _SELECT_BY_TRANSACTION_TYPE = '''
            SELECT 
                transaction_id,transaction_type, category_name, amount, transaction_date, description
            FROM 
                transactions
            INNER JOIN 
                categories ON transactions.category_id = categories.category_id
            WHERE 
                user_id = %s AND 
                transaction_type = %s
                AND date_part ('year', transaction_date)= %s
            ORDER BY
                transaction_date DESC
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
    def select_all_transactions_datetime(cls, user_id, year):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_ALL_TRANSACTIONS_DATETIME_DETAILPAGE, [user_id, year])
            transactions_list = \
                [(item[0], item[1], item[2], str(item[3]), str(item[4]), item[5]) for item in cursor.fetchall()]
            return transactions_list

    @classmethod
    def select_one_transaction(cls, transaction_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_ONE, transaction_id)
            registro = cursor.fetchone()
            print(registro)

    @classmethod
    def select_all_incomes_datetime_detailpage(cls, user_id, year):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_ALL_INCOMES_DATETIME_DETAILPAGE, [user_id, year])
            list_incomes_datetime = \
                [(item[0], item[1], item[2], str(item[3]), str(item[4]), item[5]) for item in cursor.fetchall()]
            return list_incomes_datetime

    @classmethod
    def select_all_expensives_datetime_detailpage(cls, user_id, year):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_ALL_EXPENSIVES_DATETIME_DETAILPAGE, [user_id, year])
            list_expensive_datetime = \
                [(item[0], item[1], item[2], str(item[3]), str(item[4]), item[5]) for item in cursor.fetchall()]
            return list_expensive_datetime

    @classmethod
    def select_expensives_and_categories_detailpages(cls, user_id, year, category):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_EXPENSIVES_AND_CATEGORIES_DETAILPAGE, [user_id, year, category])
            list_expensive_categories = \
                [(item[0], item[1], item[2], str(item[3]), str(item[4]), item[5]) for item in cursor.fetchall()]
            return list_expensive_categories

    @classmethod
    def select_incomes_and_categories_detailpages(cls, user_id, year, category):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_INCOMES_AND_CATEGORIES_DETAILPAGE, [user_id, year, category])
            list_incomes_categories = \
                [(item[0], item[1], item[2], str(item[3]), str(item[4]), item[5]) for item in cursor.fetchall()]
            return list_incomes_categories

    @classmethod
    def select_expensives_and_categories(cls, user_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_EXPENSIVES_AND_CATEGORIES, user_id)
            list_expensive_categories = [item for item in cursor.fetchall()]
            return list_expensive_categories

    @classmethod
    def select_by_transaction_type(cls, user_id, transaction_type, year):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_BY_TRANSACTION_TYPE, [user_id, transaction_type, year])
            list_transactions = \
                [(item[0], item[1], item[2], str(item[3]), str(item[4]), item[5]) for item in cursor.fetchall()]
            return list_transactions


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

        (TransactionDao.select_by_transaction_type('1', 'ingreso'))