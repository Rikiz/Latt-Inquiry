# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        self.gridWidget = QtWidgets.QWidget(Widget)
        self.gridWidget.setGeometry(QtCore.QRect(190, 230, 371, 83))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.gridWidget)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalWidget = QtWidgets.QWidget(Widget)
        self.horizontalWidget.setGeometry(QtCore.QRect(190, 130, 301, 83))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit1 = QtWidgets.QTextEdit(self.horizontalWidget)
        self.textEdit1.setObjectName("textEdit1")
        self.horizontalLayout.addWidget(self.textEdit1)
        self.progressBar = QtWidgets.QProgressBar(Widget)
        self.progressBar.setGeometry(QtCore.QRect(190, 340, 341, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridWidget_2 = QtWidgets.QWidget(Widget)
        self.gridWidget_2.setGeometry(QtCore.QRect(180, 390, 371, 83))
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.gridWidget_2)
        self.textEdit_2.setAutoFillBackground(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_2.addWidget(self.textEdit_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton.clicked.connect(Widget.onClickSubmit)
        self.pushButton_3.clicked.connect(Widget.onClickOutput)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "经纬度查询"))
        self.textEdit.setPlaceholderText(_translate("Widget", "地址"))
        self.pushButton.setText(_translate("Widget", "Go!"))
        self.textEdit1.setPlaceholderText(_translate("Widget", "api key"))
        self.textEdit_2.setPlaceholderText(_translate("Widget", "结果保存地址"))
        self.pushButton_3.setText(_translate("Widget", "Go!"))
