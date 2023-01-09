import pyjokes
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
import GoogleTrans2020
from PyQt5.QtWidgets import *


class Ui_GenerSmex(object):
    def setupUi(self, GenerSmex):
        self.lbl = QLabel()
        GenerSmex.setObjectName("GenerSmex")
        GenerSmex.resize(643, 645)
        GenerSmex.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(GenerSmex)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.shutk)
        self.verticalLayout_2.addWidget(self.pushButton)
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.Rte = QtWidgets.QSpinBox(self.centralwidget)
        self.Rte.setMaximum(10)
        self.Rte.setObjectName("Rte")
        self.verticalLayout_2.addWidget(self.Rte)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.rte)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.instruk)
        self.verticalLayout_2.addWidget(self.toolButton)
        GenerSmex.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GenerSmex)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 26))
        self.menubar.setObjectName("menubar")
        GenerSmex.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GenerSmex)
        self.statusbar.setObjectName("statusbar")
        GenerSmex.setStatusBar(self.statusbar)

        self.retranslateUi(GenerSmex)
        QtCore.QMetaObject.connectSlotsByName(GenerSmex)

    def shutk(self):
        self.textBrowser.clear()
        joke = pyjokes.get_joke()
        self.textBrowser.append(joke)

    def rte(self):
        shutk = self.textBrowser.toPlainText()
        rte = self.Rte.text()
        datafile = open('Rte.csv', 'a', newline='', encoding="utf8")
        writer = csv.writer(datafile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([rte])
        writer.writerow([shutk])
        datafile.close()
    def instruk(self):
        self.textBrowser.clear()
        file = open("bub.txt","r",encoding="utf8")
        instrukt = file.read()
        self.textBrowser.append(instrukt)
        file.close()




    def retranslateUi(self, GenerSmex):
        _translate = QtCore.QCoreApplication.translate
        GenerSmex.setWindowTitle(_translate("GenerSmex", "GenerSmex"))
        self.pushButton.setWhatsThis(_translate("GenerSmex", "<html><head/><body><p>Эта кнопка генерирует великолепные анекдоты</p></body></html>"))
        self.pushButton.setText(_translate("GenerSmex", "Сгенерировать анекдот"))
        self.textBrowser.setHtml(_translate("GenerSmex", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("GenerSmex", "Оставить оценку"))
        self.toolButton.setText(_translate("GenerSmex", "..."))


