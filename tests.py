import random
import datetime
from Root.db_conection.user_dao import UserDao
from Root.models.users import Users
from Root.models.transaction import Transaction
from Root.db_conection.transaction_dao import TransactionDao
from Root.main_window.detail_page.transaction_services import TransactionServices
from Root.models.categories import Categories


users = ['Pedro','Juan','Maria','Camila']

passwords = ['123', '345', '678', '901']

emails = ['pedro@mail.com', 'juan@mail.com', 'maria@mail.com', 'camila@mail.com']

tipo_transacciones = ['ingreso', 'gasto']

categorias_id = [1,2,3,4,5,6,7,8,9,10,11]

descripcion = ['Compra', 'Venta', 'Comida', 'Higiene', 'Ocio', 'Pago']


def creating_new_user():

    for i in range(len(users)):

        usuario = Users(username=users[i], password=passwords[i], email=emails[i])
        UserDao.add_user(usuario)

def creating_new_transactions():
   list_users = UserDao.get_all_users()
   for i in list_users:
       for x in range(90):
           amount = random.randint(50,1500)
           fecha_random = datetime.date(random.randint(2021, 2024),random.randint(3, 12),random.randint(1, 30))
           new_transaction = Transaction(transaction_id=None,
                                         user_id=i,
                                         transaction_type=tipo_transacciones[random.randint(0,1)],
                                         category_id=categorias_id[random.randint(0,10)],
                                         amount= amount,
                                         transaction_date=fecha_random,
                                         text_description=descripcion[random.randint(0,5)])

           TransactionDao.new_transaction(new_transaction)

# creating_new_user()

# creating_new_transactions()

