class Users:

    def __init__(self, user_id=None, username=None, password=None, email=None):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._email = email

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):
        return f'''
        User Id: {self._user_id}
        Username: {self._username}
        Password: {self._password}
        Email: {self._email}
        '''