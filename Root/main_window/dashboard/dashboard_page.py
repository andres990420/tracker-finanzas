from PySide6.QtWidgets import \
    QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QScrollArea, QMainWindow
from PySide6.QtCore import Qt
from Root.main_window.dashboard.plots.expensives_categories_plot import ExpensivesCategoriesPlot
from Root.main_window.dashboard.plots.expensives_resume_plot import ExpensivesResumePlot
from Root.main_window.dashboard.plots.incomes_categories_plot import IncomesCategoriesPlot
from Root.main_window.dashboard.plots.incomes_resume_plot import IncomesResumePlot
from Root.main_window.dashboard.plots.transactions_resume_plot import TransactionsResumePlot


class DashboardPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1200,600)

        # Creacion del scroll area
        self.scroll_area = QScrollArea(self)

        # Configurando el scrolla area
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        # Hacer el scroll area el central widget
        self.setCentralWidget(self.scroll_area)

        # Creacion del main widget para scroll area
        self.main_widget = QWidget()

        # Agregando el main widget al scroll area
        self.scroll_area.setWidget(self.main_widget)

        # Creacion del main layout
        self.main_layout = QVBoxLayout()

        #Agregando el main layout al main widget
        self.main_widget.setLayout(self.main_layout)

        # Creacion del Titulo de la pagina
        tittle_label = QLabel('DASHBOARD')
        self.main_layout.addWidget(tittle_label)

        # Creacion del layout para los filtros de busqueda
        self.filter_layout = QHBoxLayout()
        self.main_layout.addLayout(self.filter_layout)

        # Creacion del layout de los graficos de gastos
        self.expensives_resume_layout = QHBoxLayout()
        self.main_layout.addLayout(self.expensives_resume_layout)

        # Creacion del layout de los graficos de ingresos
        self.incomes_resume_layout = QHBoxLayout()
        self.main_layout.addLayout(self.incomes_resume_layout)

        # Creacion de layout con los datos en general
        self.all_transactions_layout = QHBoxLayout()
        self.main_layout.addLayout(self.all_transactions_layout)

        # Creacion de los botones de filtros
        self.createFilterComponents()

        # Creacion de los graficos
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

        # Creacion grafico de todos los gastos en el anyo
        self.expensives_resume_layout.addWidget(ExpensivesResumePlot('2024'))

        # Creacion grafico de todos los gastos con su division por categoria en el anyo
        self.expensives_resume_layout.addWidget(ExpensivesCategoriesPlot())

        # Creacion grafico all los ingresos en el anyo
        self.incomes_resume_layout.addWidget(IncomesResumePlot())

         #Creacion grafico all los ingresos con su categoria en el anyo
        self.incomes_resume_layout.addWidget(IncomesCategoriesPlot())

        # Cracion grafico ingresos vs gastos en el anyo
        self.all_transactions_layout.addWidget(TransactionsResumePlot())


if __name__ == "__main__":
    app = QApplication()
    window = DashboardPage()
    window.show()
    app.exec()