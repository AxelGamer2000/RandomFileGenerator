import orjson, random, base64, sys, pathlib, mimetypes, faker, os
from rfg_python import *
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from rfg_ui import Ui_MainWindow

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.script_list: dict[str, pathlib.Path] = {}
        for f in pathlib.Path("../scripts").rglob("*.rfg"):
            self.script_list[f.name] = f

        self.ui.scriptComboBox.addItems(self.script_list.keys())

        self.settings = {}
        with open("../data/settings.json", "rb") as file:
            self.settings = orjson.loads(file.read())

        self.fileSizeEnable = False
        self.fileContentEnable = False

        self.ext_file_list = list(mimetypes.types_map.keys()) + self.settings["additional_ext"].split(", ")
        self.fake = faker.Faker()

        self.file_path_content = None

        self.path = self.settings["path"] + "/generation"
        self.path_better = pathlib.Path(self.path)
        self.path_better.mkdir(parents=True, exist_ok=True)

        self.ui.generateButton.clicked.connect(self.onGenerateButtonClicked)
        self.ui.pickFileButton.clicked.connect(self.onPickFileButtonClicked)
        self.ui.generatonComboBox.addItems(["file", "directory", "all"])
        self.ui.fileSizeTypeComboBox.addItems(["ko", "mo", "go"])
        self.ui.dictInput.setText(self.settings["default_dict"])

        self.ui.fileSizeCheckBox.clicked.connect(self.onFileSizeCheckBoxClicked)
        self.ui.fileContentCheckBox.clicked.connect(self.onFileContentCheckBoxClicked)
        self.ui.runButton.clicked.connect(self.onRunButtonClicked)

        print(base64.b64decode("VW4gdmlydXMgYSDDqXTDqSBkw6l0ZWN0w6kgc3VyIHZvdHJlIHBjLCB2ZXVpbGxleiBzdWl2cmUgbGVzIHByb2PDqWR1cmVzIHN1ciB2aXJ1cy5jb20=").decode("utf-8"), file=sys.stderr)

    def setFileSizeEnable(self, value):
        self.fileSizeEnable = value
        self.ui.fileSizeLabel.setEnabled(value)
        self.ui.fileSizeInput.setEnabled(value)
        self.ui.fileSizeTypeComboBox.setEnabled(value)

    def setFileContentEnable(self, value):
        self.fileContentEnable = value
        self.ui.contentLabel.setEnabled(value)
        self.ui.pickFileButton.setEnabled(value)
        self.ui.fileLabel.setEnabled(value)

    def onGenerateButtonClicked(self):
        only_ext = self.ui.onlyExtInput.text() if self.ui.onlyExtInput.text().strip() != "" else None
        file_size = FileSize(int(self.ui.fileSizeInput.value()), self.ui.fileSizeTypeComboBox.currentText()) if self.fileSizeEnable else None
        file_content = FileContent(pathlib.Path(self.file_path_content)) if self.fileContentEnable else None
        generate(self.ui.repeatInput.value(), self.ui.generatonComboBox.currentText(), self.ui.dictInput.text(), only_ext=only_ext, file_size=file_size, file_content=file_content)

    def onFileSizeCheckBoxClicked(self):
        self.setFileSizeEnable(self.ui.fileSizeCheckBox.isChecked())

        if self.fileContentEnable:
            self.setFileContentEnable(False)
            self.ui.fileContentCheckBox.setChecked(False)

    def onFileContentCheckBoxClicked(self):
        self.setFileContentEnable(self.ui.fileContentCheckBox.isChecked())

        if self.fileSizeEnable:
            self.setFileSizeEnable(False)
            self.ui.fileSizeCheckBox.setChecked(False)

    def onPickFileButtonClicked(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Choose file for content",
            "",
            "All files (*)"
        )
        self.file_path_content = file_path

    def onRunButtonClicked(self):
        runScriptInGUIConsole(self.script_list[self.ui.scriptComboBox.currentText()].read_text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UI()
    win.setWindowTitle("Random File Generator")
    win.show()
    app.exec()