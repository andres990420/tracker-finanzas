from PySide6.QtCharts import QChart, QBarSeries, QBarSet, QBarCategoryAxis, \
    QChartView, QValueAxis
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import  QWidget, QVBoxLayout, QApplication, QSizePolicy
from Root.main_window.detail_page.transaction_services import TransactionServices
from Root.login.session import Session
from Root.utils.utils import Utils


class ExpensivesCategoriesPlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(400)
        self.year = '2024'
        self.sets = {
            'GASTOS DEL HOGAR': QBarSet('GASTOS DEL HOGAR'),
            'TRANSPORTE': QBarSet('TRANSPORTE'),
            'SALUD': QBarSet('SALUD'),
            'CARIDAD/REGALOS': QBarSet('CARIDAD/REGALOS'),
            'DAILY LIVING': QBarSet('DAILY LIVING'),
            'ENTRETENIMIENTO': QBarSet('ENTRETENIMIENTO'),
            'OBLIGACIONES': QBarSet('OBLIGACIONES'),
            'SUSCRIPCIONES': QBarSet('SUSCRIPCIONES'),
            'OTROS': QBarSet('OTROS'),
            'GASTOS NO PREDECIBLE': QBarSet('GASTOS NO PREDECIBLE'),
            'ALIMENTACIÓN': QBarSet('ALIMENTACIÓN')
        }

        sets_expensives_categories = list(self.sets.keys())
        expensives_categories_list = TransactionServices().get_expensives_categories(Session.get_current_user_id())

        months_list = []
        data_dict = {category:[] for category in sets_expensives_categories}

        for value, month, category in expensives_categories_list:
            if month not in months_list:
                months_list.append(month)
            if category in data_dict:
                data_dict[category].append((month, value))

        for category, values in data_dict.items():
            category_values = {month: 0 for month in months_list}
            for month, value in values:
                category_values[month] = value
            data_dict[category] = list(category_values.values())

        self.series = QBarSeries()

        for category, values in data_dict.items():
            if any(values):
                self.sets[category].append(values)
                self.series.append(self.sets[category])

        self.chart = QChart()
        self.chart.setTitle(f'Gastos por Categoria {self.year}')
        self.chart.addSeries(self.series)
        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignRight)
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        months_list = Utils.get_months(months_list)

        self.categories = months_list
        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axis_x)

        expensives_list_max = max([max(values) for values in data_dict.values() if any(values)])

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, expensives_list_max + 500)
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(self.axis_y)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.chart_view)


if __name__ == '__main__':
    app = QApplication()
    w = ExpensivesCategoriesPlot()
    w.show()
    app.exec()