#from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import serial
import time
import traceback, sys
import serial.tools.list_ports
import datetime

from binascii import hexlify
from MainTab import MainTab
from DataAnalysis import DataAnalysis
from Plot import plot
#from itertools import count
#import matplotlib.pyplot as plt



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.initUI()



    def initUI(self):

        self.mainwinxpos = 20
        self.mainwinypos = 20
        self.mainwinwidth = 1280
        self.mainwinheight = 800

        self.tabwidgetxpos = self.mainwinxpos-10
        self.tabwidgetypos = self.mainwinypos-10
        self.tabwidgetwidth =  self.mainwinwidth-50
        self.tabwidgetheight = self.mainwinheight-20

        LoggeddataviewGBposx = 10
        LoggeddataviewGBposy = 20
        LoggeddataviewGBWidth = 545
        LoggeddataviewGBHight = 650


        self.setGeometry(self.mainwinxpos, self.mainwinypos, self.mainwinwidth, self.mainwinheight)
        self.setWindowTitle("Test GUI Ver1.3")


        self.tabwidget = QTabWidget(self)
        self.tabwidget.setGeometry(QRect(self.tabwidgetxpos, self.tabwidgetypos, self.tabwidgetwidth, self.tabwidgetheight))

        self.MainTabObj = MainTab()
        self.DataAnalysis = DataAnalysis(LoggeddataviewGBposx,LoggeddataviewGBposy,LoggeddataviewGBWidth,LoggeddataviewGBHight)
        #self.plot = plot()


        self.tabwidget.addTab(self.MainTabObj,"Main")
        self.tabwidget.addTab(self.DataAnalysis, "Logged Data Analysis")
        #self.tabwidget.addTab(self.plot, "Plot")
        self.tabwidget.setCurrentIndex(0)
        #self.tabwidget.currentChanged.connect(self.TabindexChanged)


        #self.Plot.Plotbutton.clicked.connect(self.Disp)

        #self.tabwidget.addTab(ThirdTab(), "Logged Data")
        #self.Plot.Plotbutton.setCheckable(True)
        #self.Plot.Plotbutton.clicked.connect(self.killthread)


        #firstTab.line.textChanged.connect(secondTab.editor.setPlainText)



if __name__ == '__main__':
    app = QApplication([])
    app.setStyle("Fusion")
    #app.setStyle("cleanlooks")
    #app.setStyle('windows')
    #app.setStyle('cde')
    #app.setStyle('motif')
    #app.setStyle('plastique')
    #app.setStyle("bb10bright")
    #app.setStyle("bb10dark")
    #app.setStyle('windowsvista')
    #aloo =QStyleFactory.keys()
    #print(aloo)

    #app.setStyle("gtk2")
    #app.setStyle('Breeze')
    #app.setStyle('Oxygen')
    #app.setStyle('QtCurve')
    
    
    window = MainWindow()
    window.show()
    app.exec_()
