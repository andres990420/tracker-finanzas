from PySide6.QtCharts import QChart, QBarSeries, QBarSet, QBarCategoryAxis, \
    QChartView, QValueAxis
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
from Root.utils.utils import Utils
from Root.login.session import Session
from Root.main_window.detail_page.transaction_services import TransactionServices


class IncomesResumePlot(QWidget):
    def __init__(self, year):
        super().__init__()
        self.set_ingresos = QBarSet('Ingresos')
        self.set_ingresos.setLabelColor('BLACK')
        self.setFixedHeight(400)
        self.year = year

        incomes_list_plot = []
        month_list = []
        incomes_list = TransactionServices().get_all_incomes_dashboard(Session.get_current_user_id(), self.year)
        for i in incomes_list:
            incomes_list_plot.append(float(i[0]))
            month_list.append(int(i[1]))

        self.set_ingresos.append(incomes_list_plot)

        self.series = QBarSeries()
        self.series.setLabelsVisible(True)
        self.series.setLabelsPosition(QBarSeries.LabelsPosition.LabelsOutsideEnd)
        self.series.append(self.set_ingresos)

        self.chart = QChart()
        self.chart.setTitle(f'RESUME INGRESOS {self.year}')
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        self.categories = Utils.get_months(month_list)
        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, max(incomes_list_plot) + 1000)
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

        self.year = year

        self.chart.setTitle(f'RESUME INGRESOS {self.year}')

        self.set_ingresos = QBarSet('INGRESOS')
        self.set_ingresos.setLabelColor('BLACK')

        incomes_list_plot = []
        month_list = []
        incomes_list = TransactionServices().get_all_incomes_dashboard(Session.get_current_user_id(), self.year)
        for i in incomes_list:
            incomes_list_plot.append(float(i[0]))
            month_list.append(int(i[1]))

        self.set_ingresos.append(incomes_list_plot)

        self.categories = Utils().get_months(month_list)

        self.axis_x.append(self.categories)
        self.axis_y.setRange(0, max(incomes_list_plot) + 1000)

        self.series.setLabelsVisible(True)
        self.series.setLabelsPosition(QBarSeries.LabelsPosition.LabelsOutsideEnd)
        self.series.append(self.set_ingresos)

if __name__ == '__main__':

    app = QApplication()
    w = IncomesResumePlot('2024')
    w.show()
    app.exec()