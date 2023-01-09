import sys
import pyjokes
from PyQt5 import QtWidgets
import bub
import csv
import GoogleTrans2020
class ExampleApp(QtWidgets.QMainWindow, bub.Ui_GenerSmex):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()







if __name__ == '__main__':
    main()