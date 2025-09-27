# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rfgXUTeHO.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 228)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setGeometry(QRect(0, 160, 601, 51))
        self.repeatInput = QSpinBox(self.centralwidget)
        self.repeatInput.setObjectName(u"repeatInput")
        self.repeatInput.setGeometry(QRect(20, 90, 71, 27))
        self.repeatInput.setMinimum(1)
        self.repeatInput.setMaximum(10000)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 70, 66, 18))
        self.generatonComboBox = QComboBox(self.centralwidget)
        self.generatonComboBox.setObjectName(u"generatonComboBox")
        self.generatonComboBox.setGeometry(QRect(120, 90, 86, 26))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 70, 121, 18))
        self.onlyExtInput = QLineEdit(self.centralwidget)
        self.onlyExtInput.setObjectName(u"onlyExtInput")
        self.onlyExtInput.setGeometry(QRect(470, 90, 113, 26))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(470, 70, 121, 18))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Generation Mode", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Only Ext", None))
    # retranslateUi

