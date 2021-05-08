import requests
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QFileDialog,QLineEdit,QErrorMessage




class Doviz(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        url = "http://data.fixer.io/api/latest?access_key=f8d05bece4f0136d5210293e3e7418c0&format=1"
        request = requests.get(url)
        self.json_verisi = request.json()
        self.ilk_doviz_baslik = QLabel("Firsy Currency")
        self.ilk_döviz = QLineEdit()
        self.ikinci_doviz_baslik = QLabel("Second currency")
        self.ikinci_döviz = QLineEdit()
        self.hesapla = QPushButton("Calcualte")
        self.sonuc = QLabel("")
        self.error = QErrorMessage()
        h_box = QHBoxLayout()
        h_box.addWidget(self.ilk_doviz_baslik)
        h_box.addStretch()
        h_box.addWidget(self.ilk_döviz)

        h_box2 =QHBoxLayout()
        h_box2.addWidget(self.ikinci_doviz_baslik)
        h_box2.addStretch()
        h_box2.addWidget(self.ikinci_döviz)

        v_box =QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addStretch()
        v_box.addLayout(h_box2)
        v_box.addWidget(self.hesapla)
        v_box.addWidget(self.sonuc)
        self.hesapla.clicked.connect(self.hesaplama)
        self.setWindowTitle("Currency Calculation")

        self.setLayout(v_box)
        self.show()
    def hesaplama(self):
        a = self.ilk_döviz.text()
        b = self.ikinci_döviz.text()
        try:
            self.ilk_dovizz = self.json_verisi["rates"][a]
            self.ikinci_dovizz = self.json_verisi["rates"][b]
            sonuc = self.ilk_dovizz/self.ikinci_dovizz
            self.sonuc.setText("1 {} = {} {}".format(a,sonuc,b))
        except KeyError:
            self.error.showMessage("Please enter currencies with capital letters" )



app = QApplication(sys.argv)
doviz = Doviz()
sys.exit(app.exec_())