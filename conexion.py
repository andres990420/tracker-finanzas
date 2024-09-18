from psycopg2 import pool
from base_logger import log

class Conexion:

    _DATABASE = 'tracker_database'
    _HOST = '127.0.0.1'
    _PORT = 5432
    _PASSWORD = 'admin'
    _USER = 'postgres'
    _MIN_CONN = 1
    _MAX_CONN = 3
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
               cls._pool = pool.SimpleConnectionPool(minconn=cls._MIN_CONN,
                                                     maxconn=cls._MAX_CONN,
                                                     user=cls._USER,
                                                     port=cls._PORT,
                                                     password=cls._PASSWORD,
                                                     host=cls._HOST,
                                                     database=cls._DATABASE)
               log.debug('Se obtuvo pool correctamente')
               return cls._pool
            except Exception as e:
                log.debug(f'Ocurrio una execption: {e}')

        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)

    @classmethod
    def cerrar_conexino(cls):
        cls.obtenerPool().closeall()
