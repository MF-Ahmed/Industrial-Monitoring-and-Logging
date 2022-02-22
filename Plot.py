from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QDate
import matplotlib
import os
matplotlib.use('Qt5Agg')
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
import serial as sr
import time
import traceback, sys
import serial.tools.list_ports
import datetime
import numpy as np
# from MainTab import MainTab
import matplotlib.animation as animation
from matplotlib import style
#from drawnow import *

import logging
from logging.handlers import TimedRotatingFileHandler



class plot(QWidget):
    def __init__(self):

        super().__init__()
        self.plot()


    def plot(self):
        root = tk.Tk()
        root.title('Real time Plot')
        root.configure(background = 'light blue')
        root.geometry("700x500")
        #root.mainloop()

        fig = Figure();
        ax = fig.add_subplot(111)

        ax.set_title('serial data')
        ax.set_xlabel('sample')
        ax.set_ylabel('voltage')
        ax.set_xlim(0,100)
        ax.set_ylim(-0.5,6)
        lines = ax.plot([],[])[0]

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().place(x=10,y=10,width = 600,height=400)
        canvas.draw()
        root.update()



        root.mainloop()






