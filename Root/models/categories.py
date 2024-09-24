class Categories:

    CATEGORIES = {'GASTOS DEL HOGAR': 1,
                    'TRANSPORTE': 2,
                    'SALUD': 3,
                    'CARIDAD/REGALOS': 4,
                    'DAILY LIVING': 5,
                    'ENTRETENIMIENTO': 6,
                    'OBLIGACIONES': 7,
                    'SUSCRIPCIONES': 8,
                    'OTROS': 9,
                    'GASTOS NO PREDECIBLE': 10,
                    'ALIMENTACIÓN': 11}

if __name__ == '__main__':

   x = Categories().CATEGORIES.keys()
   print(x)

   print(Categories().CATEGORIES.get('OTROS'))