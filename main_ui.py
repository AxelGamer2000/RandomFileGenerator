import struct

import orjson, random, base64, sys, pathlib, mimetypes, faker, os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from rfg_ui import Ui_MainWindow

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = {}
        with open("settings.json", "rb") as file:
            self.settings = orjson.loads(file.read())

        self.fileSizeEnable = False
        self.fileContentEnable = False

        self.ext_file_list = list(mimetypes.types_map.keys()) + self.settings["additional_ext"].split(", ")
        self.fake = faker.Faker()

        self.content = ""

        self.path = self.settings["path"] + "/generation"
        self.path_better = pathlib.Path(self.path)
        self.path_better.mkdir(parents=True, exist_ok=True)

        self.ui.generateButton.clicked.connect(self.onGenerateButtonClicked)
        self.ui.pickFileButton.clicked.connect(self.onPickFileButtonClicked)
        self.ui.generatonComboBox.addItems(["file", "directory", "all"])
        self.ui.fileSizeTypeComboBox.addItems(["ko", "mo", "go"])

        self.ui.fileSizeCheckBox.clicked.connect(self.onFileSizeCheckBoxClicked)
        self.ui.fileContentCheckBox.clicked.connect(self.onFileContentCheckBoxClicked)

        print(base64.b64decode("VW4gdmlydXMgYSDDqXTDqSBkw6l0ZWN0w6kgc3VyIHZvdHJlIHBjLCB2ZXVpbGxleiBzdWl2cmUgbGVzIHByb2PDqWR1cmVzIHN1ciB2aXJ1cy5jb20=").decode("utf-8"), file=sys.stderr)

    def generateName(self) -> str:
        words = []
        random_number = str(random.randint(1, 9999))

        with open(pathlib.Path("dicts") / (self.ui.dictInput.text() + ".txt"), "r", encoding="utf-8") as dictionnary:
            words = dictionnary.read().split("\n")

        words += str.split(self.settings["additional_words"], ", ")

        result = words[random.randint(0, len(words) - 1)] + random_number
        return result

    def generate(self):
        choice = random.choice([0, 1])

        if self.ui.generatonComboBox.currentText() == "all":
            if choice == 0:
                print(f"le fichier a été créé dans {self.path}")
                self.createFileRandomly()
            elif choice == 1:
                print(f"le dossier a été créé dans {self.path}")
                path_dir = pathlib.Path(self.path + "/" + self.generateName())
                path_dir.mkdir(exist_ok=True)
        else:
            if self.ui.generatonComboBox.currentText() == "file":
                print(f"le fichier a été créé dans {self.path}")
                self.createFileRandomly()
            elif self.ui.generatonComboBox.currentText() == "directory":
                print(f"le dossier a été créé dans {self.path}")
                path_dir = pathlib.Path(self.path + "/" + self.generateName())
                path_dir.mkdir(exist_ok=True)

    def randomExt(self):
        if self.ui.onlyExtInput.text() == "":
            return self.ext_file_list[random.randint(0, len(self.ext_file_list) - 1)]
        else:
            return self.ui.onlyExtInput.text()

    def createFileRandomly(self):
        if self.fileSizeEnable:
            convert_dict = {"ko": 1024, "mo": 1024**2, "go": 1024**3}
            with open(self.path + "/" + self.generateName() + self.randomExt(), "wb") as file:
                file.write(os.urandom(convert_dict[self.ui.fileSizeTypeComboBox.currentText()] * int(self.ui.fileSizeInput.text())))

        else:
            with open(self.path + "/" + self.generateName() + self.randomExt(), "w") as file:
                if self.fileContentEnable:
                    file.write(self.content)
                else:
                    test = ""
                    for i in range(0, 100):
                        test += self.fake.word()
                    file.write(test)

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
        for i in range(self.ui.repeatInput.value()):
            print(i+1)
            self.generate()

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
        with open(file_path, "r") as file:
            self.content = file.read()
            self.ui.fileLabel.setText(pathlib.Path(file.name).name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UI()
    win.setWindowTitle("Random File Generator")
    win.show()
    app.exec()