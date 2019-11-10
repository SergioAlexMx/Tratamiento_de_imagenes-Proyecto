# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QDir, QUrl, QFileInfo
from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class Ui_MainWindow(object):
    ruta = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 467)

        self.printer = QPrinter()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.painter = QtWidgets.QLabel(self.centralwidget)
        self.painter.setObjectName("painter")
        self.verticalLayout.addWidget(self.painter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 22))
        self.menubar.setObjectName("menubar")
        self.menuAbrir = QtWidgets.QMenu(self.menubar)
        self.menuAbrir.setObjectName("menuAbrir")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir_imagen = QtWidgets.QAction(MainWindow)
        self.actionAbrir_imagen.setObjectName("actionAbrir_imagen")
        self.actionCerrar = QtWidgets.QAction(MainWindow)
        self.actionCerrar.setObjectName("actionCerrar")
        self.actionImprimir = QtWidgets.QAction(MainWindow)
        self.actionImprimir.setObjectName("actionImprimir")
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionAcerca_de_QT = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de_QT.setObjectName("actionAcerca_de_QT")
        self.menuAbrir.addAction(self.actionAbrir_imagen)
        self.menuAbrir.addAction(self.actionImprimir)
        self.menuAbrir.addSeparator()
        self.menuAbrir.addAction(self.actionCerrar)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menuAyuda.addAction(self.actionAcerca_de_QT)
        self.menubar.addAction(self.menuAbrir.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.actionImprimir.setDisabled(True)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionAbrir_imagen.triggered.connect(self.abrirImagen)
        self.actionImprimir.triggered.connect(self.printI)

    def printI(self):
        dialog = QPrintDialog(self.printer, MainWindow)
        if dialog.exec_():
            p = QPainter(self.printer)
            rect = p.viewport()
            size = self.painter.pixmap().size()
            size.scale(rect.size(), Qt.Qt.KeepAspectRatio)
            p.setViewport(rect.x(), rect.y(), size.width(), size.height())
            p.setWindow(self.painter.pixmap().rect())
            p.drawPixmap(0, 0, self.painter.pixmap())


    def abrirImagen(self):
        self.ruta, _ = QFileDialog.getOpenFileName(MainWindow, "Abrir imagen", QDir.currentPath(),
                                                   "Image Files (*.png *.jpg *.bmp *.tif)")
        url = QUrl.fromLocalFile(self.ruta)

        if self.ruta:
            image = QImage(self.ruta)
            if image.isNull(): # En caso de error mostrar un mensaje grafico
                QMessageBox.information(self, "Visualizador de imagenes",
                                        "No se pudo cargar la imagen %s" % (self.ruta))
                return

            self.painter.setPixmap(QPixmap.fromImage(image))
            self.painter.setAlignment(Qt.Qt.AlignCenter)
            MainWindow.setWindowTitle(
                "Editor de imagenes - %s" % (url.fileName()))  # Agregamos el nombre de la imagen al titulo de la imagen
            self.actionImprimir.setDisabled(False) # Activamos el boton de imprimir una vez cargada la imagen
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editor de imagenes - PID"))
        self.menuAbrir.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionAbrir_imagen.setText(_translate("MainWindow", "Abrir imagen"))
        self.actionCerrar.setText(_translate("MainWindow", "Cerrar"))
        self.actionImprimir.setText(_translate("MainWindow", "Imprimir"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))
        self.actionAcerca_de_QT.setText(_translate("MainWindow", "Acerca de QT"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
