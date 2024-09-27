from PySide6.QtWidgets import \
    QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, QMainWindow, QComboBox
from PySide6.QtCore import Qt
from Root.main_window.dashboard.plots.expensives_categories_plot import ExpensivesCategoriesPlot
from Root.main_window.dashboard.plots.expensives_resume_plot import ExpensivesResumePlot
from Root.main_window.dashboard.plots.incomes_categories_plot import IncomesCategoriesPlot
from Root.main_window.dashboard.plots.incomes_resume_plot import IncomesResumePlot
from Root.main_window.dashboard.plots.transactions_resume_plot import TransactionsResumePlot


class DashboardPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,500)
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

        year_label = QLabel('Year')
        self.filter_layout.addWidget(year_label)

        self.year_combobox = QComboBox()
        self.year_combobox.addItems(['2024', '2023', '2022'])
        self.filter_layout.addWidget(self.year_combobox)


        # month_label = QLabel('Month')
        # self.filter_layout.addWidget(month_label)

        filter_button = QPushButton('FILTRAR')
        self.filter_layout.addWidget(filter_button)
        filter_button.clicked.connect(self.update_chart)
        self.filter_layout.setAlignment(Qt.AlignmentFlag.AlignJustify)

        # Creacion grafico de todos los gastos en el anyo
        self.expensive_resume_plot = ExpensivesResumePlot()
        self.main_layout.addWidget(self.expensive_resume_plot)

        # Creacion grafico de todos los gastos con su division por categoria en el anyo
        self.main_layout.addWidget(ExpensivesCategoriesPlot())

        # Creacion grafico all los ingresos en el anyo
        self.main_layout.addWidget(IncomesResumePlot())

        # Creacion grafico all los ingresos con su categoria en el anyo
        self.main_layout.addWidget(IncomesCategoriesPlot())

        # Cracion grafico ingresos vs gastos en el anyo
        self.main_layout.addWidget(TransactionsResumePlot())

    def update_chart(self):
        self.expensive_resume_plot.update_chart(self.year_combobox.currentText())
        # self.expensive_resume_plot.update()
        # self.expensive_resume_plot.repaint()


if __name__ == "__main__":
    app = QApplication()
    window = DashboardPage()
    window.show()
    app.exec()