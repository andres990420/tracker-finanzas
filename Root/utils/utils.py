class Utils:

    _MONTHS = {'1': 'Enero', '2': 'Febrero', '3': 'Marzo', '4': 'Abril', '5': 'Mayo', '6': 'Junio',
               '7': 'Julio', '8': 'Agosto','9':'Septiembre', '10': 'Octubre',
               '11': 'Noviembre', '12': 'Diciembre'}

    @classmethod
    def get_months(cls, month_list):
        months_for_categories = []
        for i in month_list:
            if cls._MONTHS.get(str(i)) not in months_for_categories:
                months_for_categories.append(cls._MONTHS.get(str(i)))
        return months_for_categories

    @classmethod
    def get_categories(cls, categories_list):
        categories_list_final = []
        for i in categories_list:
            if i not in categories_list_final:
                categories_list_final.append(i)
        return categories_list_final


if __name__ == '__main__':
    test = [['6685.00', '5'], ['1433.00', '7'], ['2873.00', '9'],['1587.00', '10'], ['614.00', '11']]
    x = []
    for y in test:
        x.append(y[1])

    i = [9 , 7, 12, 5, 3, 3]
    print(Utils().get_months(i))