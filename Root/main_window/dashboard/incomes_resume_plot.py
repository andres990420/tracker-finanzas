from PySide6.QtCharts import QChart, QBarSeries, QBarSet, QBarCategoryAxis, \
    QChartView, QValueAxis
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
from Root.main_window.detail_page.transaction_services import TransactionServices


class IncomesResumePlot(QWidget):
    def __init__(self):
        super().__init__()
        self.set_ingresos = QBarSet('Ingresos')
        self.setFixedSize(600, 600)

        incomes_list_plot = []
        incomes_list = TransactionServices().get_incomes('1')
        for i in incomes_list:
            incomes_list_plot.append(float(i[3]))

        self.set_ingresos.append(incomes_list_plot)

        self.series = QBarSeries()
        self.series.append(self.set_ingresos)

        self.chart = QChart()
        self.chart.setTitle('RESUME INGRESOS')
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        self.categories = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre',
                           'Octubre', 'Noviembre', 'Diciembre']
        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axis_x)

        max_and_min_plot = TransactionServices().get_max_and_min_incomes('1')

        self.axis_y = QValueAxis()
        self.axis_y.setRange(max_and_min_plot[1],max_and_min_plot[0])
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(self.axis_y)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.chart_view)


if __name__ == '__main__':

    app = QApplication()
    w = IncomesResumePlot()
    w.show()
    app.exec()