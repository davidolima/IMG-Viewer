import os, ctypes
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QFileOpenEvent, QIcon
from PyQt5.QtWidgets import (QWidget, QLabel,QSizePolicy,QSizeGrip,QApplication, QFileDialog)

class Ui_MAIN(object):

    def setupUI(self, MAIN):
        MAIN.setObjectName("MAIN")
        MAIN.resize(500,500)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        MAIN.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'Icon.png'))



        self.centralwidget = QtWidgets.QWidget(MAIN)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.Img = QtWidgets.QLabel(self.centralwidget)
        self.Img.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

        self.retranslateUi(MAIN)
        
        user32 = ctypes.windll.user32
        MAIN.setMaximumSize(user32.GetSystemMetrics(78),user32.GetSystemMetrics(79))
        self.centralwidget.setMaximumSize(user32.GetSystemMetrics(78),user32.GetSystemMetrics(79))
        self.Img.setMaximumSize(user32.GetSystemMetrics(78),user32.GetSystemMetrics(79))

        self.file = QFileDialog.getOpenFileName()[0]
        self.imgFile = QPixmap(self.file,'r')
        
        imgDimensions = str(self.imgFile.size())[str(self.imgFile.size()).index("("):]
        print(imgDimensions)
        imgWidth = int(imgDimensions[:imgDimensions.index(",")] .replace(",","").replace(" ","").replace("(",""))
        imgHeight = int(imgDimensions[imgDimensions.index(","):].replace(",","").replace(" ","").replace(")",""))

        fileName = self.file[self.file.rindex("/")+1:] + " ({}x{})".format(imgWidth,imgHeight)

        MAIN.setWindowTitle(fileName)
        print("\nImage Width:",imgWidth,"\nImage Height:",imgHeight)

        mwDimensions = str(self.Img.maximumSize())[str(self.Img.maximumSize()).index("(")+1:]
        mwWidth = int(mwDimensions[:mwDimensions.index(",")].replace(",","").replace(" ","").replace(" ","").replace(")",""))
        mwHeight = int(mwDimensions[mwDimensions.index(","):].replace(",","").replace(" ","").replace(" ","").replace(")",""))

        print("\nMaximum Width",mwWidth,"\nMaximum Height:",mwHeight)

        if imgHeight > mwHeight:
            self.imgFile = self.imgFile.scaled(self.imgFile.width(),mwHeight)
        
        if imgWidth > mwWidth:
            self.imgFile = self.imgFile.scaled(mwWidth, self.imgFile.height())

        self.Img.setPixmap(self.imgFile)
        self.centralwidget.setGeometry(0,0,self.imgFile.width(),self.imgFile.height())
        MAIN.resize(self.imgFile.width(),self.imgFile.height())


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