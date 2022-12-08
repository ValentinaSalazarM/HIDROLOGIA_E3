# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

from PySide6.QtWidgets import QFileDialog
from application.app import grafica_tabla

from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

widgets = None
ultimoConsolidado = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        title = "Tratamiento de Aguas Residuales"
        description = "Selección de tecnologías de tratamiento"

        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        # widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)


        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))




        # ///////////////////////////////////////////////////////////////

        # Menú principal - Cantarrana
        widgets.botonMenuCantarrana.clicked.connect(self.pagCantarranaSeleccionada)
        widgets.CantarranaBtnCalcular.clicked.connect(self.calcularCantarrana)
        widgets.CantarranaBtnDescargarGrafica.clicked.connect(self.descargarGraficaCantarrana)

        # Menú principal - Bosa Barreno
        widgets.botonMenuBosa.clicked.connect(self.pagBosaSeleccionada)
        widgets.BosaBtnCalcular.clicked.connect(self.calcularBosa)
        widgets.BosaBtnDescargarGrafica.clicked.connect(self.descargarGraficaBosa)

        
    
    # ///////////////////////////////////////////////////////////////
    # MENÚ PRINCIPAL

    def pagCantarranaSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_Cantarrana)

    def pagBosaSeleccionada (self):
        widgets.stackedWidget.setCurrentWidget(widgets.pagina_Bosa)

    # ///////////////////////////////////////////////////////////////
    def calcularCantarrana (self):
        global ultimoConsolidado
        nivelAgregacion = widgets.CantarranaComboBoxNivel.currentText()
        numIntervalos =  widgets.CantarranaComboBoxIntervalo.text()
        numIntervalos = int (numIntervalos)

        consolidado, minimo, maximo, rango, amplitud, n_datos = grafica_tabla ("Cantarrana", nivelAgregacion, numIntervalos)
        ultimoConsolidado = consolidado
        widgets.CantarranaFieldMinimo.setText(str(round(minimo, 3)))
        widgets.CantarranaFieldMaximo.setText(str(round(maximo, 3)))
        widgets.CantarranaFieldRango.setText(str(round(rango, 0)))
        widgets.CantarranaFieldAmplitud.setText(str(round(amplitud, 3)))
        widgets.CantarranaFieldDatos.setText(str(round(n_datos, 0)))

        widgets.CantarranaTabla.setColumnCount(len(consolidado.columns))
        widgets.CantarranaTabla.setRowCount(len(consolidado))
        widgets.CantarranaTabla.setHorizontalHeaderLabels(consolidado.columns)
        widgets.CantarranaTabla.setColumnWidth(0, 300)
        widgets.CantarranaTabla.setColumnWidth(1, 400)       
                
        for i in range(len(consolidado)):
            for j in range(len(consolidado.columns)):
                item = QTableWidgetItem(str(consolidado.iat[i,j]))
                item.setTextAlignment(Qt.AlignHCenter)
                widgets.CantarranaTabla.setItem(i,j, item)
        if nivelAgregacion == "Diario":
            widgets.CantarranaGrafica.setStyleSheet(u"background-image: url(:images/curvasDuracion/Cantarrana_diario.jpg);")
        elif nivelAgregacion == "Semanal":
            widgets.CantarranaGrafica.setStyleSheet(u"background-image: url(:images/curvasDuracion/Cantarrana_semanal.jpg);")
        elif nivelAgregacion == "Decadal":
            widgets.CantarranaGrafica.setStyleSheet(u"background-image: url(:images/curvasDuracion/Cantarrana_decadal.jpg);")
        elif nivelAgregacion == "Quincenal":
            widgets.CantarranaGrafica.setStyleSheet(u"background-image: url(:images/curvasDuracion/Cantarrana_quincenal.jpg);")
        elif nivelAgregacion == "Mensual":
            widgets.CantarranaGrafica.setStyleSheet(u"background-image: url(:images/curvasDuracion/Cantarrana_mensual.jpg);")
        

    def calcularBosa (self):
        global ultimoConsolidado
        nivelAgregacion = widgets.BosaComboBoxNivel.currentText()
        numIntervalos =  widgets.BosaComboBoxIntervalo.text()
        numIntervalos = int (numIntervalos)
        consolidado, minimo, maximo, rango, amplitud, n_datos = grafica_tabla ("Bosa", nivelAgregacion, numIntervalos)
        ultimoConsolidado = consolidado
        widgets.BosaFieldMinimo.setText(str(round(minimo, 3)))
        widgets.BosaFieldMaximo.setText(str(round(maximo, 3)))
        widgets.BosaFieldRango.setText(str(round(rango, 0)))
        widgets.BosaFieldAmplitud.setText(str(round(amplitud, 3)))
        widgets.BosaFieldDatos.setText(str(round(n_datos, 0)))

        widgets.BosaTabla.setColumnCount(len(consolidado.columns))
        widgets.BosaTabla.setRowCount(len(consolidado))
        widgets.BosaTabla.setHorizontalHeaderLabels(consolidado.columns)
        widgets.BosaTabla.setColumnWidth(0, 300)
        widgets.BosaTabla.setColumnWidth(1, 400)
                            
        for i in range(len(consolidado)):
            for j in range(len(consolidado.columns)):
                item = QTableWidgetItem(str(consolidado.iat[i,j]))
                item.setTextAlignment(Qt.AlignHCenter)
                widgets.BosaTabla.setItem(i,j, item)

        if nivelAgregacion == "diario":
            widgets.BosaGrafica.setStyleSheet(u"background-image: url(:/curvasDuracion/images/curvasDuracion/Bosa_diario.jpg);")
        elif nivelAgregacion == "semanal":
            widgets.BosaGrafica.setStyleSheet(u"background-image: url(:/curvasDuracion/images/curvasDuracion/Bosa_semanal.jpg);")
        elif nivelAgregacion == "decadal":
            widgets.BosaGrafica.setStyleSheet(u"background-image: url(:/curvasDuracion/images/curvasDuracion/Bosa_decadal.jpg);")
        elif nivelAgregacion == "quincenal":
            widgets.BosaGrafica.setStyleSheet(u"background-image: url(:/curvasDuracion/images/curvasDuracion/Bosa_quincenal.jpg);")
        elif nivelAgregacion == "mensual":
            widgets.BosaGrafica.setStyleSheet(u"background-image: url(:/curvasDuracion/images/curvasDuracion/Bosa_mensual.jpg);")
    
    def descargarGraficaCantarrana (self):
        ruta = self.solicitarRuta ()
        ultimoConsolidado.to_excel(ruta + os.path.sep + "Cantarrana.xlsx") 

    def descargarGraficaBosa (self):
        ruta = self.solicitarRuta ()
        ultimoConsolidado.to_excel(ruta + os.path.sep + "Bosa.xlsx") 

    def solicitarRuta (self):
    
        fname = QFileDialog.getExistingDirectory(self, 'Seleccionar una carpeta', '/')

        if fname:
            # Returns pathName with the '/' separators converted to separators that are appropriate for the underlying operating system.
            # On Windows, toNativeSeparators("c:/winnt/system32") returns
            # "c:\winnt\system32".
            fname = QDir.toNativeSeparators(fname)

        return fname
    

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # //////////////////////////////////////////////////////////////

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.MenuPrincipal) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())

