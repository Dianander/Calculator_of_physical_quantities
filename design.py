# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_0_0_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp, QApplication
from PyQt5.QtWidgets import QDialog, QMessageBox
import settings

class Ui_CCalculator_0_1(object):
    def setupUi(self, CCalculator_0_1):
        CCalculator_0_1.setObjectName("CCalculator_0_1")
        CCalculator_0_1.resize(500, 520)
        CCalculator_0_1.setMinimumSize(QtCore.QSize(600, 520))
        CCalculator_0_1.setMaximumSize(QtCore.QSize(600, 520))
        CCalculator_0_1.setBaseSize(QtCore.QSize(600, 520))
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('icons/logo.png'))        
        self.Calculator_0_1 = QtWidgets.QWidget(CCalculator_0_1)
        self.Calculator_0_1.setObjectName("Calculator_0_1")
        self.method_box = QtWidgets.QComboBox(self.Calculator_0_1)
        self.method_box.setGeometry(QtCore.QRect(0, 00, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method_box.sizePolicy().hasHeightForWidth())
        self.method_box.setSizePolicy(sizePolicy)
        self.method_box.setMinimumSize(QtCore.QSize(300, 50))
        self.method_box.setMaximumSize(QtCore.QSize(300, 50))
        self.method_box.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.method_box.setFrame(True)
        self.method_box.setObjectName("method_box")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")        
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")        
        self.method_box.addItem("")
        self.method_box.addItem("")        
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")        
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.setItemIcon(1, QIcon("'icons/logo.png'"))        
        self.submethod_box = QtWidgets.QComboBox(self.Calculator_0_1)
        self.submethod_box.setGeometry(QtCore.QRect(0, 50, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submethod_box.sizePolicy().hasHeightForWidth())
        self.submethod_box.setSizePolicy(sizePolicy)
        self.submethod_box.setMinimumSize(QtCore.QSize(300, 50))
        self.submethod_box.setMaximumSize(QtCore.QSize(300, 50))
        self.submethod_box.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submethod_box.setCurrentText("")
        self.submethod_box.setFrame(True)
        self.submethod_box.setObjectName("submethod_box")
        self.submethod_box.addItem("")
        self.line = QtWidgets.QFrame(self.Calculator_0_1)
        self.line.setGeometry(QtCore.QRect(292, 0, 21, 500))
        self.line.setMinimumSize(QtCore.QSize(2, 500))
        self.line.setMaximumSize(QtCore.QSize(500, 2))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.value_label_1 = QtWidgets.QLabel(self.Calculator_0_1)
        self.value_label_1.setGeometry(QtCore.QRect(0, 160, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_label_1.sizePolicy().hasHeightForWidth())
        self.value_label_1.setSizePolicy(sizePolicy)
        self.value_label_1.setMinimumSize(QtCore.QSize(300, 50))
        self.value_label_1.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.value_label_1.setFont(font)
        self.value_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.value_label_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.value_label_1.setLineWidth(1)
        self.value_label_1.setMidLineWidth(1)
        self.value_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.value_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.value_label_1.setWordWrap(False)
        self.value_label_1.setObjectName("value_label_1")
        self.value_label_2 = QtWidgets.QLabel(self.Calculator_0_1)
        self.value_label_2.setGeometry(QtCore.QRect(0, 200, 250, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_label_2.sizePolicy().hasHeightForWidth())
        self.value_label_2.setSizePolicy(sizePolicy)
        self.value_label_2.setMinimumSize(QtCore.QSize(300, 50))
        self.value_label_2.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.value_label_2.setFont(font)
        self.value_label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.value_label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.value_label_2.setLineWidth(1)
        self.value_label_2.setMidLineWidth(1)
        self.value_label_2.setText("")
        self.value_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.value_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.value_label_2.setWordWrap(False)
        self.value_label_2.setObjectName("value_label_2")
        self.formula_label_1 = QtWidgets.QLabel(self.Calculator_0_1)
        self.formula_label_1.setGeometry(QtCore.QRect(0, 250, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formula_label_1.sizePolicy().hasHeightForWidth())
        self.formula_label_1.setSizePolicy(sizePolicy)
        self.formula_label_1.setMinimumSize(QtCore.QSize(300, 50))
        self.formula_label_1.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.formula_label_1.setFont(font)
        self.formula_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.formula_label_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.formula_label_1.setLineWidth(1)
        self.formula_label_1.setMidLineWidth(1)
        self.formula_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.formula_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.formula_label_1.setWordWrap(False)
        self.formula_label_1.setObjectName("formula_label_1")
        self.formula_label_2 = QtWidgets.QLabel(self.Calculator_0_1)
        self.formula_label_2.setGeometry(QtCore.QRect(0, 300, 250, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formula_label_2.sizePolicy().hasHeightForWidth())
        self.formula_label_2.setSizePolicy(sizePolicy)
        self.formula_label_2.setMinimumSize(QtCore.QSize(300, 50))
        self.formula_label_2.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.formula_label_2.setFont(font)
        self.formula_label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.formula_label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.formula_label_2.setLineWidth(1)
        self.formula_label_2.setMidLineWidth(1)
        self.formula_label_2.setText("")
        self.formula_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.formula_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.formula_label_2.setWordWrap(False)
        self.formula_label_2.setObjectName("formula_label_2")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.a_line = QtWidgets.QLineEdit(self.Calculator_0_1)
        self.a_line.setEnabled(False)
        self.a_line.setGeometry(QtCore.QRect(305, 30, 300, 30))
        self.a_line.setMinimumSize(QtCore.QSize(300, 30))
        self.a_line.setMaximumSize(QtCore.QSize(300, 30))
        self.a_line.setFrame(False)
        self.a_line.setObjectName("a_line")
        self.b_line = QtWidgets.QLineEdit(self.Calculator_0_1)
        self.b_line.setEnabled(False)
        self.b_line.setGeometry(QtCore.QRect(305, 90, 300, 30))
        self.b_line.setMinimumSize(QtCore.QSize(300, 30))
        self.b_line.setMaximumSize(QtCore.QSize(300, 30))
        self.b_line.setFrame(False)
        self.b_line.setObjectName("b_line")
        self.a_label = QtWidgets.QLabel(self.Calculator_0_1)
        self.a_label.setEnabled(False)
        self.a_label.setGeometry(QtCore.QRect(300, 0, 300, 30))
        self.a_label.setMinimumSize(QtCore.QSize(300, 30))
        self.a_label.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.a_label.setFont(font)
        self.a_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.a_label.setAlignment(QtCore.Qt.AlignCenter)
        self.a_label.setObjectName("a_label")
        self.b_label = QtWidgets.QLabel(self.Calculator_0_1)
        self.b_label.setEnabled(False)
        self.b_label.setGeometry(QtCore.QRect(300, 60, 300, 30))
        self.b_label.setMinimumSize(QtCore.QSize(300, 30))
        self.b_label.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.b_label.setFont(font)
        self.b_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.b_label.setAlignment(QtCore.Qt.AlignCenter)
        self.b_label.setObjectName("b_label")
        self.answer_label_1 = QtWidgets.QLabel(self.Calculator_0_1)
        self.answer_label_1.setGeometry(QtCore.QRect(300, 360, 300, 30))
        self.answer_label_1.setMinimumSize(QtCore.QSize(300, 30))
        self.answer_label_1.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.answer_label_1.setFont(font)
        self.answer_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.answer_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_label_1.setObjectName("answer_label_1")
        self.answer_label_2 = QtWidgets.QLabel(self.Calculator_0_1)
        self.answer_label_2.setGeometry(QtCore.QRect(300, 400, 300, 35))
        self.answer_label_2.setMinimumSize(QtCore.QSize(300, 35))
        self.answer_label_2.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.answer_label_2.setFont(font)
        self.answer_label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.answer_label_2.setText("")
        self.answer_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_label_2.setObjectName("answer_label_2")
        self.answer_btn = QtWidgets.QPushButton(self.Calculator_0_1)
        self.answer_btn.setGeometry(QtCore.QRect(300, 440, 300, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_btn.sizePolicy().hasHeightForWidth())
        self.answer_btn.setSizePolicy(sizePolicy)
        self.answer_btn.setMinimumSize(QtCore.QSize(300, 60))
        self.answer_btn.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer_btn.setFont(font)
        self.answer_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.answer_btn.setObjectName("answer_btn")
        self.c_label = QtWidgets.QLabel(self.Calculator_0_1)
        self.c_label.setEnabled(False)
        self.c_label.setGeometry(QtCore.QRect(300, 120, 300, 30))
        self.c_label.setMinimumSize(QtCore.QSize(300, 30))
        self.c_label.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.c_label.setFont(font)
        self.c_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_label.setAlignment(QtCore.Qt.AlignCenter)
        self.c_label.setObjectName("c_label")
        self.c_line = QtWidgets.QLineEdit(self.Calculator_0_1)
        self.c_line.setEnabled(False)
        self.c_line.setGeometry(QtCore.QRect(305, 150, 300, 30))
        self.c_line.setMinimumSize(QtCore.QSize(300, 30))
        self.c_line.setMaximumSize(QtCore.QSize(300, 30))
        self.c_line.setFrame(False)
        self.c_line.setObjectName("c_line")
        self.d_label = QtWidgets.QLabel(self.Calculator_0_1)
        self.d_label.setEnabled(False)
        self.d_label.setGeometry(QtCore.QRect(300, 180, 300, 30))
        self.d_label.setMinimumSize(QtCore.QSize(300, 30))
        self.d_label.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.d_label.setFont(font)
        self.d_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d_label.setObjectName("d_label")
        self.d_line = QtWidgets.QLineEdit(self.Calculator_0_1)
        self.d_line.setEnabled(False)
        self.d_line.setGeometry(QtCore.QRect(305, 210, 300, 30))
        self.d_line.setMinimumSize(QtCore.QSize(300, 30))
        self.d_line.setMaximumSize(QtCore.QSize(300, 30))
        self.d_line.setFrame(False)
        self.d_line.setObjectName("d_line")
        self.e_label = QtWidgets.QLabel(self.Calculator_0_1)
        self.e_label.setEnabled(False)
        self.e_label.setGeometry(QtCore.QRect(300, 240, 300, 30))
        self.e_label.setMinimumSize(QtCore.QSize(300, 30))
        self.e_label.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.e_label.setFont(font)
        self.e_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.e_label.setObjectName("e_label")
        self.e_line = QtWidgets.QLineEdit(self.Calculator_0_1)
        self.e_line.setEnabled(False)
        self.e_line.setGeometry(QtCore.QRect(305, 280, 300, 30))
        self.e_line.setMinimumSize(QtCore.QSize(300, 30))
        self.e_line.setMaximumSize(QtCore.QSize(300, 30))
        self.e_line.setFrame(False)
        self.e_line.setObjectName("e_line")       
        
        self.method_box.raise_()
        self.submethod_box.raise_()
        self.value_label_1.raise_()
        self.value_label_2.raise_()
        self.formula_label_1.raise_()
        self.formula_label_2.raise_()
        self.answer_label_1.raise_()
        self.answer_label_2.raise_()
        self.answer_btn.raise_()
        self.a_label.raise_()
        self.b_label.raise_()
        self.c_label.raise_()
        self.d_label.raise_()
        self.e_label.raise_()
        self.line.raise_()
        self.a_line.raise_()
        self.b_line.raise_()        
        self.c_line.raise_()
        self.d_line.raise_()
        self.e_line.raise_()
        
        
        Dark_action = QAction(QIcon('logo.png'), '&???????????? ????????', self)
        Dark_action.setStatusTip('???????????????????? ???????????? ????????')
        Dark_action.triggered.connect(self.dark_theme)
        Dark_action.setIcon(QIcon('icons/dark_theme_icon.png'))
        
        
        Light_action = QAction(QIcon('icons/light_theme_icon.png'), '&?????????????? ????????', self)
        Light_action.setStatusTip('???????????????????? ?????????????? ????????')
        Light_action.triggered.connect(self.light_theme)


        About_project = QAction(QIcon('icons/answer_icon.png'), '&dialogus', self)
        About_project.setStatusTip('???????????????????? ???????????? ????????')
        About_project.triggered.connect(self.about_project_func)
        
        menubar = self.menuBar()
        settings_Menu = menubar.addMenu('&??????????????????')
        
        menubar.addAction(About_project)
        
        settings_Menu.setIcon(QIcon('icons/settings_gear.png'))
         
        self.Theme = settings_Menu.addMenu('&????????') 

        self.Theme.addAction(Dark_action)
        self.Theme.addAction(Light_action)

        
        open("settings.py").read()        
        
        if settings.theme == 'light':
            self.light_theme()                
        if settings.theme == 'dark':
            self.dark_theme()  
       
        CCalculator_0_1.setCentralWidget(self.Calculator_0_1)
        
        self.retranslateUi(CCalculator_0_1)
        QtCore.QMetaObject.connectSlotsByName(CCalculator_0_1)                

    def retranslateUi(self, CCalculator_0_1):
        _translate = QtCore.QCoreApplication.translate
        CCalculator_0_1.setWindowTitle(_translate("CCalculator_0_1", "Calculator 0.1"))
        self.method_box.setItemText(0, _translate("CCalculator_0_1", " ???????????????? ????????????????"))
        self.method_box.setItemText(1, _translate("CCalculator_0_1", ""))
        self.method_box.setItemText(2, _translate("CCalculator_0_1", " ????????????????"))
        self.method_box.setItemText(3, _translate("CCalculator_0_1", " ????????"))
        self.method_box.setItemText(4, _translate("CCalculator_0_1", " ??????????"))
        self.method_box.setItemText(5, _translate("CCalculator_0_1", " ??????????????????"))
        self.method_box.setItemText(6, _translate("CCalculator_0_1", " ??????????"))
        self.method_box.setItemText(7, _translate("CCalculator_0_1", " ??????????"))
        self.method_box.setItemText(8, _translate("CCalculator_0_1", " ????????"))
        self.method_box.setItemText(9, _translate("CCalculator_0_1", " ??????????????"))
        self.method_box.setItemText(10, _translate("CCalculator_0_1", " ??????????"))
        self.method_box.setItemText(11, _translate("CCalculator_0_1", " ????????????????"))
        self.method_box.setItemText(12, _translate("CCalculator_0_1", " ????????????"))
        self.method_box.setItemText(13, _translate("CCalculator_0_1", " ????????????????"))
        self.method_box.setItemText(14, _translate("CCalculator_0_1", " ???????????? ????????"))
        self.method_box.setItemText(15, _translate("CCalculator_0_1", " ??????"))
        self.method_box.setItemText(16, _translate("CCalculator_0_1", " ??????????????"))
        self.method_box.setItemText(17, _translate("CCalculator_0_1", " ??????????????????????"))
        self.method_box.setItemText(18, _translate("CCalculator_0_1", " ???????????????????? ??????????????"))
        self.method_box.setItemText(19, _translate("CCalculator_0_1", " ????????????????\n ????????????????????????"))
        self.method_box.setItemText(20, _translate("CCalculator_0_1", " ???????????????? ??????????????\n ????????????????"))
        self.method_box.setItemText(21, _translate("CCalculator_0_1", " ???????????????? ??????????????\n ??????????????????"))
        self.method_box.setItemText(22, _translate("CCalculator_0_1", " ?????????????????? ??????????????"))
        self.method_box.setItemText(23, _translate("CCalculator_0_1", " ???????????????? ??????????????\n ??????????????????????????????"))
        self.method_box.setItemText(24, _translate("CCalculator_0_1", " ?????????????????????????? ??????????"))
        self.method_box.setItemText(25, _translate("CCalculator_0_1", " ???????? ????????"))
        self.method_box.setItemText(26, _translate("CCalculator_0_1", " ????????????????????"))
        self.method_box.setItemText(27, _translate("CCalculator_0_1", " ??????????????????????????"))
        self.method_box.setItemText(28, _translate("CCalculator_0_1", " ????????????????\n ??????????????????????????"))
        self.method_box.setItemText(29, _translate("CCalculator_0_1", " ???????????????? ????. ????????"))
        self.method_box.setItemText(30, _translate("CCalculator_0_1", " ????????????????????????????"))
        self.method_box.setItemText(31, _translate("CCalculator_0_1", " ?????????????? ????. ????????"))
        self.method_box.setItemText(32, _translate("CCalculator_0_1", " ????????????????????\n ??????????????????????"))
        self.method_box.setItemText(33, _translate("CCalculator_0_1", " ???????? ????????????????????\n ??????????"))
        
        self.answer_btn.setText(_translate("CCalculator_0_1", "??????????????????"))
        self.value_label_1.setText(_translate("CCalculator_0_1", "??????. ????????????????:"))
        self.formula_label_1.setText(_translate("CCalculator_0_1", "??????????????:"))
        self.a_line.setText(_translate("CCalculator_0_1", ""))
        self.b_line.setText(_translate("CCalculator_0_1", ""))
        self.a_label.setText(_translate("CCalculator_0_1", ""))
        self.b_label.setText(_translate("CCalculator_0_1", ""))
        self.answer_label_1.setText(_translate("CCalculator_0_1", "??????????:"))
        self.c_label.setText(_translate("CCalculator_0_1", ""))
        self.c_line.setText(_translate("CCalculator_0_1", ""))
        self.d_label.setText(_translate("CCalculator_0_1", ""))
        self.d_line.setText(_translate("CCalculator_0_1", ""))
        self.e_label.setText(_translate("CCalculator_0_1", ""))
        self.e_line.setText(_translate("CCalculator_0_1", ""))
        
        
        self.answer_btn.setShortcut("Return")
        
        
        
    def dark_theme(self):     
        self.setStyleSheet("color: rgb(180, 180, 180);" 
                           "background-color: rgb(0, 0, 0);"
                           "selection-background-color: rgb(30, 30, 30);"
                           "border-color: rgb(0, 0, 0);"
                           "border-bottom-color: rgb(30, 30, 30);"
                           "alternate-background-color: rgb(31, 31, 31);")
        global theme_s
        theme_s = 'dark'
        settings = open("settings.py",'w')
        settings.write("theme = 'dark'")
        settings.close()
        
    def light_theme(self):
        self.setStyleSheet("color: rgb(15, 15, 15);"
                           "background-color: rgb(235, 235, 235);"
                           "selection-background-color: rgb(225, 225, 225);"
                           "selection-color: rgb(25, 25, 25);"
                           "border-color: rgb(200, 200, 200);"
                           "alternate-background-color: rgb(190, 190, 190);")
        global theme_s
        theme_s = 'light'
        settings = open("settings.py",'w')
        settings.write("theme = 'light'")
        settings.close()
        
    def about_project_func(self):
        about_project = QMessageBox()
        about_project.setWindowIcon(QIcon('icons/answer_icon.png'))
        about_project.setWindowTitle('?? ??????????????')
        about_project.setText('?????????????? ????????????: 1.0 \n'
                              '--------- \n'
                              '????????????????????????:\n'
                              '????????????: ???????????????? ???????????? \n'
                              '??????: ???????????????? ???????????? \n'
                              '????????????????????: ???????????????? ???????????? \n'
                              '???????????????????????? ???? ?????????????????? ????????????????????: ???????????????? ???????????? \n'
                              '--------- \n'
                              '???????????? ??????????????????????????: \n'
                              '?????????? ???????????? ???? ???????????? ?? ???????????????????? ?? ??????????????, \n'
                              '????????, ?????? ?????????????? ???????? \n')
        if theme_s == 'light':
            about_project.setStyleSheet("color: rgb(15, 15, 15);"
                           "background-color: rgb(235, 235, 235);"
                           "selection-background-color: rgb(225, 225, 225);"
                           "selection-color: rgb(25, 25, 25);"
                           "border-color: rgb(200, 200, 200);"
                           "alternate-background-color: rgb(190, 190, 190);")   
            
        if theme_s == 'dark':
            about_project.setStyleSheet("color: rgb(180, 180, 180);" 
                           "background-color: rgb(0, 0, 0);"
                           "selection-background-color: rgb(30, 30, 30);"
                           "border-color: rgb(0, 0, 0);"
                           "border-bottom-color: rgb(30, 30, 30);"
                           "alternate-background-color: rgb(31, 31, 31);") 
        about_project.exec()