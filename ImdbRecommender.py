from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit
from PyQt5.QtGui import QPixmap,QImage
import sys
import requests
from bs4 import BeautifulSoup
import urllib
import random

class Imdb(QWidget):
    def __init__(self):
        super().__init__()

        url = "https://www.imdb.com/chart/top"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")
        self.basliklar = soup.find_all("td", {"class": "titleColumn"})
        self.ratingler = soup.find_all("td", {"class": "ratingColumn imdbRating"})
        self.photo = soup.find_all("img")
        self.links = []
        for link in self.photo:
            self.links.append(link.get("src"))
        self.init_ui()




    def init_ui(self):
        self.box = QLineEdit()
        self.rating = QPushButton("Search(rating)")
        self.name = QPushButton("Search(name)")
        self.order = QPushButton("Search in order")
        self.label = QLabel("")
        self.photo = QLabel(self)
        self.random = QPushButton("Let me decide!")

        v_box = QVBoxLayout()
        v_box.addWidget(self.box)
        h_box = QHBoxLayout()
        h_box.addWidget(self.rating)
        h_box.addWidget(self.name)
        h_box.addWidget(self.order)
        h_box.addWidget(self.random)
        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.photo)
        h_box2.addWidget(self.label)

        v_box2 = QVBoxLayout()
        v_box2.addLayout(v_box)
        v_box2.addLayout(h_box)
        v_box2.addLayout(h_box2)
        self.setLayout(v_box2)
        self.setWindowTitle("What will you watch?")
        self.rating.clicked.connect(self.search_r)
        self.name.clicked.connect(self.search_n)
        self.order.clicked.connect(self.search_o)
        self.random.clicked.connect(self.random_)
        self.show()
    def search_r(self):
        rating_ = float(self.box.text())
        baslist = []
        ratlist = []
        linklist = []
        for baslik, rating,photo in zip(self.basliklar, self.ratingler,self.links):

            baslik = baslik.text
            rating = rating.text
            baslik = baslik.strip()
            baslik = baslik.replace("\n", "")
            rating = rating.strip()
            rating = rating.replace("\n", "")
            if float(rating) == rating_ :

                baslist.append(baslik)

                ratlist.append(rating)

                linklist.append(photo)
        x = random.randint(0, len(baslist) - 1)
        data = urllib.request.urlopen(linklist[x]).read()
        image = QImage()
        image.loadFromData(data)
        self.label.setText("{}\nRating  {}".format(baslist[x], ratlist[x]))
        self.photo.setPixmap(QPixmap(image))

    def search_n(self):
        name = self.box.text()

        for baslik,rating,photo in zip(self.basliklar,self.ratingler,self.links):




            baslik = baslik.text
            rating = rating.text
            baslik = baslik.strip()
            baslik = baslik.replace("\n", "")
            rating = rating.strip()
            rating = rating.replace("\n", "")
            if baslik[10:-6] == name or baslik[9:-6] == name or baslik[8:-6] == name:
                data = urllib.request.urlopen(photo).read()
                image = QImage()
                image.loadFromData(data)
                self.label.setText("{}\nRating  {}".format(baslik, rating))
                self.photo.setPixmap(QPixmap(image))
    def search_o(self):
        order = self.box.text()
        for baslik,rating,photo in zip(self.basliklar,self.ratingler,self.links):
            baslik = baslik.text
            rating = rating.text
            baslik = baslik.strip()
            baslik = baslik.replace("\n", "")
            rating = rating.strip()
            rating = rating.replace("\n", "")
            if baslik[:4] == order +"." or baslik[:3] == order +"." or baslik[:2] == order+".":
                data = urllib.request.urlopen(photo).read()
                image = QImage()
                image.loadFromData(data)
                self.label.setText("{}\nRating  {}".format(baslik, rating))
                self.photo.setPixmap(QPixmap(image))
    def random_(self):
        x = random.randint(0,249)
        data = urllib.request.urlopen(self.links[x]).read()
        image = QImage()
        image.loadFromData(data)
        self.label.setText("{}\n  {}".format(self.basliklar[x], self.ratingler[x]))
        self.photo.setPixmap(QPixmap(image))



app  = QApplication(sys.argv)
imdb = Imdb()
sys.exit(app.exec_())