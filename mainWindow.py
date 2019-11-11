# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PIL import Image, ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtGui import QPainter, QImage, QPixmap
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.ruta = None
        self.imageOriginal = None
        self.printer = QPrinter()
        self.scaleFactor = 0.0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 490)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 703, 392))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuVista = QtWidgets.QMenu(self.menubar)
        self.menuVista.setObjectName("menuVista")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
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
        self.label_size = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_size.setFont(font)
        self.label_size.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label_size)
        self.dockInfo.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockInfo)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.dock_edicion = QtWidgets.QDockWidget(MainWindow)
        self.dock_edicion.setObjectName("dock_edicion")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.toolBox = QtWidgets.QToolBox(self.dockWidgetContents_2)
        self.toolBox.setObjectName("toolBox")
        self.page_resize = QtWidgets.QWidget()
        self.page_resize.setGeometry(QtCore.QRect(0, 0, 154, 315))
        self.page_resize.setObjectName("page_resize")
        self.formLayout = QtWidgets.QFormLayout(self.page_resize)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.page_resize)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.page_resize)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.checkBox_lock = QtWidgets.QCheckBox(self.page_resize)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_lock.setFont(font)
        self.checkBox_lock.setObjectName("checkBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkBox_lock)
        self.spinAncho = QtWidgets.QSpinBox(self.page_resize)
        self.spinAncho.setObjectName("spinAncho")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.spinAncho)
        self.spinAlto = QtWidgets.QSpinBox(self.page_resize)
        self.spinAlto.setObjectName("spinAlto")

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.spinAlto)
        self.pushAplicarResize = QtWidgets.QPushButton(self.page_resize)
        self.pushAplicarResize.setObjectName("pushAplicarResize")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.pushAplicarResize)
        self.toolBox.addItem(self.page_resize, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 154, 315))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout_4.addWidget(self.toolBox)
        self.dock_edicion.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_edicion)
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
        self.actionDeshacer = QtWidgets.QAction(MainWindow)
        self.actionDeshacer.setObjectName("actionDeshacer")
        self.actionMostrar_original = QtWidgets.QAction(MainWindow)
        self.actionMostrar_original.setObjectName("actionMostrar_original")
        self.menuArchivo.addAction(self.actionAbrir_imagen)
        self.menuArchivo.addAction(self.actionImprimir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionCerrar)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcerca_de_QT)
        self.menuVista.addAction(self.actionZoom_in)
        self.menuVista.addAction(self.actionZoom_out)
        self.menuVista.addSeparator()
        self.menuVista.addAction(self.actionMostrar_original)
        self.menuEditar.addAction(self.actionDeshacer)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionResize)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.spinAlto.setMaximum(100000)
        self.spinAncho.setMaximum(100000)

        self.actionAbrir_imagen.triggered.connect(self.abrirImagen)
        self.actionImprimir.triggered.connect(self.printIm)
        self.actionResize.triggered.connect(self.resizeImagen)

        self.pushAplicarResize.clicked.connect(self.resizeImagen)

        self.checkBox_lock.clicked.connect(self.checkBoxLock)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def checkBoxLock(self):
        if (self.checkBox_lock.isChecked()):
            self.spinAlto.setEnabled(False)
        else:
            self.spinAlto.setEnabled(True)

    def resizeImagen(self):
        if self.ruta is not None:
            self.imageOriginal = QImage(self.ruta)
            if not self.checkBox_lock.isChecked():

                width = int(self.spinAncho.text())
                height = int(self.spinAlto.text())

                im1 = Image.open(self.ruta)
                im1 = im1.resize((width, height))

                qim = ImageQt.ImageQt(im1)

                self.painter.setPixmap(QPixmap.fromImage(qim))
            else:
                im1 = Image.open(self.ruta)

                new_width = int(self.spinAncho.text())

                height = int(im1.height)
                width = int(im1.width)
                new_height = new_width * height / width


                im1 = im1.resize((new_width, int(new_height)))

                qim = ImageQt.ImageQt(im1)

                self.painter.setPixmap(QPixmap.fromImage(qim))
        else:
            QMessageBox.information(MainWindow, "ERROR - No se puede redimencionar",
                                    "Seleccione una imagen desde el menu de Archivo > Abrir")

    def abrirImagen(self):
        self.ruta, _ = QFileDialog.getOpenFileName(MainWindow, "Abrir imagen", QDir.currentPath(),
                                                   "Image Files (*.png *.jpg *.bmp *.tif)")
        url = QUrl.fromLocalFile(self.ruta)
        if self.ruta:
            image = QImage(self.ruta)
            imageP = Image.open(self.ruta)

            if image.isNull():  # En caso de error mostrar un mensaje grafico
                QMessageBox.information(self, "Visualizador de imagenes",
                                        "No se pudo cargar la imagen %s" % (self.ruta))
                return
            self.painter.setPixmap(QPixmap.fromImage(image))
            self.painter.setAlignment(Qt.Qt.AlignCenter)

            self.label_size.setText("Tamaño: %d x %d" % (image.width(), image.height()))
            self.label_nombre.setText("Nombre: %s " % (url.fileName()))
            self.label_tipo.setText("Tipo: %s" % (imageP.mode))
            MainWindow.setWindowTitle(
                "Editor de imagenes - %s" % (url.fileName()))  # Agregamos el nombre de la imagen al titulo de la imagen
            self.spinAlto.setValue(image.height())
            self.spinAncho.setValue(image.width())

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.painter.setText(_translate("MainWindow", "Escoja una imagen presionando Archivo>Abrir imagen"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.menuVista.setTitle(_translate("MainWindow", "Vista"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.dockInfo.setWindowTitle(_translate("MainWindow", "Información"))
        self.label_nombre.setText(_translate("MainWindow", "Nombre: "))
        self.label_tipo.setText(_translate("MainWindow", "Tipo de imagen: "))
        self.label_size.setText(_translate("MainWindow", "Tamaño:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.dock_edicion.setWindowTitle(_translate("MainWindow", "Edición"))
        self.label_2.setText(_translate("MainWindow", "Ancho:"))
        self.label_3.setText(_translate("MainWindow", "Alto:"))
        self.checkBox_lock.setText(_translate("MainWindow", "Mantener relación"))
        self.pushAplicarResize.setText(_translate("MainWindow", "Aplicar"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_resize), _translate("MainWindow", "Reescalar imagen"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2"))
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
        self.actionDeshacer.setText(_translate("MainWindow", "Deshacer"))
        self.actionMostrar_original.setText(_translate("MainWindow", "Mostrar original"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
