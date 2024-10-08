from Root.db_conection.pool_cursor import PoolCursor
from Root.utils.base_logger import log
from Root.models.users import Users


class UserDao:

    _LOGEAR = "SELECT user_id, username, password_hash FROM users WHERE username=%s AND password_hash=%s"
    _INSERT = 'INSERT INTO users (username, password_hash, email) VALUES (%s, %s, %s)'
    _UPDATE_PASSWORD = 'UPDATE users SET password_hash=%s WHERE user_id= %s'
    _UPDATE_EMAIL = 'UPDATE users SET email=%s WHERE user_id= %s'
    _DELETE = 'DELETE FROM users WHERE user_id=%s'
    _GET_ALL_USERS = 'SELECT * FROM users'

    @classmethod
    def add_user(cls, user):
        with PoolCursor() as cursor:
            user_values = (user.username, user.password, user.email)
            cursor.execute(cls._INSERT, user_values)
            log.debug(f'Usuario creado: {user_values} ')

    @classmethod
    def update_user_password(cls, user):
        with PoolCursor() as cursor:
            user_values = (user.password, user.user_id)
            cursor.execute(cls._UPDATE_PASSWORD, user_values)
            log.debug(f'Password de {user.username} cambiada correctamente')


    @classmethod
    def update_user_email(cls, user):
        with PoolCursor() as cursor:
            user_values = (user.email, user.user_id)
            cursor.execute(cls._UPDATE_EMAIL, user_values)
            log.debug(f'Email de {user.username} cambiada correctamente')

    @classmethod
    def delete_user(cls, user):
        with PoolCursor() as cursor:
            cursor.execute(cls._DELETE, user.user_id)
            log.debug(f'Usuario {user.username} eliminado')

    @classmethod
    def login(cls, user):
        with PoolCursor() as cursor:
            user_values = (user.username, user.password)
            cursor.execute(cls._LOGEAR, user_values)
            registro = cursor.fetchone()
            if registro:
                user.user_id, user.username, user.password = registro
                return Users(user_id=user.user_id, username=user.username, password=user.password)
            else:
                log.debug('No se ha encontrado el usuario')
                return None

    @classmethod
    def get_all_users(cls):
        with PoolCursor() as cursor:
            cursor.execute(cls._GET_ALL_USERS)
            users_id = []
            for i in cursor.fetchall():
                users_id.append(i[0])
            return users_id
