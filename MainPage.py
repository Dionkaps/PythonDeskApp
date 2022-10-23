from asyncio.windows_events import NULL
from audioop import reverse
from cgitb import text
from re import X
from turtle import right
from PythonApp import *
from sqlite import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QDesktopWidget, QApplication, QMessageBox,  QListWidgetItem
from AppOpener import run
from edit_window import *
from PyQt5.QtCore import *
import sys
from windows_tools.installed_software import get_installed_software

counter = 0
flag_end = False
animation_dist = 600
animation_duration = 600 #in ms
update_name = ''
name = []

_translate = QtCore.QCoreApplication.translate


class MainPage(Ui_MainWindow):

    try:
        conn = sqlite3.connect('javatpoint.db')
    except:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Could't connect to the database")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()  # this will show our messagebox

    def butt_creation():  # not ass creation
        data = conn.execute("SELECT DISTINCT NAME FROM UserData")
        for row in data:
            name.append(row[0])

    butt_creation()

    def __init__(self, window):
        self.setupUi(window)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # gia na min einai resizable to parathiro
        MainWindow.statusBar().setSizeGripEnabled(False)

        self.testButton.clicked.connect(self.right_clicked)
        self.testButton_2.clicked.connect(self.left_clicked)
        # Anathesi function se button
        self.addButton.clicked.connect(self.add_up)
        self.settingsUpButton.clicked.connect(self.settings_up)
        self.settingsDownButton.clicked.connect(self.settings_down)
        self.deleteButton.clicked.connect(self.delete_item)
        self.addDownButton.clicked.connect(self.add_down)
        self.editButton.clicked.connect(self.edit_up)
        self.updateDownButton.clicked.connect(self.edit_down)
        self.confirmButton.clicked.connect(self.confirm_insert)
        self.updateButton.clicked.connect(self.update)
        self.update_deleteButton.clicked.connect(self.update_delete)

        global flag_end

        if(int((len(name)/5)-0.2)==counter): #Eksalifei to bug pou emfanize keni selida xwris koumpia otan teleiwne o pinakas
            self.testButton.hide()

        if (len(name) == 0+counter*5):
            self.testButton.hide()
            flag_end = True
        elif (flag_end == False):
            self.booton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.booton.setMinimumSize(QtCore.QSize(80, 80))
            self.booton.setMaximumSize(QtCore.QSize(80, 80))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.booton.setFont(font)
            self.booton.setObjectName("booton")
            self.booton.setText(_translate("MainWindow", name[0+counter*5]))
            self.horizontalLayout_2.addWidget(self.booton)
            self.booton.clicked.connect(
                self.click_ass1)  # Button event onClick

        if (len(name) == 1+counter*5):
            self.testButton.hide()
            flag_end = True
        elif (flag_end == False):
            self.booton1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.booton1.setMinimumSize(QtCore.QSize(80, 80))
            self.booton1.setMaximumSize(QtCore.QSize(80, 80))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.booton1.setFont(font)
            self.booton1.setObjectName("booton1")
            self.booton1.setText(_translate("MainWindow", name[1+counter*5]))
            self.horizontalLayout_2.addWidget(self.booton1)
            self.booton1.clicked.connect(
                self.click_ass2)  # Button event onClick

        if (len(name) == 2+counter*5):
            self.testButton.hide()
            flag_end = True
        elif (flag_end == False):
            self.booton2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.booton2.setMinimumSize(QtCore.QSize(80, 80))
            self.booton2.setMaximumSize(QtCore.QSize(80, 80))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.booton2.setFont(font)
            self.booton2.setObjectName("booton2")
            self.booton2.setText(_translate("MainWindow", name[2+counter*5]))
            self.horizontalLayout_2.addWidget(self.booton2)
            self.booton2.clicked.connect(
                self.click_ass3)  # Button event onClick

        if (len(name) == 3+counter*5):
            self.testButton.hide()
            flag_end = True
        elif (flag_end == False):
            self.booton3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.booton3.setMinimumSize(QtCore.QSize(80, 80))
            self.booton3.setMaximumSize(QtCore.QSize(80, 80))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.booton3.setFont(font)
            self.booton3.setObjectName("booton3")
            self.booton3.setText(_translate("MainWindow", name[3+counter*5]))
            self.horizontalLayout_2.addWidget(self.booton3)
            self.booton3.clicked.connect(
                self.click_ass4)  # Button event onClick

        if (len(name) == 4+counter*5):
            self.testButton.hide()
            flag_end = True
        elif (flag_end == False):
            self.booton4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.booton4.setMinimumSize(QtCore.QSize(80, 80))
            self.booton4.setMaximumSize(QtCore.QSize(80, 80))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.booton4.setFont(font)
            self.booton4.setObjectName("booton4")
            self.booton4.setText(_translate("MainWindow", name[4+counter*5]))
            self.horizontalLayout_2.addWidget(self.booton4)
            self.booton4.clicked.connect(
                self.click_ass5)  # Button event onClick

        self.testButton_2.hide()  # krivei to aristero velos me tin enarksi tis efarmogis

    def left_clicked(self):
        global counter
        if (counter == 1):
            self.testButton_2.hide()
        counter = counter - 2  # -2 giati me to pou kaleitai i right clicked exei +1
        global flag_end
        flag_end = False
        self.right_clicked()
        if (len(name) != counter*5):
            self.testButton.show()

    def refresh_icons(self):
        global flag_end
        global counter
        global name
        if(int((len(name)/5)-0.2)==counter):  #Eksalifei to bug pou emfanize keni selida xwris koumpia otan teleiwne o pinakas
            self.testButton.hide()
        if (len(name) == 0+counter*5):
            self.testButton.hide()
            flag_end = True
        elif (flag_end == False):
            self.booton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.booton.setMinimumSize(QtCore.QSize(80, 80))
            self.booton.setMaximumSize(QtCore.QSize(80, 80))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.booton.setFont(font)
            self.booton.setObjectName("booton")
            self.booton.setText(_translate("MainWindow", name[0+counter*5]))
            self.horizontalLayout_2.addWidget(self.booton)
            self.booton.clicked.connect(
                self.click_ass1)  # Button event onClick

        if (len(name) == 1+counter*5):
            self.testButton.hide()
            flag_end = True
        elif (flag_end == False):
            self.booton1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.booton1.setMinimumSize(QtCore.QSize(80, 80))
            self.booton1.setMaximumSize(QtCore.QSize(80, 80))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.booton1.setFont(font)
            self.booton1.setObjectName("booton1")
            self.booton1.setText(_translate("MainWindow", name[1+counter*5]))
            self.horizontalLayout_2.addWidget(self.booton1)
            self.booton1.clicked.connect(
                self.click_ass2)  # Button event onClick

        if (len(name) == 2+counter*5):
            self.testButton.hide()
            flag_end = True
        elif (flag_end == False):
            self.booton2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.booton2.setMinimumSize(QtCore.QSize(80, 80))
            self.booton2.setMaximumSize(QtCore.QSize(80, 80))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.booton2.setFont(font)
            self.booton2.setObjectName("booton2")
            self.booton2.setText(_translate("MainWindow", name[2+counter*5]))
            self.horizontalLayout_2.addWidget(self.booton2)
            self.booton2.clicked.connect(
                self.click_ass3)  # Button event onClick

        if (len(name) == 3+counter*5):
            self.testButton.hide()
            flag_end = True
        elif (flag_end == False):
            self.booton3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.booton3.setMinimumSize(QtCore.QSize(80, 80))
            self.booton3.setMaximumSize(QtCore.QSize(80, 80))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.booton3.setFont(font)
            self.booton3.setObjectName("booton3")
            self.booton3.setText(_translate("MainWindow", name[3+counter*5]))
            self.horizontalLayout_2.addWidget(self.booton3)
            self.booton3.clicked.connect(
                self.click_ass4)  # Button event onClick

        if (len(name) == 4+counter*5):
            self.testButton.hide()
            flag_end = True
        elif (flag_end == False):
            self.booton4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.booton4.setMinimumSize(QtCore.QSize(80, 80))
            self.booton4.setMaximumSize(QtCore.QSize(80, 80))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.booton4.setFont(font)
            self.booton4.setObjectName("booton4")
            self.booton4.setText(_translate("MainWindow", name[4+counter*5]))
            self.horizontalLayout_2.addWidget(self.booton4)
            self.booton4.clicked.connect(
                self.click_ass5)  # Button event onClick

    def right_clicked(self):
        global counter
        counter = counter + 1
        if counter != 0:
            self.testButton_2.show()
        for i in reversed(range(self.horizontalLayout_2.count())):
            # removes all the widgets inside the horizontal layout
            self.horizontalLayout_2.itemAt(i).widget().setParent(None)
        self.refresh_icons()
    
    def click_ass1(self):
        text1 = self.booton.text()
        print(text1)
        find_by_name(text1)

    def click_ass2(self):
        text2 = self.booton1.text()
        print(text2)
        find_by_name(text2)

    def click_ass3(self):
        text3 = self.booton2.text()
        print(text3)
        find_by_name(text3)

    def click_ass4(self):
        text4 = self.booton3.text()
        print(text4)
        find_by_name(text4)

    def click_ass5(self):
        text5 = self.booton4.text()
        print(text5)
        find_by_name(text5)

    def selected_items(self):

        try:
            print(self.listWidget.currentItem().text())
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Select an item first")
            x = msg.exec_()  # this will show our messagebox
            print("Select an item from the list first before ....")

    def yes_button(self,i):
        if(i.text()=='&Yes'):
            global name
            name.clear()
            edit_list = []
            delete_items(self.listWidget.currentItem().text())
            self.name_input.clear()
            data = conn.execute("SELECT DISTINCT NAME FROM UserData")
            for row in data:
                name.append(row[0])
            self.listWidget.clear() #clean stoixeiwn prin to population
            self.listWidget.addItems(table_population(edit_list))

            self.addlistWidget.clear() #clean stoixeiwn prin to population


            apps_list = []
            for software in get_installed_software():
                apps_list.append(software['name'])

            apps_list.reverse()# reverse twn stoixeiwn tis listas gia na fainontai oi 'kales' efarmoges prwtes

            for app in apps_list:
                item = QListWidgetItem(app)
                item.setFlags(item.flags() |  QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.addlistWidget.addItem(item) 
            for j in reversed(range(self.horizontalLayout_2.count())):
                # removes all the widgets inside the horizontal layout
                self.horizontalLayout_2.itemAt(j).widget().setParent(None)
            global counter, flag_end
            counter = 0
            self.testButton_2.hide()
            flag_end = False
            self.refresh_icons()
            if(len(name)>5):
                    self.testButton.show()
            else:
                self.testButton.hide()
        else:
            return

    def delete_item(self):
        try:
            msg = QMessageBox()
            msg.setWindowTitle("Delete Item")
            msg.setText("Are you sure you want to delete " + self.listWidget.currentItem().text())
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.buttonClicked.connect(self.yes_button)
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Select an item to delete")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()  # this will show our messagebox

    def settings_up(self):
        global animation_dist
        edit_list = []
        x_pos = self.edit_page.x()
        y_pos = self.edit_page.y()
        # Animation parathirou me lista epilogwn
        self.anim = QPropertyAnimation(self.edit_page, b"geometry")
        self.anim.setDuration(animation_duration)
        self.anim.setStartValue(QRect(x_pos, y_pos, 1204, 967))
        self.anim.setEndValue(QRect(x_pos, y_pos-animation_dist, 1204, 967))
        self.anim.start()

        x_pos = self.settings_backframe.x()
        y_pos = self.settings_backframe.y()
        self.anim1 = QPropertyAnimation(self.settings_backframe, b"geometry")
        self.anim1.setDuration(animation_duration)
        self.anim1.setStartValue(QRect(x_pos, y_pos, 801, 561))
        self.anim1.setEndValue(QRect(x_pos, y_pos-animation_dist, 801, 561))
        self.anim1.start()

        x_pos = self.main_frame.x()
        y_pos = self.main_frame.y()
        self.anim2 = QPropertyAnimation(self.main_frame, b"geometry")
        self.anim2.setDuration(animation_duration)
        self.anim2.setStartValue(QRect(x_pos, y_pos, 771, 131))
        self.anim2.setEndValue(QRect(x_pos, y_pos, 0, 131))
        self.anim2.start()

        self.listWidget.clear() #clean stoixeiwn prin to population
        self.listWidget.addItems(table_population(edit_list))
        

        self.settingsUpButton.setEnabled(False)  #apenergopoiisi koumpiou gia apotropi epanalipsis animation
        self.settingsDownButton.setEnabled(True) #energopoisi tou koumpiou 

    def settings_down(self):
        global animation_dist
        x_pos = self.edit_page.x()
        y_pos = self.edit_page.y()
        # Animation parathirou me lista epilogwn
        self.anim = QPropertyAnimation(self.edit_page, b"geometry")
        self.anim.setDuration(animation_duration)
        self.anim.setStartValue(QRect(x_pos, y_pos, 1204, 967))
        self.anim.setEndValue(QRect(x_pos, y_pos+animation_dist, 1204, 967))
        self.anim.start()

        x_pos = self.settings_backframe.x()
        y_pos = self.settings_backframe.y()
        self.anim1 = QPropertyAnimation(self.settings_backframe, b"geometry")
        self.anim1.setDuration(animation_duration)
        self.anim1.setStartValue(QRect(x_pos, y_pos, 801, 561))
        self.anim1.setEndValue(QRect(x_pos, y_pos+animation_dist, 801, 561))
        self.anim1.start()

        x_pos = self.main_frame.x()
        y_pos = self.main_frame.y()
        self.anim2 = QPropertyAnimation(self.main_frame, b"geometry")
        self.anim2.setDuration(animation_duration)
        self.anim2.setStartValue(QRect(x_pos, y_pos, 0, 131))
        self.anim2.setEndValue(QRect(x_pos, y_pos, 771, 131))
        self.anim2.start()

        self.settingsUpButton.setEnabled(True) #energopoisi tou koumpiou 
        self.settingsDownButton.setEnabled(False) #apenergopoiisi koumpiou gia apotropi epanalipsis animation

    def add_up(self):
        global animation_dist
        x_pos = self.add_page.x()
        y_pos = self.add_page.y()
        # Animation parathirou me lista epilogwn
        self.anim = QPropertyAnimation(self.add_page, b"geometry")
        self.anim.setDuration(animation_duration)
        self.anim.setStartValue(QRect(x_pos, y_pos, 1204, 967))
        self.anim.setEndValue(QRect(x_pos, y_pos-animation_dist, 1204, 967))
        self.anim.start()

        x_pos = self.add_backframe.x()
        y_pos = self.add_backframe.y()
        self.anim1 = QPropertyAnimation(self.add_backframe, b"geometry")
        self.anim1.setDuration(animation_duration)
        self.anim1.setStartValue(QRect(x_pos, y_pos, 801, 561))
        self.anim1.setEndValue(QRect(x_pos, y_pos-animation_dist, 801, 561))
        self.anim1.start()

        x_pos = self.edit_page.x()
        y_pos = self.edit_page.y()
        # Animation parathirou me lista epilogwn
        self.anim2 = QPropertyAnimation(self.edit_page, b"geometry")
        self.anim2.setDuration(animation_duration)
        self.anim2.setStartValue(QRect(x_pos, y_pos, 1204, 967))
        self.anim2.setEndValue(QRect(x_pos, y_pos-animation_dist, 1204, 967))
        self.anim2.start()

        x_pos = self.settings_backframe.x()
        y_pos = self.settings_backframe.y()
        self.anim3 = QPropertyAnimation(self.settings_backframe, b"geometry")
        self.anim3.setDuration(animation_duration)
        self.anim3.setStartValue(QRect(x_pos, y_pos, 801, 561))
        self.anim3.setEndValue(QRect(x_pos, y_pos-animation_dist, 801, 561))
        self.anim3.start()
        
        apps_list = []

        for software in get_installed_software():
            apps_list.append(software['name'])

        apps_list.reverse()# reverse twn stoixeiwn tis listas gia na fainontai oi 'kales' efarmoges prwtes
        self.addlistWidget.clear() #clean stoixeiwn prin to population

        for app in apps_list:
            item = QListWidgetItem(app)
            item.setFlags(item.flags() |  QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.addlistWidget.addItem(item) 

        self.addButton.setEnabled(False)  #apenergopoiisi koumpiou gia apotropi epanalipsis animation
        self.addDownButton.setEnabled(True) #energopoisi tou koumpiou 

    def add_down(self):
        global animation_dist
        x_pos = self.add_page.x()
        y_pos = self.add_page.y()
        # Animation parathirou me lista epilogwn
        self.anim = QPropertyAnimation(self.add_page, b"geometry")
        self.anim.setDuration(animation_duration)
        self.anim.setStartValue(QRect(x_pos, y_pos, 1204, 967))
        self.anim.setEndValue(QRect(x_pos, y_pos+animation_dist, 1204, 967))
        self.anim.start()

        x_pos = self.add_backframe.x()
        y_pos = self.add_backframe.y()
        self.anim1 = QPropertyAnimation(self.add_backframe, b"geometry")
        self.anim1.setDuration(animation_duration)
        self.anim1.setStartValue(QRect(x_pos, y_pos, 801, 561))
        self.anim1.setEndValue(QRect(x_pos, y_pos+animation_dist, 801, 561))
        self.anim1.start()

        self.addButton.setEnabled(True)  #apenergopoiisi koumpiou gia apotropi epanalipsis animation
        self.addDownButton.setEnabled(False) #energopoisi tou koumpiou

        x_pos = self.edit_page.x()
        y_pos = self.edit_page.y()
        # Animation parathirou me lista epilogwn
        self.anim2 = QPropertyAnimation(self.edit_page, b"geometry")
        self.anim2.setDuration(animation_duration)
        self.anim2.setStartValue(QRect(x_pos, y_pos, 1204, 967))
        self.anim2.setEndValue(QRect(x_pos, y_pos+animation_dist, 1204, 967))
        self.anim2.start()

        x_pos = self.settings_backframe.x()
        y_pos = self.settings_backframe.y()
        self.anim3 = QPropertyAnimation(self.settings_backframe, b"geometry")
        self.anim3.setDuration(animation_duration)
        self.anim3.setStartValue(QRect(x_pos, y_pos, 801, 561))
        self.anim3.setEndValue(QRect(x_pos, y_pos+animation_dist, 801, 561))
        self.anim3.start()

    def confirm_insert(self):
        global name
        name.clear()
        edit_list = []
        
        for j in range(self.addlistWidget.count()):     #diaperna ti lista kai elegxei poia antikeimena einai markarismena
            item = self.addlistWidget.item(j)
            if item.checkState() == QtCore.Qt.Checked:
                add_new_items(self.name_input.toPlainText(),item.text())

        self.name_input.clear()
        data = conn.execute("SELECT DISTINCT NAME FROM UserData")
        for row in data:
            name.append(row[0])


        for i in reversed(range(self.horizontalLayout_2.count())):
            # removes all the widgets inside the horizontal layout
            self.horizontalLayout_2.itemAt(i).widget().setParent(None)
        self.refresh_icons()

        self.listWidget.clear() #clean stoixeiwn prin to population
        self.listWidget.addItems(table_population(edit_list))

        self.addlistWidget.clear() #clean stoixeiwn prin to population

        #Fortwnei tis efarmoges tou pc
        apps_list = []
        for software in get_installed_software():
            apps_list.append(software['name'])

        apps_list.reverse()# reverse twn stoixeiwn tis listas gia na fainontai oi 'kales' efarmoges prwtes

        for app in apps_list:
            item = QListWidgetItem(app)
            item.setFlags(item.flags() |  QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.addlistWidget.addItem(item)

        for j in reversed(range(self.horizontalLayout_2.count())):
                # removes all the widgets inside the horizontal layout
                self.horizontalLayout_2.itemAt(j).widget().setParent(None)
        global counter, flag_end
        #counter = 0
        flag_end = False
        self.refresh_icons()
        if(len(name)>5):
            self.testButton.show()
        else:
            self.testButton.hide()            

    def edit_up(self):
        try:
            global update_name
            update_name = self.listWidget.currentItem().text()
            self.name_input_4.setText(self.listWidget.currentItem().text())
            global animation_dist
            x_pos = self.update_page.x()
            y_pos = self.update_page.y()
            # Animation parathirou me lista epilogwn
            self.anim = QPropertyAnimation(self.update_page, b"geometry")
            self.anim.setDuration(animation_duration)
            self.anim.setStartValue(QRect(x_pos, y_pos, 1204, 967))
            self.anim.setEndValue(QRect(x_pos, y_pos-animation_dist, 1204, 967))
            self.anim.start()

            x_pos = self.update_backframe.x()
            y_pos = self.update_backframe.y()
            # Animation parathirou me lista epilogwn
            self.anim1 = QPropertyAnimation(self.update_backframe, b"geometry")
            self.anim1.setDuration(animation_duration)
            self.anim1.setStartValue(QRect(x_pos, y_pos, 801, 561))
            self.anim1.setEndValue(QRect(x_pos, y_pos-animation_dist, 801, 561))
            self.anim1.start()

            x_pos = self.edit_page.x()
            y_pos = self.edit_page.y()
            # Animation parathirou me lista epilogwn
            self.anim2 = QPropertyAnimation(self.edit_page, b"geometry")
            self.anim2.setDuration(animation_duration)
            self.anim2.setStartValue(QRect(x_pos, y_pos, 1204, 967))
            self.anim2.setEndValue(QRect(x_pos, y_pos-animation_dist, 1204, 967))
            self.anim2.start()

            x_pos = self.settings_backframe.x()
            y_pos = self.settings_backframe.y()
            self.anim3 = QPropertyAnimation(self.settings_backframe, b"geometry")
            self.anim3.setDuration(animation_duration)
            self.anim3.setStartValue(QRect(x_pos, y_pos, 801, 561))
            self.anim3.setEndValue(QRect(x_pos, y_pos-animation_dist, 801, 561))
            self.anim3.start()

            self.updatelistWidget.clear() #clean stoixeiwn prin to population

            #Fortwnei tis efarmoges tou pc
            apps_list = []
            for software in get_installed_software():
                apps_list.append(software['name'])

            apps_list.reverse()# reverse twn stoixeiwn tis listas gia na fainontai oi 'kales' efarmoges prwtes

            for app in apps_list:
                item = QListWidgetItem(app)
                item.setFlags(item.flags() |  QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.updatelistWidget.addItem(item)
            
            link_list = []
            self.updatelistWidget_2.clear() #clean stoixeiwn prin to population
            self.updatelistWidget_2.addItems(table_population_on_update(link_list,self.listWidget.currentItem().text()))
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Select an item to edit")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()  # this will show our messagebox

    def edit_down(self):
        edit_list = []
        global animation_dist
        x_pos = self.update_page.x()
        y_pos = self.update_page.y()
        # Animation parathirou me lista epilogwn
        self.anim = QPropertyAnimation(self.update_page, b"geometry")
        self.anim.setDuration(animation_duration)
        self.anim.setStartValue(QRect(x_pos, y_pos, 1204, 967))
        self.anim.setEndValue(QRect(x_pos, y_pos+animation_dist, 1204, 967))
        self.anim.start()

        x_pos = self.update_backframe.x()
        y_pos = self.update_backframe.y()
        # Animation parathirou me lista epilogwn
        self.anim1 = QPropertyAnimation(self.update_backframe, b"geometry")
        self.anim1.setDuration(animation_duration)
        self.anim1.setStartValue(QRect(x_pos, y_pos, 801, 561))
        self.anim1.setEndValue(QRect(x_pos, y_pos+animation_dist, 801, 561))
        self.anim1.start()

        x_pos = self.edit_page.x()
        y_pos = self.edit_page.y()
        # Animation parathirou me lista epilogwn
        self.anim2 = QPropertyAnimation(self.edit_page, b"geometry")
        self.anim2.setDuration(animation_duration)
        self.anim2.setStartValue(QRect(x_pos, y_pos, 1204, 967))
        self.anim2.setEndValue(QRect(x_pos, y_pos+animation_dist, 1204, 967))
        self.anim2.start()

        x_pos = self.settings_backframe.x()
        y_pos = self.settings_backframe.y()
        self.anim3 = QPropertyAnimation(self.settings_backframe, b"geometry")
        self.anim3.setDuration(animation_duration)
        self.anim3.setStartValue(QRect(x_pos, y_pos, 801, 561))
        self.anim3.setEndValue(QRect(x_pos, y_pos+animation_dist, 801, 561))
        self.anim3.start()

        self.listWidget.clear() #clean stoixeiwn prin to population
        self.listWidget.addItems(table_population(edit_list))

    def update(self):
        global update_name
        new_name = self.name_input_4.toPlainText()
        sql_update(update_name,new_name)
        global name
        data = conn.execute("SELECT DISTINCT NAME FROM UserData")
        name.clear()
        for row in data:
            name.append(row[0])
        print("Item updated")
        update_name = self.name_input_4.toPlainText()

        for j in range(self.updatelistWidget.count()):     #diaperna ti lista kai elegxei poia antikeimena einai markarismena
            item = self.updatelistWidget.item(j)
            if item.checkState() == QtCore.Qt.Checked:
                add_new_items(update_name,item.text())
        link_list = []
        self.updatelistWidget_2.clear() #clean stoixeiwn prin to population
        self.updatelistWidget_2.addItems(table_population_on_update(link_list,update_name))

        self.updatelistWidget.clear() #clean stoixeiwn prin to population

        #Fortwnei tis efarmoges tou pc
        apps_list = []
        for software in get_installed_software():
            apps_list.append(software['name'])

        apps_list.reverse()# reverse twn stoixeiwn tis listas gia na fainontai oi 'kales' efarmoges prwtes

        for app in apps_list:
            item = QListWidgetItem(app)
            item.setFlags(item.flags() |  QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.updatelistWidget.addItem(item)

    def update_yes_button(self,i):
        if(i.text()=='&Yes'):
            global name, update_name
            name.clear()
            update_delete_items(update_name,self.updatelistWidget_2.currentItem().text())

            link_list = []
            self.updatelistWidget_2.clear() #clean stoixeiwn prin to population
            self.updatelistWidget_2.addItems(table_population_on_update(link_list,update_name))
            
            for j in reversed(range(self.horizontalLayout_2.count())):
                # removes all the widgets inside the horizontal layout
                self.horizontalLayout_2.itemAt(j).widget().setParent(None)
            data = conn.execute("SELECT DISTINCT NAME FROM UserData")
            for row in data:
                name.append(row[0])
            global counter, flag_end
            counter = 0
            self.testButton_2.hide()
            flag_end = False
            self.refresh_icons()
            if(len(name)>5):
                    self.testButton.show()
            else:
                self.testButton.hide()

        else:
            return
    def update_delete(self):
        try:
            msg = QMessageBox()
            msg.setWindowTitle("Delete Item")
            msg.setText("Are you sure you want to delete " + self.listWidget.currentItem().text())
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.buttonClicked.connect(self.update_yes_button)
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Select an item to delete")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()  # this will show our messagebox

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

# Create an instance of our app
ui = MainPage(MainWindow)

# Show the window and start the app
MainWindow.show()
app.exec_()