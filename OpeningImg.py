import os, sys, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QEvent, QSize, QPoint, QByteArray
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap, QFileOpenEvent, QIcon, QResizeEvent, QMouseEvent, QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QLabel, QSizePolicy, QSizeGrip, QApplication, QFileDialog, QDesktopWidget, QMessageBox, QFrame)

class MainWindow(QWidget):

    def init(self, MAIN):
        super().__init__()
        
        #setting things up
        MAIN.setObjectName("MAIN")
        MAIN.setMinimumSize(500,500)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        MAIN.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'Icon.ico'))
        MAIN.setStyleSheet("background-color: gray;")

        self.Frame = QtWidgets.QWidget(MAIN)
        self.Img = QtWidgets.QLabel(self.Frame)
        self.Img.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.Img.setLineWidth(2)
        
        sysRes = QApplication.desktop().screenGeometry()
        self.sysWidth = sysRes.width()
        self.sysHeight = sysRes.height()

        self.Frame.setMaximumSize(self.sysWidth,self.sysHeight)

        self.retranslateUi(MAIN)
        
        try:
            if len(sys.argv) <= 1:
                self.file = QFileDialog.getOpenFileName()[0]
            else:
                self.file = str(sys.argv[1]).replace("\\",'/')

            if self.file[self.file.rindex('.'):] == '.gif':
                self.imgFile = QMovie(self.file, QByteArray(), self)

            else:
                self.imgFile = QPixmap(self.file,'r')

            print(self.file)

            self.resizeWindow(MAIN)
            self.centerWindow()
        
        except Exception as e:
            print(e)
            self.error = QMessageBox(MAIN)
            self.error.setWindowTitle("NOT AN IMAGE FILE!")
            self.error.setText("Please select an image file and try again.")
            self.error.show()

        self.oldPos = QPoint
        self.bg = 1

    def resizeEvent(self, event):

        print(event.size())
        self.Frame.setMinimumSize(event.size())
        self.Frame.setMaximumSize(event.size())


        if self.file[self.file.rindex('.'):] == '.gif':
            pass

        else:
            self.imgFile2 = self.imgFile.scaled(self.Frame.maximumWidth(),self.Frame.maximumHeight(), QtCore.Qt.KeepAspectRatio)
            self.Img.setPixmap(self.imgFile2)

        self.Img.adjustSize()
        self.centerWindow()

    def wheelEvent(self, event):
        self.zoom = event.angleDelta().y()

        if self.file[self.file.rindex('.'):] == '.gif':
            pass


        else:
            if self.Img.size().width() <= self.sysWidth*3 or self.Img.size().width() <= self.sysWidth*3:
                self.imgFile2 = self.imgFile.scaled(self.Img.size().width()+self.zoom, self.Img.size().height()+self.zoom, QtCore.Qt.KeepAspectRatio)
                
            else:
                self.imgFile2 = self.imgFile.scaled(self.Img.size().width()-130, self.Img.size().height()-130, QtCore.Qt.KeepAspectRatio)
        
            self.Img.setPixmap(self.imgFile2)

        self.Img.adjustSize()

        print(self.Img.size())

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.bg += 1
            if self.bg%2 != 0:
                MAIN.setStyleSheet("background-color: gray;")
            else:
                MAIN.setStyleSheet("background-color: white;")
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.Img.move(self.Img.x() + delta.x(), self.Img.y() + delta.y())
        self.oldPos = event.globalPos()

    def retranslateUi(self, MAIN):
        _translate = QtCore.QCoreApplication.translate
        MAIN.setWindowTitle(_translate("MAIN", "IMG Viewer"))

    def centerWindow(self):
        fg = self.Img.frameGeometry()
        cp = self.Frame.frameGeometry().center()
        fg.moveCenter(cp)
        self.Img.move(fg.topLeft())


    def resizeWindow(self, MAIN):
        print("\nMaximum Width:",self.sysWidth,"\nMaximum Height:",self.sysHeight)

        self.Frame.setGeometry(0,0,MAIN.width(),MAIN.height())

        if self.file[self.file.rindex('.'):] == '.gif':
            self.Img.setMovie(self.imgFile)
            self.Img.movie().start()
            self.movie_size = self.imgFile.currentImage().size()
            fileName = self.file[self.file.rindex("/")+1:] + " ({}x{})".format(self.movie_size.width(),self.movie_size.height())
            MAIN.setMinimumSize(self.movie_size.width(),self.movie_size.height())

        else:
            self.Img.setPixmap(self.imgFile)
            self.Img.adjustSize()
            fileName = self.file[self.file.rindex("/")+1:] + " ({}x{})".format(self.imgFile.width(),self.imgFile.height())
        
        MAIN.setGeometry(0,0,self.sysWidth,self.sysHeight)
        MAIN.showMaximized()
        MAIN.setWindowTitle(fileName)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MAIN = MainWindow(QtWidgets.QMainWindow())
    MAIN.init(MAIN)
    sys.exit(app.exec_())