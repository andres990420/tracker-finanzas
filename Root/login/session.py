from Root.db_conection.user_dao import UserDao
from Root.models.users import Users


class Session:

    current_user = Users(username='andres', password='123', user_id='1')

    @classmethod
    def login(cls, user):
        cls.current_user = user

    @classmethod
    def logout(cls):
        cls.current_user = None

    @classmethod
    def get_current_user(cls):
        return cls.current_user

    @classmethod
    def is_authenticated(cls):
        return cls.current_user is not None

    @classmethod
    def get_current_user_id(cls):
        return str(cls.current_user.user_id)


if __name__ == '__main__':

    user_values = Users(username='andres', password='123')
    user = UserDao.login(user_values)
    Session.login(user)
    print(Session.get_current_user())
    x =  Session.get_current_user()
    print(x.user_id)