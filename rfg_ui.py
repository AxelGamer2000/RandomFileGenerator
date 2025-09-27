# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rfgsxpEkN.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 305)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setGeometry(QRect(0, 230, 601, 51))
        self.repeatInput = QSpinBox(self.centralwidget)
        self.repeatInput.setObjectName(u"repeatInput")
        self.repeatInput.setGeometry(QRect(20, 60, 71, 27))
        self.repeatInput.setMinimum(1)
        self.repeatInput.setMaximum(1000000)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 66, 18))
        self.generatonComboBox = QComboBox(self.centralwidget)
        self.generatonComboBox.setObjectName(u"generatonComboBox")
        self.generatonComboBox.setGeometry(QRect(120, 60, 86, 26))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 40, 121, 18))
        self.onlyExtInput = QLineEdit(self.centralwidget)
        self.onlyExtInput.setObjectName(u"onlyExtInput")
        self.onlyExtInput.setGeometry(QRect(260, 60, 81, 26))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 40, 81, 18))
        self.pickFileButton = QPushButton(self.centralwidget)
        self.pickFileButton.setObjectName(u"pickFileButton")
        self.pickFileButton.setEnabled(False)
        self.pickFileButton.setGeometry(QRect(20, 140, 94, 26))
        self.pickFileButton.setCheckable(False)
        self.pickFileButton.setChecked(False)
        self.pickFileButton.setFlat(False)
        self.fileLabel = QLabel(self.centralwidget)
        self.fileLabel.setObjectName(u"fileLabel")
        self.fileLabel.setEnabled(False)
        self.fileLabel.setGeometry(QRect(20, 170, 381, 18))
        self.contentLabel = QLabel(self.centralwidget)
        self.contentLabel.setObjectName(u"contentLabel")
        self.contentLabel.setEnabled(False)
        self.contentLabel.setGeometry(QRect(20, 120, 66, 18))
        self.fileSizeInput = QSpinBox(self.centralwidget)
        self.fileSizeInput.setObjectName(u"fileSizeInput")
        self.fileSizeInput.setEnabled(False)
        self.fileSizeInput.setGeometry(QRect(150, 140, 71, 27))
        self.fileSizeInput.setMinimum(1)
        self.fileSizeInput.setMaximum(999)
        self.fileSizeLabel = QLabel(self.centralwidget)
        self.fileSizeLabel.setObjectName(u"fileSizeLabel")
        self.fileSizeLabel.setEnabled(False)
        self.fileSizeLabel.setGeometry(QRect(150, 120, 66, 18))
        self.fileSizeTypeComboBox = QComboBox(self.centralwidget)
        self.fileSizeTypeComboBox.setObjectName(u"fileSizeTypeComboBox")
        self.fileSizeTypeComboBox.setEnabled(False)
        self.fileSizeTypeComboBox.setGeometry(QRect(220, 140, 51, 26))
        self.dictInput = QLineEdit(self.centralwidget)
        self.dictInput.setObjectName(u"dictInput")
        self.dictInput.setGeometry(QRect(300, 140, 101, 26))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(300, 120, 101, 18))
        self.fileContentCheckBox = QCheckBox(self.centralwidget)
        self.fileContentCheckBox.setObjectName(u"fileContentCheckBox")
        self.fileContentCheckBox.setGeometry(QRect(460, 60, 111, 23))
        self.fileSizeCheckBox = QCheckBox(self.centralwidget)
        self.fileSizeCheckBox.setObjectName(u"fileSizeCheckBox")
        self.fileSizeCheckBox.setGeometry(QRect(460, 80, 91, 23))
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
        self.pickFileButton.setText(QCoreApplication.translate("MainWindow", u"pick file", None))
        self.fileLabel.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.contentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.fileSizeLabel.setText(QCoreApplication.translate("MainWindow", u"File Size", None))
        self.dictInput.setText(QCoreApplication.translate("MainWindow", u"fr", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dictionnary", None))
        self.fileContentCheckBox.setText(QCoreApplication.translate("MainWindow", u"File Content", None))
        self.fileSizeCheckBox.setText(QCoreApplication.translate("MainWindow", u"File Size", None))
    # retranslateUi

