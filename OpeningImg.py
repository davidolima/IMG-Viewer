import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QEvent, QSize
from PyQt5.QtGui import QPixmap, QFileOpenEvent, QIcon, QResizeEvent
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QLabel,QSizePolicy,QSizeGrip,QApplication, QFileDialog, QDesktopWidget, QMessageBox)

class Ui_MAIN(object):

    def init(self, MAIN):

        #setting things up
        MAIN.setObjectName("MAIN")
        MAIN.setMinimumSize(500,500)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        MAIN.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'Icon.png'))
        MAIN.setStyleSheet("background-color: gray;")

        self.Frame = QtWidgets.QWidget(MAIN)
        self.Frame.setSizeIncrement(QSize(30,30))
        self.Img = QtWidgets.QLabel(self.Frame)
        
        sysRes = QApplication.desktop().screenGeometry()
        self.sysWidth = sysRes.width()
        self.sysHeight = sysRes.height()

        MAIN.setMaximumSize(self.sysWidth,self.sysHeight)
        self.Frame.setMaximumSize(self.sysWidth,self.sysHeight)
        self.Img.setMaximumSize(self.sysWidth,self.sysHeight)

        #Program running
        self.retranslateUi(MAIN)
        
        try:
            self.file = QFileDialog.getOpenFileName()[0]
            self.imgFile = QPixmap(self.file,'r')
            self.resizeWindow(MAIN)
            self.centerWindow(MAIN)
        
        except:
            self.error = QMessageBox(MAIN)
            self.error.setWindowTitle("NOT AN IMAGE FILE!")
            self.error.setText("Please select an image file and try again.")
            self.error.show()


    def retranslateUi(self, MAIN):
        _translate = QtCore.QCoreApplication.translate
        MAIN.setWindowTitle(_translate("MAIN", "IMG Viewer"))

    def centerWindow(self, MAIN):
        rect = MAIN.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(cp)
        # MAIN.move(rect.topLeft())

    def resizeWindow(self, MAIN):

        imgDimensions = str(self.imgFile.size())[str(self.imgFile.size()).index("("):]
        imgWidth = int(imgDimensions[:imgDimensions.index(",")] .replace(",","").replace(" ","").replace("(",""))
        imgHeight = int(imgDimensions[imgDimensions.index(","):].replace(",","").replace(" ","").replace(")",""))

        fileName = self.file[self.file.rindex("/")+1:] + " ({}x{})".format(imgWidth,imgHeight)

        print("\nImage Width:",imgWidth,"\nImage Height:",imgHeight)
        print("\nMaximum Width:",self.sysWidth,"\nMaximum Height:",self.sysHeight)

        if imgHeight > self.sysHeight:
            self.imgFile = self.imgFile.scaled(imgWidth,self.sysHeight, QtCore.Qt.KeepAspectRatio)
            imgDimensions = str(self.imgFile.size())[str(self.imgFile.size()).index("("):]
            imgWidth = int(imgDimensions[:imgDimensions.index(",")] .replace(",","").replace(" ","").replace("(",""))
            imgHeight = int(imgDimensions[imgDimensions.index(","):].replace(",","").replace(" ","").replace(")",""))
        
        if imgWidth > self.sysWidth:
            self.imgFile = self.imgFile.scaled(self.sysWidth, imgHeight, QtCore.Qt.KeepAspectRatio)
            imgDimensions = str(self.imgFile.size())[str(self.imgFile.size()).index("("):]
            imgWidth = int(imgDimensions[:imgDimensions.index(",")] .replace(",","").replace(" ","").replace("(",""))
            imgHeight = int(imgDimensions[imgDimensions.index(","):].replace(",","").replace(" ","").replace(")",""))
    


        MAIN.setMinimumSize(self.imgFile.width(),self.imgFile.height())
        MAIN.showMaximized()
        self.Img.setPixmap(self.imgFile)
        rect = self.Frame.frameGeometry()
        cp = MAIN.frameGeometry().center()
        rect.moveCenter(cp)
        self.Frame.move(rect.topLeft())

        MAIN.setWindowTitle(fileName)
        # MAIN.resize(self.sysWidth,self.sysHeight)
        self.Frame.setGeometry(0,0,imgWidth,self.sysHeight)
        self.Img.adjustSize()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QMainWindow()
    ui = Ui_MAIN()
    ui.init(MAIN)
    MAIN.show()
    sys.exit(app.exec_())