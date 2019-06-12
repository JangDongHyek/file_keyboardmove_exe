# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movefile.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
import sys
import os
import shutil
from PIL import Image
start = False
from tkinter import *
from tkinter import messagebox



class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1700, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, -10, 801, 1051))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(910, 20, 190, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1320, 20, 231, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(910, 160, 70, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1110, 160, 70, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1300, 160, 70, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1490, 160, 70, 12))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(910, 270, 70, 12))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1110, 270, 70, 12))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1300, 270, 70, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1490, 270, 70, 12))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(910, 380, 70, 12))
        self.label_12.setObjectName("label_12")

        self.base = QtWidgets.QLineEdit(self.centralwidget)
        self.base.setGeometry(QtCore.QRect(910, 60, 360, 30))
        self.base.setObjectName("lineEdit")
        self.mov = QtWidgets.QLineEdit(self.centralwidget)
        self.mov.setGeometry(QtCore.QRect(1320, 60, 360, 30))
        self.mov.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(910, 190, 127, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(1110, 190, 127, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(1300, 190, 127, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(1490, 190, 127, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(910, 300, 127, 30))
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(1110, 300, 127, 30))
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(1300, 300, 127, 30))
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(1490, 300, 127, 30))
        self.lineEdit_10.setObjectName("lineEdit_10")

        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(910, 410, 127, 30))
        self.lineEdit_11.setObjectName("lineEdit_11")


        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(1110, 410, 127, 30))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1110, 380, 70, 12))
        self.label_13.setObjectName("label_13")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(1300, 410, 127, 30))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1300, 380, 70, 12))
        self.label_14.setObjectName("label_14")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(1490, 410, 127, 30))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1490, 380, 70, 12))
        self.label_15.setObjectName("label_15")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(910, 530, 127, 30))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(910, 500, 70, 12))
        self.label_16.setObjectName("label_16")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(1110, 530, 127, 30))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1110, 500, 70, 12))
        self.label_17.setObjectName("label_17")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(1300, 530, 127, 30))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1300, 500, 70, 12))
        self.label_18.setObjectName("label_18")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(1490, 530, 127, 30))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1490, 500, 70, 12))
        self.label_19.setObjectName("label_19")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setGeometry(QtCore.QRect(910, 650, 127, 30))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(910, 620, 70, 12))
        self.label_20.setObjectName("label_20")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setGeometry(QtCore.QRect(1110, 650, 127, 30))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(1110, 620, 70, 12))
        self.label_21.setObjectName("label_21")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_21.setGeometry(QtCore.QRect(1300, 650, 127, 30))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(1300, 620, 70, 12))
        self.label_22.setObjectName("label_22")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_22.setGeometry(QtCore.QRect(1490, 650, 127, 30))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(1490, 620, 70, 12))
        self.label_23.setObjectName("label_23")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_23.setGeometry(QtCore.QRect(910, 760, 127, 30))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(910, 730, 70, 12))
        self.label_24.setObjectName("label_24")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_24.setGeometry(QtCore.QRect(1110, 760, 127, 30))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(1110, 730, 70, 12))
        self.label_25.setObjectName("label_25")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_25.setGeometry(QtCore.QRect(1300, 760, 127, 30))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(1300, 730, 70, 12))
        self.label_26.setObjectName("label_26")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_26.setGeometry(QtCore.QRect(1490, 760, 127, 30))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(1490, 730, 70, 12))
        self.label_27.setObjectName("label_27")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_27.setGeometry(QtCore.QRect(910, 870, 127, 30))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(910, 840, 70, 12))
        self.label_28.setObjectName("label_28")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_28.setGeometry(QtCore.QRect(1110, 870, 127, 30))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(1110, 840, 70, 12))
        self.label_29.setObjectName("label_29")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_29.setGeometry(QtCore.QRect(1300, 870, 127, 30))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(1300, 840, 70, 12))
        self.label_30.setObjectName("label_30")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_30.setGeometry(QtCore.QRect(1490, 870, 127, 30))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(1490, 840, 70, 12))
        self.label_31.setObjectName("label_31")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(910, 940, 331, 61))
        self.pushButton.clicked.connect(self.show_img)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1300, 940, 331, 61))
        self.pushButton_2.clicked.connect(self.description_img)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_img(self):
        num = 0
        dirn = 3
        folder_path = self.base.text()
        mov_path = self.mov.text()
        path = os.listdir(folder_path)

        for filename in path:
            fullpath = os.path.join(folder_path, filename)

            if (os.path.isdir(fullpath)):
                # print("{} : {}".format(dirn,filename))
                if self.lineEdit_3.text() == "":
                    self.lineEdit_3.setText(filename)
                    self.lineEdit_18.setText(filename)
                    continue
                if self.lineEdit_4.text() == "":
                    self.lineEdit_4.setText(filename)
                    self.lineEdit_19.setText(filename)
                    continue
                if self.lineEdit_5.text() == "":
                    self.lineEdit_5.setText(filename)
                    self.lineEdit_20.setText(filename)
                    continue
                if self.lineEdit_6.text() == "":
                    self.lineEdit_6.setText(filename)
                    self.lineEdit_21.setText(filename)
                    continue
                if self.lineEdit_7.text() == "":
                    self.lineEdit_7.setText(filename)
                    self.lineEdit_22.setText(filename)
                    continue
                if self.lineEdit_8.text() == "":
                    self.lineEdit_8.setText(filename)
                    self.lineEdit_23.setText(filename)
                    continue
                if self.lineEdit_9.text() == "":
                    self.lineEdit_9.setText(filename)
                    self.lineEdit_24.setText(filename)
                    continue
                if self.lineEdit_10.text() == "":
                    self.lineEdit_10.setText(filename)
                    self.lineEdit_25.setText(filename)
                    continue
                if self.lineEdit_11.text() == "":
                    self.lineEdit_11.setText(filename)
                    self.lineEdit_26.setText(filename)
                    continue
                if self.lineEdit_12.text() == "":
                    self.lineEdit_12.setText(filename)
                    self.lineEdit_27.setText(filename)
                    continue
                if self.lineEdit_13.text() == "":
                    self.lineEdit_13.setText(filename)
                    continue
                if self.lineEdit_14.text() == "":
                    self.lineEdit_14.setText(filename)
                    continue
                if self.lineEdit_15.text() == "":
                    self.lineEdit_15.setText(filename)
                    continue
                if self.lineEdit_16.text() == "":
                    self.lineEdit_16.setText(filename)
                    continue
                if self.lineEdit_17.text() == "":
                    self.lineEdit_17.setText(filename)
                    continue
                if self.lineEdit_18.text() == "":
                    self.lineEdit_18.setText(filename)
                    continue


                dirn += 1

        for filename in path:
            fullpath = os.path.join(folder_path, filename)

            if (os.path.isfile(fullpath)):
                if num == 0:
                    first = os.path.join(folder_path, filename)
                    first_name = filename
                    num += 1
                    continue

        print(first)
        # im = Image.open(first)
        # im.show()

        pixmap = QtGui.QPixmap(first)
        self.label.setPixmap(pixmap)
        self.label.show()

    def description_img(self):
        num = 0
        folder_path = self.base.text()
        mov_path = self.mov.text()
        path = os.listdir(folder_path)
        first = ""
        for filename in path:
            fullpath = os.path.join(folder_path, filename)

            if (os.path.isfile(fullpath)):
                if num == 0:
                    first = os.path.join(folder_path, filename)
                    first_name = filename
                    num += 1
                    continue

        im = Image.open(first)
        im.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "폴더위치"))
        self.label_3.setText(_translate("MainWindow", "이동할폴더"))
        self.label_4.setText(_translate("MainWindow", "주소를"))
        self.label_5.setText(_translate("MainWindow", "설정해주시고"))
        self.label_6.setText(_translate("MainWindow", "이미지 보기"))
        self.label_7.setText(_translate("MainWindow", "클릭하신다음"))
        self.label_8.setText(_translate("MainWindow", "F5 버튼을"))
        self.label_9.setText(_translate("MainWindow", "누르시면"))
        self.label_10.setText(_translate("MainWindow", "단축키가"))
        self.label_11.setText(_translate("MainWindow", "나옵니다"))
        self.label_12.setText(_translate("MainWindow", "일시정지 를"))
        self.label_13.setText(_translate("MainWindow", "원하시면"))
        self.label_14.setText(_translate("MainWindow", "F6 을"))
        self.label_15.setText(_translate("MainWindow", "누르시면"))
        self.label_16.setText(_translate("MainWindow", "일시정지가"))
        self.label_17.setText(_translate("MainWindow", "됩니다"))
        self.label_18.setText(_translate("MainWindow", ""))
        self.label_19.setText(_translate("MainWindow", ""))
        self.label_20.setText(_translate("MainWindow", ""))
        self.label_21.setText(_translate("MainWindow", ""))
        self.label_22.setText(_translate("MainWindow", ""))
        self.label_23.setText(_translate("MainWindow", ""))
        self.label_24.setText(_translate("MainWindow", ""))
        self.label_25.setText(_translate("MainWindow", ""))
        self.label_26.setText(_translate("MainWindow", ""))
        self.label_27.setText(_translate("MainWindow", ""))
        self.label_28.setText(_translate("MainWindow", ""))
        self.label_29.setText(_translate("MainWindow", ""))
        self.label_30.setText(_translate("MainWindow", ""))
        self.label_31.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "이미지 보기"))
        self.pushButton_2.setText(_translate("MainWindow", "이미지 상세보기"))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

    def openfolder(self, name):
        num = 0
        folder_path = self.base.text()
        mov_path = self.mov.text()
        path = os.listdir(folder_path)
        first = ""
        for filename in path:
            fullpath = os.path.join(folder_path, filename)

            if (os.path.isfile(fullpath)):
                if num == 0:
                    first = os.path.join(folder_path, filename)
                    first_name = filename
                    num += 1
                    continue
                try:
                    if num == 1:
                        second = os.path.join(folder_path, filename)
                        second_name = filename
                        num += 1
                        break
                except:
                    messagebox.showinfo("Alert","사진이더이상없습니다")
                    sys.exit()
                    break

        shutil.move(first, mov_path.format(name))
        print("{} => {}".format(first_name, name))
        try:
            print("NEXT : {}".format(second_name))

            pixmap = QtGui.QPixmap(second)
        except:
            messagebox.showinfo("Alert", "사진이 더이상 없으므로 프로그램을 종료합니다")
            sys.exit()

        try:
            self.label.setPixmap(pixmap)
            self.label.show()
        except:
            messagebox.showinfo("Alert", "사진이더이상없습니다")
            sys.exit()


    def keyPressEvent(self, e):
        global start
        if e.key() == Qt.Key_F5:
            start = True

            self.label_4.setText("Q")
            self.label_5.setText("W")
            self.label_6.setText("E")
            self.label_7.setText("R")
            self.label_8.setText("T")
            self.label_9.setText("A")
            self.label_10.setText("S")
            self.label_11.setText("D")
            self.label_12.setText("F")
            self.label_13.setText("G")
            self.label_14.setText("Z")
            self.label_15.setText("X")
            self.label_16.setText("C")
            self.label_17.setText("V")
            self.label_18.setText("B")
            self.label_19.setText("0")
            self.label_20.setText("1")
            self.label_21.setText("2")
            self.label_22.setText("3")
            self.label_23.setText("4")
            self.label_24.setText("5")
            self.label_25.setText("6")
            self.label_26.setText("7")
            self.label_27.setText("8")
            self.label_28.setText("9")
            self.label_29.setText("J")
            self.label_30.setText("K")
            self.label_31.setText("L")

        if e.key() == Qt.Key_F6:
            start = False
            self.label_4.setText("재시작을")
            self.label_5.setText("원하시면")
            self.label_6.setText("F5 를")
            self.label_7.setText("눌러주세요")
            self.label_8.setText("")
            self.label_9.setText("")
            self.label_10.setText("")
            self.label_11.setText("")
            self.label_12.setText("")
            self.label_13.setText("")
            self.label_14.setText("")
            self.label_15.setText("")
            self.label_16.setText("")
            self.label_17.setText("")
            self.label_18.setText("")
            self.label_19.setText("")
            self.label_20.setText("")
            self.label_21.setText("")
            self.label_22.setText("")
            self.label_23.setText("")
            self.label_24.setText("")
            self.label_25.setText("")
            self.label_26.setText("")
            self.label_27.setText("")
            self.label_28.setText("")
            self.label_29.setText("")
            self.label_30.setText("")
            self.label_31.setText("")

        if start and e.key() == Qt.Key_Q:
            name = self.lineEdit_3.text()
            self.openfolder(name)


        if start and e.key() == Qt.Key_W:
            name = self.lineEdit_4.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_E:
            name = self.lineEdit_5.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_R:
            name = self.lineEdit_6.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_T:
            name = self.lineEdit_7.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_A:
            name = self.lineEdit_8.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_S:
            name = self.lineEdit_9.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_D:
            name = self.lineEdit_10.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_F:
            name = self.lineEdit_11.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_G:
            name = self.lineEdit_12.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_Z:
            name = self.lineEdit_13.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_X:
            name = self.lineEdit_14.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_C:
            name = self.lineEdit_15.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_V:
            name = self.lineEdit_16.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_B:
            name = self.lineEdit_17.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_0:
            name = self.lineEdit_18.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_1:
            name = self.lineEdit_19.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_2:
            name = self.lineEdit_20.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_3:
            name = self.lineEdit_21.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_4:
            name = self.lineEdit_22.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_5:
            name = self.lineEdit_23.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_6:
            name = self.lineEdit_24.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_7:
            name = self.lineEdit_25.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_8:
            name = self.lineEdit_26.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_9:
            name = self.lineEdit_27.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_J:
            name = self.lineEdit_28.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_K:
            name = self.lineEdit_29.text()
            self.openfolder(name)

        if start and e.key() == Qt.Key_L:
            name = self.lineEdit_30.text()
            self.openfolder(name)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


