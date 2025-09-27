import sys, pathlib, orjson, json
from typing import Any

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RFG Settings")
        self.layout = QVBoxLayout()

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.settings: dict[str, Any] = orjson.loads(pathlib.Path("settings.json").read_text(encoding="utf-8"))
        self.inputs: dict[str, QLineEdit] = {}
        self.saveButton = QPushButton("save settings")

        self.createJsonParams()
        self.layout.addWidget(self.saveButton)
        self.saveButton.clicked.connect(self.onSaveButtonClicked)

    def createJsonParams(self):
        for key, value in self.settings.items():
            lineEdit = QLineEdit()
            lineEdit.setText(value)
            lineEdit.setFixedWidth(500)
            label = QLabel(text=key)
            label.setFixedWidth(500)
            self.layout.addWidget(label)
            self.layout.addWidget(lineEdit)
            self.inputs[key] = lineEdit

    def saveSettings(self):
        file_settings = {}
        for key, value in self.inputs.items():
            file_settings[key] = value.text()

        pathlib.Path("settings.json").write_text(json.dumps(file_settings, indent=4, ensure_ascii=False), encoding="utf-8")

    def onSaveButtonClicked(self):
        self.saveSettings()
        self.close()




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()