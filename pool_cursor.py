from conexion import Conexion


class PoolCursor:

    def __init__(self):
        self.conexion = None
        self.cursor = None

    def __enter__(self):
        self.conexion = Conexion.obtenerConexion()
        self.cursor = self.conexion.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.conexion.rollback()
            f'Ocurrio una excepcion: {exc_val} {exc_type} {exc_tb}'
        else:
            self.conexion.commit()
        self.cursor.close()
        Conexion.liberarConexion(self.conexion)