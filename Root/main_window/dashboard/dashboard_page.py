from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox

from Root.main_window.dashboard.plots.expensives_categories_plot import ExpensivesCategoriesPlot
from Root.main_window.dashboard.plots.expensives_resume_plot import ExpensivesResumePlot
from Root.main_window.dashboard.plots.incomes_categories_plot import IncomesCategoriesPlot
from Root.main_window.dashboard.plots.incomes_resume_plot import IncomesResumePlot
from Root.main_window.dashboard.plots.transactions_resume_plot import TransactionsResumePlot


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1200,600)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.expensives_resume_layout = QHBoxLayout()
        self.incomes_resume_layout = QHBoxLayout()
        self.all_transactions_layout = QHBoxLayout()

        tittle_label = QLabel('DASHBOARD')
        self.main_layout.addWidget(tittle_label)

        self.filter_layout = QHBoxLayout()
        self.main_layout.addLayout(self.filter_layout)

        self.main_layout.addLayout(self.expensives_resume_layout)
        self.main_layout.addLayout(self.incomes_resume_layout)
        self.main_layout.addLayout(self.all_transactions_layout)

        self.createFilterComponents()
        self.createGraphs()

    def createFilterComponents(self):
        year_label = QLabel('Year')
        self.filter_layout.addWidget(year_label)

        year_checkbox = QCheckBox()
        self.filter_layout.addWidget(year_checkbox)

        month_label = QLabel('Month')
        self.filter_layout.addWidget(month_label)

        month_checkbox = QCheckBox()
        self.filter_layout.addWidget(month_checkbox)

    def createGraphs(self):

        self.expensives_resume_layout.addWidget(ExpensivesResumePlot())
        self.expensives_resume_layout.addWidget(ExpensivesCategoriesPlot())

        self.incomes_resume_layout.addWidget(IncomesResumePlot())
        self.incomes_resume_layout.addWidget(IncomesCategoriesPlot())

        self.all_transactions_layout.addWidget(TransactionsResumePlot())


if __name__ == "__main__":
    app = QApplication()
    window = DashboardPage()
    window.show()
    app.exec()