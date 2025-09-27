import sys, jedi

from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager
from jedi.api.refactoring import Refactoring
from pygments import lex
from pygments.lexers import get_lexer_by_name
from pygments.token import Token
from rfg_python import *

import pathlib, json

from RandomFileGeneratorV4.lib.highlighter import PygmentsHighlighter
from rfg_editor_ui import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow, QCompleter, QAbstractItemView, QInputDialog, QMessageBox
from PySide6.QtGui import QFontMetrics, QStandardItem, QStandardItemModel
from PySide6.QtCore import Qt


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lexer = get_lexer_by_name("python")

        self.highlighter = PygmentsHighlighter(self.ui.codeEditor.document(), self.lexer)
        self.ui.codeEditor.setTabStopDistance(2*QFontMetrics(self.ui.codeEditor.font()).horizontalAdvance(" "))

        self.working_path = pathlib.Path("../scripts")
        self.files: dict[str, pathlib.Path] = {}

        print(type(self.ui.fileView))
        self.initializeFiles()

        self.ui.fileView.doubleClicked.connect(self.onDoubleClickedFileView)
        self.ui.fileView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.fileView.setSortingEnabled(True)
        self.ui.fileView.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.ui.initializeFilesAction.triggered.connect(self.initializeFiles)
        self.ui.saveFileAction.triggered.connect(self.saveSelectedFile)
        self.ui.createFileAction.triggered.connect(self.onTriggeredCreateFileAction)
        self.ui.deleteFileAction.triggered.connect(self.onTriggeredDeleteFileAction)
        self.ui.renameFileAction.triggered.connect(self.onTriggeredRenameFileAction)
        self.ui.renameVariableAction.triggered.connect(self.onTriggeredRenameVariableAction)
        self.ui.runProgramAction.triggered.connect(self.onTriggeredRunProgramAction)

    def getSelectedFile(self) -> pathlib.Path:
        model: QStandardItemModel = self.ui.fileView.model()
        index = self.ui.fileView.currentIndex()
        return self.files[model.itemFromIndex(index).text()]

    def initializeFiles(self):
        file_list = []
        self.files = {}
        for file in self.working_path.iterdir():
            if file.is_file() and file.suffix == ".rfg":
                file_list.append(file.name)
                self.files[file.name] = file

        model = QStandardItemModel()
        list(map(lambda name: model.appendRow(QStandardItem(name)), file_list))
        self.ui.fileView.setModel(model)
        self.ui.fileView.expandAll()

    def saveFile(self, path: pathlib.Path):
        path.write_text(self.ui.codeEditor.toPlainText())

    def saveSelectedFile(self):
        self.saveFile(self.getSelectedFile())

    def keyPressEvent(self, event, /):
        if event.key() == Qt.Key.Key_S and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.saveSelectedFile()

    def onDoubleClickedFileView(self):
        self.ui.codeEditor.setPlainText(self.getSelectedFile().read_text())

    def onTriggeredCreateFileAction(self):
        text, ok = QInputDialog.getText(None, "Create File", "Enter the file name: ")
        if ok:
            new_file = self.working_path / (text + ".rfg")
            new_file.touch(exist_ok=True)
            self.initializeFiles()

    def onTriggeredDeleteFileAction(self):
        result = QMessageBox.warning(None, "Delete File", "Delete the file is irreversible.", buttons=QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

        if result == QMessageBox.StandardButton.Ok:
            self.getSelectedFile().unlink(missing_ok=True)
            self.initializeFiles()

    def onTriggeredRenameFileAction(self):
        text, ok = QInputDialog.getText(None, "Create File", "Enter the new file name: ", text=self.getSelectedFile().stem)
        new_file = self.working_path / (text + ".rfg")
        if ok and not new_file.exists():
            self.getSelectedFile().rename(new_file)
            self.initializeFiles()

    def onTriggeredRenameVariableAction(self):
        script = jedi.Script(self.ui.codeEditor.toPlainText(), path=self.getSelectedFile())
        new_variable, ok = QInputDialog.getText(None, "Rename Variable", "Enter the new variable name: ")

        if ok:
            cursor = self.ui.codeEditor.textCursor()
            line, column = cursor.blockNumber() + 1, cursor.positionInBlock() + 1

            changes: Refactoring = script.rename(line, column, new_name=new_variable)
            changes.apply()
            self.ui.codeEditor.setPlainText(self.getSelectedFile().read_text())

    def onTriggeredRunProgramAction(self):
        runScriptInGUIConsole(self.ui.codeEditor.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = UI()
    win.setWindowTitle("RFG Editor")
    win.show()
    app.exec()