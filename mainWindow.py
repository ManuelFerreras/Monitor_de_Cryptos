# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 386)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 0, 131, 21))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: red;\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 101, 31))
        self.le_crypto = QLineEdit(self.centralwidget)
        self.le_crypto.setObjectName(u"le_crypto")
        self.le_crypto.setGeometry(QRect(10, 60, 371, 20))
        self.btn_empezar = QPushButton(self.centralwidget)
        self.btn_empezar.setObjectName(u"btn_empezar")
        self.btn_empezar.setGeometry(QRect(10, 160, 75, 23))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_empezar.setFont(font1)
        self.btn_empezar.setStyleSheet(u"background-color: green;\n"
"border: none;\n"
"text-transform: uppercase;")
        self.btn_salir = QPushButton(self.centralwidget)
        self.btn_salir.setObjectName(u"btn_salir")
        self.btn_salir.setGeometry(QRect(710, 340, 75, 23))
        self.btn_salir.setFont(font1)
        self.btn_salir.setStyleSheet(u"color: white;\n"
"background-color: red;\n"
"border:none;")
        self.le_precio_base = QLineEdit(self.centralwidget)
        self.le_precio_base.setObjectName(u"le_precio_base")
        self.le_precio_base.setGeometry(QRect(10, 120, 371, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 121, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 210, 61, 16))
        self.label_precio_base = QLabel(self.centralwidget)
        self.label_precio_base.setObjectName(u"label_precio_base")
        self.label_precio_base.setGeometry(QRect(90, 210, 111, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 240, 71, 16))
        self.label_precio_actual = QLabel(self.centralwidget)
        self.label_precio_actual.setObjectName(u"label_precio_actual")
        self.label_precio_actual.setGeometry(QRect(90, 240, 111, 16))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 270, 71, 16))
        self.label_cambio_dolar = QLabel(self.centralwidget)
        self.label_cambio_dolar.setObjectName(u"label_cambio_dolar")
        self.label_cambio_dolar.setGeometry(QRect(90, 270, 111, 16))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 300, 71, 16))
        self.label_cambio_porcentaje = QLabel(self.centralwidget)
        self.label_cambio_porcentaje.setObjectName(u"label_cambio_porcentaje")
        self.label_cambio_porcentaje.setGeometry(QRect(90, 300, 91, 16))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(610, 10, 141, 16))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: blue;")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(570, 40, 47, 13))
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(570, 110, 181, 16))
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(570, 180, 181, 16))
        self.le_porcentaje_subida = QLineEdit(self.centralwidget)
        self.le_porcentaje_subida.setObjectName(u"le_porcentaje_subida")
        self.le_porcentaje_subida.setGeometry(QRect(570, 130, 211, 20))
        self.le_porcentaje_bajada = QLineEdit(self.centralwidget)
        self.le_porcentaje_bajada.setObjectName(u"le_porcentaje_bajada")
        self.le_porcentaje_bajada.setGeometry(QRect(570, 200, 211, 20))
        self.le_email = QLineEdit(self.centralwidget)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setGeometry(QRect(570, 60, 211, 20))
        self.btn_notificar = QPushButton(self.centralwidget)
        self.btn_notificar.setObjectName(u"btn_notificar")
        self.btn_notificar.setGeometry(QRect(570, 240, 75, 23))
        self.btn_notificar.setFont(font1)
        self.btn_notificar.setStyleSheet(u"background-color: green;\n"
"border: none;\n"
"text-transform: uppercase;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Crypto Monitor", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Crypto a Monitoriar:", None))
        self.btn_empezar.setText(QCoreApplication.translate("MainWindow", u"Comenzar", None))
        self.btn_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Precio Base a Monitoriar:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Precio Base:", None))
        self.label_precio_base.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Precio Actual:", None))
        self.label_precio_actual.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cambio ($):", None))
        self.label_cambio_dolar.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Cambio (%):", None))
        self.label_cambio_porcentaje.setText(QCoreApplication.translate("MainWindow", u"%0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Notificar (Opcional)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"A qu\u00e9 porcentaje de subida notificar:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"A qu\u00e9 porcentaje de bajada notificar:", None))
        self.btn_notificar.setText(QCoreApplication.translate("MainWindow", u"NOTIFICAR", None))
    # retranslateUi

