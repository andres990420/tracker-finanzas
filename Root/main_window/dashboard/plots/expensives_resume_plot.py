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
        self.setFixedHeight(400)
        self.year = year

        self.set_gastos = QBarSet('Gastos')
        self.set_gastos.setLabelColor('BLACK')

        self.expensives_list = TransactionServices().get_all_expensives_dashboard(
            Session.get_current_user_id(), self.year)
        self.expensives_list_plot = []
        self.month_list = []
        for i in self.expensives_list:
            self.expensives_list_plot.append((int(i[0])))
            self.month_list.append(int(i[1]))

        self.categories_labels = Utils().get_months(self.month_list)

        self.expensives_list_max = 0

        self.set_gastos.append(self.expensives_list_plot)

        self.series = QBarSeries()
        self.series.setLabelsPosition(QBarSeries.LabelsPosition.LabelsOutsideEnd)
        self.series.setLabelsVisible(True)
        self.series.append(self.set_gastos)

        self.chart = QChart()
        self.chart.setTitle('RESUMEN GASTOS ' + self.year)
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        self.categories = self.categories_labels

        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, (max(self.expensives_list_plot) + 1000))
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(self.axis_y)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.chart_view)

    def update_chart(self, year):
        self.axis_x.clear()
        self.series.clear()
        self.expensives_list_plot.clear()
        self.expensives_list.clear()
        self.month_list.clear()

        self.year = year

        self.chart.setTitle(f'RESUMEN GASTOS {self.year}')

        self.set_gastos = QBarSet('Gastos')
        self.set_gastos.setLabelColor('BLACK')

        self.expensives_list = TransactionServices().get_all_expensives_dashboard(
            Session.get_current_user_id(), self.year)
        for i in self.expensives_list:
            self.expensives_list_plot.append(int(i[0]))
            self.month_list.append(int(i[1]))

        for x in self.expensives_list_plot:
            self.set_gastos.append(x)

        new_category = Utils().get_months(self.month_list)

        self.axis_x.append(new_category)

        self.axis_y.setRange(0, max(self.expensives_list_plot) + 1000)

        self.series.setLabelsVisible(True)
        self.series.setLabelsPosition(QBarSeries.LabelsPosition.LabelsOutsideEnd)
        self.series.append(self.set_gastos)


if __name__ == '__main__':

    app = QApplication()
    w = ExpensivesResumePlot()
    w.show()
    app.exec()