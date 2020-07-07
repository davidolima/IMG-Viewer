import os
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QFileOpenEvent
from PyQt5.QtWidgets import (QWidget, QLabel,QSizePolicy,QSizeGrip,QApplication, QFileDialog)

class Ui_MAIN(object):

    def setupUI(self, MAIN):
        i = QPixmap(QFileDialog.getOpenFileName()[0],'r')

        MAIN.setObjectName("MAIN")
        MAIN.resize(500,500)

        self.centralwidget = QtWidgets.QWidget(MAIN)
        self.centralwidget.setObjectName("centralwidget")
        self.Img = QtWidgets.QLabel(self.centralwidget)

        self.retranslateUi(MAIN)
        
        if QtWidgets.QMainWindow.isVisible == True:
            print("T")
        
        self.Img.setPixmap(i)
        self.centralwidget.setGeometry(0,0,i.width(),i.height())
        MAIN.resize(i.width(),i.height())

        

    def retranslateUi(self, MAIN):
            _translate = QtCore.QCoreApplication.translate
            MAIN.setWindowTitle(_translate("MAIN", "IMG Viewer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QMainWindow()
    ui = Ui_MAIN()
    ui.setupUI(MAIN)
    MAIN.show()
    sys.exit(app.exec_())