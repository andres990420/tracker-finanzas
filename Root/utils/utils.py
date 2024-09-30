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

    @classmethod
    def get_max_plot(cls, list1, list2):
        if max(list1) > max(list2):
            return max(list1)
        else:
            return max(list2)

    @classmethod
    def join_month_list(cls, list1, list2):
        list3 = []
        for item1 in list1:
            list3.append(item1)
        for item2 in list2:
            if item2 not in list3:
                list3.append(item2)
        return list3


if __name__ == '__main__':
    y = ['1', '2', '3', '5']
    x = ['1', '3', '6', '7']

    # 1, 2, 3, 5, 6, 7
    print(Utils().join_month_list(y, x))
