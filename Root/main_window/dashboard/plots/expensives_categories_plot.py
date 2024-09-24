from PySide6.QtCharts import QChart, QBarSeries, QBarSet, QBarCategoryAxis, \
    QChartView, QValueAxis
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import  QWidget, QVBoxLayout, QApplication, QMainWindow
from Root.main_window.detail_page.transaction_services import TransactionServices
from Root.login.session import Session
from Root.utils.utils import Utils

class ExpensivesCategoriesPlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,500)

        expensives_categories_list_plot = []
        months_list = []
        sets_expensives_categories = []

        expensives_categories_list = TransactionServices().get_expensives_categories(Session.get_current_user_id())
        for i in expensives_categories_list:
            expensives_categories_list_plot.append(float(i[0]))
            months_list.append(i[1])
            sets_expensives_categories.append(i[2])

        print(expensives_categories_list_plot)

        print(sets_expensives_categories)

        self.set_gastos = QBarSet('Gastos')

        for y in expensives_categories_list_plot:
            self.set_gastos.append(y)

        self.series = QBarSeries()

        # for x in sets_expensives_categories:
        #     self.series.append(x)

        self.series.append(self.set_gastos)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        months_list = Utils.get_months(months_list)
        self.categories = months_list
        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axis_x)

        expensives_list_max = 0
        for x in expensives_categories_list:
            if x[0] > expensives_list_max:
                expensives_list_max = x[0] + 100
        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, expensives_list_max)
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