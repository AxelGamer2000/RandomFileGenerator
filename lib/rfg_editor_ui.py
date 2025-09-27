# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rfg_editoreIpdSJ.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QSizePolicy, QStatusBar,
    QTreeView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.createFileAction = QAction(MainWindow)
        self.createFileAction.setObjectName(u"createFileAction")
        self.deleteFileAction = QAction(MainWindow)
        self.deleteFileAction.setObjectName(u"deleteFileAction")
        self.renameFileAction = QAction(MainWindow)
        self.renameFileAction.setObjectName(u"renameFileAction")
        self.renameVariableAction = QAction(MainWindow)
        self.renameVariableAction.setObjectName(u"renameVariableAction")
        self.runProgramAction = QAction(MainWindow)
        self.runProgramAction.setObjectName(u"runProgramAction")
        self.saveFileAction = QAction(MainWindow)
        self.saveFileAction.setObjectName(u"saveFileAction")
        self.initializeFilesAction = QAction(MainWindow)
        self.initializeFilesAction.setObjectName(u"initializeFilesAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.fileView = QTreeView(self.centralwidget)
        self.fileView.setObjectName(u"fileView")
        self.fileView.setGeometry(QRect(0, 0, 171, 571))
        self.fileView.setAnimated(True)
        self.codeEditor = QPlainTextEdit(self.centralwidget)
        self.codeEditor.setObjectName(u"codeEditor")
        self.codeEditor.setGeometry(QRect(170, 0, 631, 571))
        font = QFont()
        font.setFamilies([u"Ubuntu Mono"])
        self.codeEditor.setFont(font)
        self.codeEditor.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.codeEditor.setPlainText(u"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menuFile.addAction(self.createFileAction)
        self.menuFile.addAction(self.deleteFileAction)
        self.menuFile.addAction(self.saveFileAction)
        self.menuFile.addAction(self.initializeFilesAction)
        self.menuEdit.addAction(self.renameFileAction)
        self.menuEdit.addAction(self.renameVariableAction)
        self.menuRun.addAction(self.runProgramAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.createFileAction.setText(QCoreApplication.translate("MainWindow", u"Create File", None))
        self.deleteFileAction.setText(QCoreApplication.translate("MainWindow", u"Delete File", None))
        self.renameFileAction.setText(QCoreApplication.translate("MainWindow", u"Rename File", None))
        self.renameVariableAction.setText(QCoreApplication.translate("MainWindow", u"Rename Variable", None))
        self.runProgramAction.setText(QCoreApplication.translate("MainWindow", u"Run Program", None))
        self.saveFileAction.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.initializeFilesAction.setText(QCoreApplication.translate("MainWindow", u"Initialize Files", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", u"Run", None))
    # retranslateUi

