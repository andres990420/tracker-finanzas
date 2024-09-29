from Root.db_conection.pool_cursor import PoolCursor


class TransactionDaoDashboard:

    _SELECT_EXPENSIVES_DASHBOARD = '''
            SELECT 
                transaction_id, transaction_type, category_name, amount, transaction_date, description
            FROM 
                transactions
            INNER JOIN 
                categories ON transactions.category_id = categories.category_id
            WHERE 
                user_id = %s AND transaction_type= 'gasto'
        '''

    _SELECT_ALL_EXPENSIVES_DATETIME_DASHBOARD = '''
                SELECT 
                    SUM(amount), EXTRACT (MONTH FROM(transaction_date))
                FROM 
                    transactions
                WHERE 
                    transaction_type = 'gasto' AND user_id= %s AND date_part ('year', transaction_date)= %s
                GROUP BY 
                    EXTRACT(MONTH FROM (transaction_date))

        '''

    _SELECT_INCOMES_DASHBOARD = '''
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

    @classmethod
    def select_all_expensives_dashboard(cls, user_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_EXPENSIVES_DASHBOARD, user_id)
            expensive_list = []
            for item in cursor.fetchall():
                x = (item[0], item[1], item[2], str(item[3]), str(item[4]), item[5])
                expensive_list.append(x)
            return expensive_list

    @classmethod
    def select_all_expensives_datetime_dashboard(cls, user_id, year):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_ALL_EXPENSIVES_DATETIME_DASHBOARD, [user_id, year])
            list_expensive_datetime = []
            for item in cursor.fetchall():
                list_expensive_datetime.append(list(item))
            return list_expensive_datetime

    @classmethod
    def select_all_incomes_dashboard(cls, user_id, year):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_INCOMES_DASHBOARD, [user_id, year])
            incomes_list = []
            for item in cursor.fetchall():
                x = (item[0], item[1], item[2], str(item[3]), str(item[4]), item[5])
                incomes_list.append(x)
            return incomes_list