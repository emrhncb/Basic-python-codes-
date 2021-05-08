import sys
from PyQt5.QtWidgets import QWidget,QLineEdit,QLabel,QTextEdit,QApplication,QHBoxLayout,QVBoxLayout,QPushButton,QErrorMessage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail(QWidget):
    def __init__(self):
        super().__init__()
        self.mesaj = MIMEMultipart()
        self.mesaj["From"] = "emir.cebe@gmail.com" #You can change here with your e-mail
        self.init_ui()
    def init_ui(self):
        self.to = QLineEdit()
        self.to_text = QLabel("To Who")
        self.subject = QLineEdit()
        self.subject_text = QLabel("Subject")
        self.text = QTextEdit()
        self.text_text = QLabel("Content")
        self.send = QPushButton("Send")
        self.clean = QPushButton("Clear")


        h_box1 = QHBoxLayout()
        h_box1.addWidget(self.to_text)
        h_box1.addWidget(self.to)
        h_box2 = QHBoxLayout()

        h_box2.addWidget(self.subject_text)
        h_box2.addWidget(self.subject)

        h_box3 = QHBoxLayout()

        h_box3.addWidget(self.text_text)
        h_box3.addWidget(self.text)
        v_box = QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addWidget(self.send)
        v_box.addWidget(self.clean)
        self.send.clicked.connect(self.gonder)
        self.clean.clicked.connect(self.temizle)


        self.setLayout(v_box)
        self.show()
    def gonder(self):
        self.mesaj["To"] = self.to.text()
        self.mesaj["Subject"]  = self.subject.text()

        self.mesaj_govdesi = MIMEText(self.text.toPlainText(),"plain")
        self.mesaj.attach(self.mesaj_govdesi)
        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("emir.cebe@gmail.com", "Your Password") #Put your password here
            mail.sendmail(self.mesaj["From"], self.mesaj["To"], self.mesaj.as_string())
            print("Mail send succesfully")
            mail.close()
        except:
            self.error = QErrorMessage()
            self.error.showMessage("ERROR!")


    def temizle(self):
        self.to.clear()
        self.subject.clear()
        self.text.clear()




app = QApplication(sys.argv)
mail = Mail()
sys.exit(app.exec_())