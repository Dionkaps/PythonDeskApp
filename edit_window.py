from edit_win import *
from sqlite import table_population
import sys

name_list = ['nai','poios','einai']

class EditPage(Ui_EditWindow):

    def __init__(self1,window):
        self1.setupUi(window)
        self1.listWidget.addItems(name_list)

    def edit_window_open(self1):
        self1.window =  QtWidgets.QMainWindow()
        self1.ui = Ui_EditWindow()
        self1.ui.setupUi(self1.window)
        self1.window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self1.window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self1.window.statusBar().setSizeGripEnabled(False) #gia na min einai resizable to parathiro