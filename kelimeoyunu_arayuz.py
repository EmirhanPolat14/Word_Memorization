import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit

from PyQt5.QtGui import QPixmap, QPalette, QColor, QBrush, QFont

from PyQt5.QtCore import Qt

from PyQt5.QtCore import Qt, QTimer

import requests

import random
import time

class Kelime(QWidget):
    def __init__(self):

         super().__init__()

         self.init_ui()

    def init_ui(self):

        background_image = QPixmap("FB_IMG_1486589153069.jpg")

        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(background_image))

        self.setPalette(palette)

        self.ing_tr = QPushButton("")
        self.ing_tr.setFixedSize(100,66)
        image_path = "ingg.jpg"
        pixmap = QPixmap(image_path)
        self.ing_tr.setStyleSheet(f"QPushButton {{ background-image: url({image_path}); }}")
        self.ing_tr.setFlat(True)
        self.ing_tr.setShortcut("1")


        self.tr_ing = QPushButton("")
        self.tr_ing.setFixedSize(99,66)
        image_path2 = "turkkkk.jpg"
        pixmap2 = QPixmap(image_path2)
        self.tr_ing.setStyleSheet(f"QPushButton {{ background-image: url({image_path2}); }}")
        self.tr_ing.setFlat(True)
        self.tr_ing.setShortcut("2")

        font1 = QFont()
        font1.setBold(True)
        font1.setPointSize(7)
        self.ing_tr.setFont(font1)
        self.tr_ing.setFont(font1)


        self.soru = QLineEdit()
        self.soru.setReadOnly(True)
        self.soru.setMinimumSize(380,60)

        self.cevap = QLineEdit()
        self.cevap.setVisible(False)
        self.cevap.setReadOnly(True)
        self.cevap.setMinimumSize(380,60)


        font = QFont()
        #font.setBold(True)
        font.setPointSize(14)
        self.soru.setFont(font)
        self.cevap.setFont(font)





        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.ing_tr)
        h_box.addWidget(self.tr_ing)
        h_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.soru,alignment=Qt.AlignCenter)
        v_box.addWidget(self.cevap,alignment=Qt.AlignCenter)
        v_box.addLayout(h_box)
        v_box.addStretch()


        self.setLayout(v_box)

        self.setWindowTitle("Kelime Ezber")

        self.setFixedSize(700,600)

        self.ing_tr.clicked.connect(self.ingtur)
        self.tr_ing.clicked.connect(self.turing)

    def ingtur(self):
        sozluk = {}
        with open("kelimeler.txt", "r", encoding="utf-8") as file:
            kelime = []
            for i in file:
                i = i.strip()
                i = i.split(":")
                kelime.append(i)

        for i, j in kelime:
            sozluk[i] = j



        anahtar = random.choice(list(sozluk.keys()))
        deger = sozluk[anahtar]
        self.soru.setText(anahtar)
        QTimer.singleShot(4000, lambda: self.cevap.setVisible(True))
        QTimer.singleShot(4000, lambda: self.cevap.setText(deger))
        self.cevap.setVisible(False)

    def turing(self):
        sozluk = {}
        with open("kelimeler.txt", "r", encoding="utf-8") as file:
            kelime = []
            for i in file:
                i = i.strip()
                i = i.split(":")
                kelime.append(i)

        for i, j in kelime:
            sozluk[i] = j

        anahtar = random.choice(list(sozluk.keys()))
        deger = sozluk[anahtar]
        self.soru.setText(deger)
        QTimer.singleShot(4000, lambda: self.cevap.setVisible(True))
        QTimer.singleShot(4000, lambda: self.cevap.setText(anahtar))
        self.cevap.setVisible(False)





app = QApplication(sys.argv)
kelime_arayuz = Kelime()
kelime_arayuz.show()
sys.exit(app.exec_())

