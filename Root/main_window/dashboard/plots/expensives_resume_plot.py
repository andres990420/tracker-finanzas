from PySide6.QtCharts import QChart, QBarSeries, QBarSet, QBarCategoryAxis, \
    QChartView, QValueAxis
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from Root.login.session import Session
from Root.main_window.detail_page.transaction_services import TransactionServices
from Root.utils.utils import Utils


class ExpensivesResumePlot(QWidget):
    def __init__(self, year):
        super().__init__()
        self.setFixedSize(600,600)

        self.set_gastos = QBarSet('Gastos')

        expensives_list = TransactionServices().get_all_expensive_datetime(Session.get_current_user_id())
        expensives_list_plot = []
        month_list = []
        for i in expensives_list:
            expensives_list_plot.append(int(i[0]))
            month_list.append(int(i[1]))

        categories = Utils().get_months(month_list)

        expensives_list_max = 0
        for x in expensives_list:
            if x[0] > expensives_list_max:
                expensives_list_max = x[0] + 1000

        self.set_gastos.append(expensives_list_plot)

        self.series = QBarSeries()
        self.series.append(self.set_gastos)

        self.chart = QChart()
        self.chart.setTitle('RESUMEN GASTOS ' + year)
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        self.categories = categories

        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, round(expensives_list_max))
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(self.axis_y)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.chart_view)


if __name__ == '__main__':

    app = QApplication()
    w = ExpensivesResumePlot('2024')
    w.show()
    app.exec()