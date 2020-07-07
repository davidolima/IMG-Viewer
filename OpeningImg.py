import os, ctypes
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QFileOpenEvent
from PyQt5.QtWidgets import (QWidget, QLabel,QSizePolicy,QSizeGrip,QApplication, QFileDialog)

class Ui_MAIN(object):

    def setupUI(self, MAIN):

        MAIN.setObjectName("MAIN")
        MAIN.resize(500,500)

        self.centralwidget = QtWidgets.QWidget(MAIN)
        self.centralwidget.setObjectName("centralwidget")
        self.Img = QtWidgets.QLabel(self.centralwidget)

        self.retranslateUi(MAIN)
        
        user32 = ctypes.windll.user32
        MAIN.setMaximumSize(user32.GetSystemMetrics(78),user32.GetSystemMetrics(79))
        self.centralwidget.setMaximumSize(user32.GetSystemMetrics(78),user32.GetSystemMetrics(79))
        self.Img.setMaximumSize(user32.GetSystemMetrics(78),user32.GetSystemMetrics(79))

        i = QPixmap(QFileDialog.getOpenFileName()[0],'r')
        
        imgDimensions = str(i.size())[str(i.size()).index("("):]
        print(imgDimensions)
        imgWidth = int(imgDimensions[:imgDimensions.index(",")] .replace(",","").replace(" ","").replace("(",""))
        imgHeight = int(imgDimensions[imgDimensions.index(","):].replace(",","").replace(" ","").replace(")",""))

        print("\nImage Width:",imgWidth,"\nImage Height:",imgHeight)

        mwDimensions = str(self.Img.maximumSize())[str(self.Img.maximumSize()).index("(")+1:]
        mwWidth = int(mwDimensions[:mwDimensions.index(",")].replace(",","").replace(" ","").replace(" ","").replace(")",""))
        mwHeight = int(mwDimensions[mwDimensions.index(","):].replace(",","").replace(" ","").replace(" ","").replace(")",""))

        print("\nMaximum Width",mwWidth,"\nMaximum Height:",mwHeight)

        if imgHeight > mwHeight and imgWidth > mwWidth:
            i = i.scaled(mwWidth,mwHeight)
        
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