# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import imghdr
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.printer = QPrinter()
        self.scaleFactor = 0.0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 395, 353))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.painter = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.painter.setFont(font)
        self.painter.setAlignment(QtCore.Qt.AlignCenter)
        self.painter.setObjectName("painter")
        self.horizontalLayout.addWidget(self.painter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuVista = QtWidgets.QMenu(self.menubar)
        self.menuVista.setObjectName("menuVista")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockInfo = QtWidgets.QDockWidget(MainWindow)
        self.dockInfo.setObjectName("dockInfo")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_nombre = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_nombre.setFont(font)
        self.label_nombre.setObjectName("label_nombre")
        self.verticalLayout_3.addWidget(self.label_nombre)
        self.label_tipo = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_tipo.setFont(font)
        self.label_tipo.setObjectName("label_tipo")
        self.verticalLayout_3.addWidget(self.label_tipo)
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.dockInfo.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockInfo)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionAbrir_imagen = QtWidgets.QAction(MainWindow)
        self.actionAbrir_imagen.setShortcutVisibleInContextMenu(True)
        self.actionAbrir_imagen.setObjectName("actionAbrir_imagen")
        self.actionImprimir = QtWidgets.QAction(MainWindow)
        self.actionImprimir.setObjectName("actionImprimir")
        self.actionCerrar = QtWidgets.QAction(MainWindow)
        self.actionCerrar.setObjectName("actionCerrar")
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionAcerca_de_QT = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de_QT.setObjectName("actionAcerca_de_QT")
        self.actionZoom_in = QtWidgets.QAction(MainWindow)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtWidgets.QAction(MainWindow)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionResize = QtWidgets.QAction(MainWindow)
        self.actionResize.setObjectName("actionResize")
        self.menuArchivo.addAction(self.actionAbrir_imagen)
        self.menuArchivo.addAction(self.actionImprimir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionCerrar)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcerca_de_QT)
        self.menuVista.addAction(self.actionZoom_in)
        self.menuVista.addAction(self.actionZoom_out)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionResize)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.actionAbrir_imagen.triggered.connect(self.abrirImagen)
        self.actionImprimir.triggered.connect(self.printIm)
        self.actionZoom_in.triggered.connect(self.zoomIn)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def normalSize(self):
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0

    def abrirImagen(self):
        self.ruta, _ = QFileDialog.getOpenFileName(MainWindow, "Abrir imagen", QDir.currentPath(),
                                                   "Image Files (*.png *.jpg *.bmp *.tif)")
        url = QUrl.fromLocalFile(self.ruta)
        if self.ruta:
            image = QImage(self.ruta)
            
            if image.isNull():  # En caso de error mostrar un mensaje grafico
                QMessageBox.information(self, "Visualizador de imagenes",
                                        "No se pudo cargar la imagen %s" % (self.ruta))
                return
            self.painter.setPixmap(QPixmap.fromImage(image))
            self.painter.setAlignment(Qt.Qt.AlignCenter)

            MainWindow.setWindowTitle(
                "Editor de imagenes - %s" % (url.fileName()))  # Agregamos el nombre de la imagen al titulo de la imagen
            self.scaleFactor = 1.0

    def printIm(self):
        dialog = QPrintDialog(self.printer, MainWindow)
        if dialog.exec_():
            p = QPainter(self.printer)
            rect = p.viewport()
            size = self.painter.pixmap().size()
            size.scale(rect.size(), Qt.Qt.KeepAspectRatio)
            p.setViewport(rect.x(), rect.y(), size.width(), size.height())
            p.setWindow(self.painter.pixmap().rect())
            p.drawPixmap(0, 0, self.painter.pixmap())

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.painter.resize(self.scaleFactor * self.painter.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
        self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.painter.setText(_translate("MainWindow", "Escoja una imagen presionando Archivo>Abrir imagen"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.menuVista.setTitle(_translate("MainWindow", "Vista"))
        self.dockInfo.setWindowTitle(_translate("MainWindow", "Información"))
        self.label_nombre.setText(_translate("MainWindow", "Nombre: "))
        self.label_tipo.setText(_translate("MainWindow", "Tipo de imagen: "))
        self.label.setText(_translate("MainWindow", "Tamaño:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAbrir_imagen.setText(_translate("MainWindow", "Abrir imagen"))
        self.actionAbrir_imagen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionImprimir.setText(_translate("MainWindow", "Imprimir"))
        self.actionImprimir.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionCerrar.setText(_translate("MainWindow", "Cerrar"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))
        self.actionAcerca_de_QT.setText(_translate("MainWindow", "Acerca de QT"))
        self.actionZoom_in.setText(_translate("MainWindow", "Zoom in"))
        self.actionZoom_out.setText(_translate("MainWindow", "Zoom out"))
        self.actionResize.setText(_translate("MainWindow", "Resize"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
