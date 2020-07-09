import os, sys, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QEvent, QSize
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap, QFileOpenEvent, QIcon, QResizeEvent, QMouseEvent
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QLabel, QSizePolicy, QSizeGrip, QApplication, QFileDialog, QDesktopWidget, QMessageBox, QFrame)

class MainWindow(QWidget):

    def init(self, MAIN):
        super().__init__()
        
        #setting things up
        MAIN.setObjectName("MAIN")
        MAIN.setMinimumSize(500,500)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        MAIN.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'Icon.png'))
        MAIN.setStyleSheet("background-color: gray;")

        self.Frame = QtWidgets.QWidget(MAIN)
        self.Img = QtWidgets.QLabel(self.Frame)
        self.Img.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.Img.setLineWidth(2)
        
        sysRes = QApplication.desktop().screenGeometry()
        self.sysWidth = sysRes.width()
        self.sysHeight = sysRes.height()

        MAIN.setMaximumSize(self.sysWidth,self.sysHeight)
        self.Frame.setMaximumSize(self.sysWidth,self.sysHeight)
        self.Img.setMaximumSize(self.sysWidth,self.sysHeight)

        #Program running
        self.retranslateUi(MAIN)
        
        try:
            if len(sys.argv) <= 1:
                self.file = QFileDialog.getOpenFileName()[0]
            else:
                self.file = str(sys.argv[1]).replace("\\",'/')

            print(self.file)

            self.imgFile = QPixmap(self.file,'r')
            self.resizeWindow(MAIN)
            self.centerWindow()
        
        except:
            self.error = QMessageBox(MAIN)
            self.error.setWindowTitle("NOT AN IMAGE FILE!")
            self.error.setText("Please select an image file and try again.")
            self.error.show()



    def resizeEvent(self, event):

        print('imgFile:',self.imgFile.size())

        self.Frame.setMinimumSize(event.size())
        self.Frame.setMaximumSize(event.size())

        self.imgFile2 = self.imgFile.scaled(self.Frame.maximumWidth(),self.Frame.maximumHeight(), QtCore.Qt.KeepAspectRatio)

        self.Img.setPixmap(self.imgFile2)
        self.Img.adjustSize()

        self.centerWindow()

    def wheelEvent(self, event):
        print(event.angleDelta())

    def mouseMoveEvent(self, event):
        self.Frame.move(event.x(),event.y())

    def retranslateUi(self, MAIN):
        _translate = QtCore.QCoreApplication.translate
        MAIN.setWindowTitle(_translate("MAIN", "IMG Viewer"))

    def centerWindow(self):
        fg = self.Img.frameGeometry()
        cp = self.Frame.frameGeometry().center()
        fg.moveCenter(cp)
        self.Img.move(fg.topLeft())


    def resizeWindow(self, MAIN):
        imgDimensions = str(self.imgFile.size())[str(self.imgFile.size()).index("("):]
        imgWidth = int(imgDimensions[:imgDimensions.index(",")] .replace(",","").replace(" ","").replace("(",""))
        imgHeight = int(imgDimensions[imgDimensions.index(","):].replace(",","").replace(" ","").replace(")",""))

        fileName = self.file[self.file.rindex("/")+1:] + " ({}x{})".format(imgWidth,imgHeight)

        print("\nImage Width:",imgWidth,"\nImage Height:",imgHeight)
        print("\nMaximum Width:",self.sysWidth,"\nMaximum Height:",self.sysHeight)

        # if imgHeight > self.sysHeight:
        #     self.imgFile = self.imgFile.scaled(imgWidth,self.sysHeight, QtCore.Qt.KeepAspectRatio)
        #     imgDimensions = str(self.imgFile.size())[str(self.imgFile.size()).index("("):]
        #     imgWidth = int(imgDimensions[:imgDimensions.index(",")] .replace(",","").replace(" ","").replace("(",""))
        #     imgHeight = int(imgDimensions[imgDimensions.index(","):].replace(",","").replace(" ","").replace(")",""))
        
        # if imgWidth > self.sysWidth:
        #     self.imgFile = self.imgFile.scaled(self.sysWidth, imgHeight, QtCore.Qt.KeepAspectRatio)
        #     imgDimensions = str(self.imgFile.size())[str(self.imgFile.size()).index("("):]
        #     imgWidth = int(imgDimensions[:imgDimensions.index(",")] .replace(",","").replace(" ","").replace("(",""))
        #     imgHeight = int(imgDimensions[imgDimensions.index(","):].replace(",","").replace(" ","").replace(")",""))
    


        # MAIN.setMinimumSize(self.imgFile.width(),self.imgFile.height())
        MAIN.setGeometry(0,0,self.sysWidth,self.sysHeight)
        MAIN.showMaximized()
        self.Frame.setGeometry(0,0,MAIN.width(),MAIN.height())
        self.Img.setPixmap(self.imgFile)
        MAIN.setWindowTitle(fileName)
        self.Img.adjustSize()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MAIN = MainWindow(QtWidgets.QMainWindow())

    # ui = MainWindow(MAIN)
    # ui.show()
    # ui.__init__(MAIN)

    MAIN.init(MAIN)
    sys.exit(app.exec_())