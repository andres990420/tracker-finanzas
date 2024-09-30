from PySide6.QtCharts import QChart, QBarSeries, QBarSet, QBarCategoryAxis, \
    QChartView, QValueAxis
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from Root.utils.utils import Utils
from Root.login.session import Session
from Root.main_window.detail_page.transaction_services import TransactionServices


class TransactionsResumePlot(QWidget):
    def __init__(self, year):
        super().__init__()
        self.setFixedHeight(400)

        self.year = year

        self.set_ingresos = QBarSet('Ingresos')
        self.set_ingresos.setLabelColor('BLUE')
        self.set_gastos = QBarSet('Gastos')
        self.set_gastos.setLabelColor('RED')

        incomes_month_list = []
        incomes_list = TransactionServices().get_all_incomes_dashboard(Session.get_current_user_id(), self.year)
        incomes_data_dict = {data[1]: data[0] for data in incomes_list}
        for i in incomes_list:
            incomes_month_list.append(int(i[1]))

        expensives_month_list = []
        expensives_list = TransactionServices().get_all_expensives_dashboard(Session.get_current_user_id(), self.year)

        expensive_data_dict = {data[1]: data[0] for data in expensives_list}
        for i in expensives_list:
            expensives_month_list.append(int(i[1]))

        month_list_final = Utils.join_month_list(incomes_month_list, expensives_month_list)

        for month in month_list_final:
            if month not in expensive_data_dict:
                expensive_data_dict.update({month: 0})
            if month not in incomes_data_dict:
                incomes_data_dict.update({month: 0})
        for month in month_list_final:
            self.set_gastos.append(expensive_data_dict[month])
            self.set_ingresos.append(incomes_data_dict[month])

        self.series = QBarSeries()
        self.series.setLabelsVisible(True)
        self.series.setLabelsPosition(QBarSeries.LabelsPosition.LabelsOutsideEnd)
        self.series.append(self.set_ingresos)
        self.series.append(self.set_gastos)

        self.chart = QChart()
        self.chart.setTitle(f'INGRESOS VS GASTOS {self.year}')
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        self.categories = Utils.get_months(month_list_final)
        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axis_x)

        max_plot = Utils.get_max_plot(expensive_data_dict.values(), incomes_data_dict.values())

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, max_plot + 1000)
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

        self.chart.setTitle(f'INGRESOS VS GASTOS {self.year}')

        self.set_ingresos = QBarSet('Ingresos')
        self.set_ingresos.setLabelColor('BLUE')
        self.set_gastos = QBarSet('Gastos')
        self.set_gastos.setLabelColor('RED')

        incomes_month_list = []
        incomes_list = TransactionServices().get_all_incomes_dashboard(Session.get_current_user_id(), self.year)
        incomes_data_dict = {data[1]: data[0] for data in incomes_list}
        for i in incomes_list:
            incomes_month_list.append(int(i[1]))

        expensives_month_list = []
        expensives_list = TransactionServices().get_all_expensives_dashboard(Session.get_current_user_id(), self.year)

        expensive_data_dict = {data[1]: data[0] for data in expensives_list}
        for i in expensives_list:
            expensives_month_list.append(int(i[1]))

        month_list_final = Utils.join_month_list(incomes_month_list, expensives_month_list)

        for month in month_list_final:
            if month not in expensive_data_dict:
                expensive_data_dict.update({month: 0})
            if month not in incomes_data_dict:
                incomes_data_dict.update({month: 0})
        for month in month_list_final:
            self.set_gastos.append(expensive_data_dict[month])
            self.set_ingresos.append(incomes_data_dict[month])

        # self.series = QBarSeries()
        self.series.setLabelsVisible(True)
        self.series.setLabelsPosition(QBarSeries.LabelsPosition.LabelsOutsideEnd)
        self.series.append(self.set_ingresos)
        self.series.append(self.set_gastos)

        self.categories = Utils.get_months(month_list_final)
        self.axis_x.append(self.categories)

        max_plot = Utils.get_max_plot(expensive_data_dict.values(), incomes_data_dict.values())
        self.axis_y.setRange(0, max_plot + 1000)

