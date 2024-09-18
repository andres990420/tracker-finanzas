import re
from base_logger import log


class Authentificador:

    @classmethod
    def authen_email(cls, email):
        try:
            email_regex = re.compile(r'^[A-Za-z0-9.+_-]+@[A-Za-z0-9._-]+\.[a-zA-Z]*$')
            is_valid_email = False
            if email_regex.match(email):
                is_valid_email = True
            else:
                print('Email  Invalido')
            return is_valid_email
        except Exception as e:
            log.debug('Ocurrio una excepcion', e)

    def authen_password(self, username, password):
        try:
            is_valid_password = False
            if password not in username:
                is_valid_password = True
            else:
                print('La Password no debe ser igual al username')
            return is_valid_password
        except Exception as e:
            log.debug('Ocurrio una excepcion: ', e)


if __name__ == '__main__':

    password = '123'
    username = 'andres123'
    print(Authentificador().authen_password(username, password))