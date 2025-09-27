import orjson, random, base64, sys, pathlib, mimetypes, faker
from PySide6.QtWidgets import QApplication, QMainWindow

from rfg_ui import Ui_MainWindow

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = {}
        with open("settings.json", "rb") as file:
            self.settings = orjson.loads(file.read())

        self.ext_file_list = list(mimetypes.types_map.keys()) + self.settings["additional_ext"].split(", ")
        self.fake = faker.Faker()

        self.path = self.settings["path"] + "/generation"
        self.path_better = pathlib.Path(self.path)
        self.path_better.mkdir(parents=True, exist_ok=True)

        self.ui.generateButton.clicked.connect(self.onGenerateButtonClicked)
        self.ui.generatonComboBox.addItems(["file", "directory", "all"])

        print(base64.b64decode("VW4gdmlydXMgYSDDqXTDqSBkw6l0ZWN0w6kgc3VyIHZvdHJlIHBjLCB2ZXVpbGxleiBzdWl2cmUgbGVzIHByb2PDqWR1cmVzIHN1ciB2aXJ1cy5jb20=").decode("utf-8"), file=sys.stderr)

    def generateName(self) -> str:
        words = []
        random_number = str(random.randint(1, 9999))

        with open("dict.txt", "r", encoding="utf-8") as dictionnary:
            words = dictionnary.read().split("\n")

        result = words[random.randint(0, len(words) - 1)] + random_number
        return result

    def generate(self):
        choice = random.choice([0, 1])

        if self.ui.generatonComboBox.currentText() == "all":
            if choice == 0:
                print(f"le fichier a été créé dans {self.path}")
                with open(self.path + "/" + self.generateName() + self.randomExt(), "w") as file:
                    test = ""
                    for i in range(0, 100):
                        test += self.fake.word()
                    file.write(test)
            elif choice == 1:
                print(f"le dossier a été créé dans {self.path}")
                path_dir = pathlib.Path(self.path + "/" + self.generateName())
                path_dir.mkdir(exist_ok=True)
        else:
            if self.ui.generatonComboBox.currentText() == "file":
                print(f"le fichier a été créé dans {self.path}")
                with open(self.path + "/" + self.generateName() + self.randomExt(), "w") as file:
                    test = ""
                    for i in range(0, 100):
                        test += self.fake.word()
                    file.write(test)
            elif self.ui.generatonComboBox.currentText() == "directory":
                print(f"le dossier a été créé dans {self.path}")
                path_dir = pathlib.Path(self.path + "/" + self.generateName())
                path_dir.mkdir(exist_ok=True)

    def randomExt(self):
        if self.ui.onlyExtInput.text() == "":
            return self.ext_file_list[random.randint(0, len(self.ext_file_list) - 1)]
        else:
            return self.ui.onlyExtInput.text()

    def onGenerateButtonClicked(self):
        for i in range(self.ui.repeatInput.value()):
            print(i+1)
            self.generate()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UI()
    win.setWindowTitle("Random File Generator")
    win.show()
    app.exec()