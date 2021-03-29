from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PySide2.QtCore import Slot

from mainWindow import Ui_MainWindow

import threading
import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns
import datetime as dt
import sys
import time
import yagmail

sender_email = "monitorcryptosmf@gmail.com"
rec_email = None
porcentaje_bajada_notificar = None
porcentaje_subida_notificar = None
yag = yagmail.SMTP("monitorcryptosmf@gmail.com", "gwwuxwmrqjljmfwf")

currency = "USD"
metric = "Close"
precio_base = 0


start = dt.datetime(2021, 3, 28)
end = dt.datetime.now()

crypto = ''

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_salir.clicked.connect(self.salir)
        self.ui.btn_empezar.clicked.connect(self.empezar)
        self.ui.btn_notificar.clicked.connect(self.notificar)

    @Slot()
    def notificar(self):
        global rec_email
        global porcentaje_subida_notificar
        global porcentaje_bajada_notificar
        if self.ui.le_email.text() != "" and self.ui.le_porcentaje_bajada.text() != "" or self.ui.le_email.text() != "" and self.ui.le_porcentaje_subida.text() != "":
            rec_email = self.ui.le_email.text()
            if self.ui.le_porcentaje_bajada.text() != "":
                porcentaje_bajada_notificar = float(self.ui.le_porcentaje_bajada.text())
            else:
                porcentaje_bajada_notificar = None
            if self.ui.le_porcentaje_subida.text() != "":
                porcentaje_subida_notificar = float(self.ui.le_porcentaje_subida.text())
            else:
                porcentaje_subida_notificar = None
        else:
            self.mostrar_dialog("Debe ingresar un email y almenos un porcentaje de notificación.", "Error")

    @Slot()
    def empezar(self):
        global crypto
        global precio_base
        if self.ui.le_crypto.text() != "" and self.ui.label_precio_base.text() != "":
            crypto = self.ui.le_crypto.text().upper()
            self.ui.label_precio_base.setText("$" + self.ui.le_precio_base.text())
            precio_base = float(self.ui.le_precio_base.text())
            self.ui.btn_empezar.setEnabled(False)
            try:
                thread = threading.Thread(target = self.monitorear_crypto, daemon=True)
                thread.start()
            except:
                self.ui.btn_empezar.setEnabled(True)
                self.ui.label_precio_base.setText("$0")
                self.mostrar_dialog("No se ha podido conseguir la información. Compruebe el nombre de la crypto.", "Error")

    @Slot()
    def salir(self):
        sys.exit(app.exec_())

    def monitorear_crypto(self):
        avisar_positivo = 60
        avisar_negativo = 60
        global rec_email
        global porcentaje_subida_notificar
        global porcentaje_bajada_notificar
        global precio_base
        while True:
            data = web.DataReader(f'{crypto}-{currency}', "yahoo", start, end)
            price = data[[metric]].copy()
            price = price.values[0][0]
            cambio_dolar = price - precio_base
            cambio_porcentaje = (price / precio_base - 1) * 100

            self.ui.label_precio_actual.setText(f'${price}')
            self.ui.label_cambio_dolar.setText(f'${cambio_dolar}')
            self.ui.label_cambio_porcentaje.setText(f'%{cambio_porcentaje}')

            if rec_email != None and avisar_positivo >= 60:
                if porcentaje_subida_notificar != None and cambio_porcentaje > porcentaje_subida_notificar:
                    mensaje = f'La moneda {crypto} ha subido un % {cambio_porcentaje}.'
                    yag.send(
                        to=rec_email,
                        subject="AVISO DE ESTADO POSITIVO",
                        contents=mensaje
                    )
                    avisar_positivo = 0
                elif porcentaje_bajada_notificar != None and cambio_porcentaje < porcentaje_bajada_notificar:
                    mensaje = f'La moneda {crypto} ha bajado un % {cambio_porcentaje}.'
                    yag.send(
                        to=rec_email,
                        subject="AVISO DE ESTADO NEGATIVO",
                        contents=mensaje
                    )
                    avisar_negativo = 0

            avisar_positivo = avisar_positivo + 1
            avisar_negativo = avisar_negativo + 1
            time.sleep(5)

    def mostrar_dialog(self, mensaje, titulo):
        # Sirve para crear un messageBox para mostrar un aviso.
        msg = QMessageBox.about(self, titulo, mensaje)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
