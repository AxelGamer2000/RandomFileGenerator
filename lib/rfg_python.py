import json, pathlib, random, os, mimetypes, faker

from qtconsole.inprocess import QtInProcessKernelManager
from qtconsole.rich_jupyter_widget import RichJupyterWidget

fake = faker.Faker()
settings = json.loads(pathlib.Path("../data/settings.json").read_text(encoding="utf-8"))
path = settings["path"] + "/generation"
path_better = pathlib.Path(path)
ext_file_list = list(mimetypes.types_map.keys()) + settings["additional_ext"].split(", ")
script_path = pathlib.Path("../scripts")

class FileSize:
    def __init__(self, number, fileSizeType):
        self.number = number
        self.fileSizeType = fileSizeType

    def getSize(self):
        convert_dict = {"ko": 1024, "mo": 1024 ** 2, "go": 1024 ** 3}
        return self.number*convert_dict[self.fileSizeType]

class FileContent:
    def __init__(self, filePath):
        self.path = pathlib.Path(filePath)

def generateName(dicti) -> str:
    words = []
    random_number = str(random.randint(1, 9999))

    with open(pathlib.Path("../dicts") / (dicti + ".txt"), "r", encoding="utf-8") as dictionary:
        words = dictionary.read().split("\n")

    words += str.split(settings["additional_words"], ", ")

    result = words[random.randint(0, len(words) - 1)] + random_number
    return result

def generate(repeat, file_mode, dicti, only_ext = None, file_size: FileSize = None, file_content: FileContent = None):
    choice = random.choice([0, 1])

    for i in range(repeat):
        if file_mode == "all":
            if choice == 0:
                print(f"le fichier a été créé dans {path}")
                createFileRandomly(dicti, file_size=file_size, file_content=file_content, only_ext=only_ext)
            elif choice == 1:
                print(f"le dossier a été créé dans {path}")
                path_dir = pathlib.Path(path + "/" + generateName(dicti))
                path_dir.mkdir(exist_ok=True)
        else:
            if file_mode == "file":
                print(f"le fichier a été créé dans {path}")
                createFileRandomly(dicti, file_size=file_size, file_content=file_content, only_ext=only_ext)
            elif file_mode == "directory" or file_mode == "dir":
                print(f"le dossier a été créé dans {path}")
                path_dir = pathlib.Path(path + "/" + generateName(dicti))
                path_dir.mkdir(exist_ok=True)

def randomExt(onlyExt = None):
    if onlyExt:
        return onlyExt
    else:
        return ext_file_list[random.randint(0, len(ext_file_list) - 1)]

def createFileRandomly(dicti, file_size: FileSize = None, file_content: FileContent = None, only_ext = None):
    if file_size:
        with open(path + "/" + generateName(dicti) + randomExt(onlyExt=only_ext), "wb") as file:
            file.write(os.urandom(file_size.getSize()))

    else:
        with open(path + "/" + generateName(dicti) + randomExt(onlyExt=only_ext), "w") as file:
            if file_content:
                file.write(file_content.path.read_text())
            else:
                test = ""
                for i in range(0, 100):
                    test += fake.word()
                file.write(test)

def runScript(code):
    if isinstance(code, pathlib.Path):
        script = script_path / code
        exec("from rfg_python import * \n" + script.read_text())
    elif isinstance(code, str):
        exec("from rfg_python import * \n" + code)

def runScriptInGUIConsole(code):
    if isinstance(code, pathlib.Path):
        script = script_path / code

        kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel()
        kernel = kernel_manager.kernel
        kernel_client = kernel_manager.client()
        kernel_client.start_channels()

        console = RichJupyterWidget()
        console.kernel_manager = kernel_manager
        console.kernel_client = kernel_client

        console.execute("from rfg_python import * \n" + script.read_text())
        console.show()
    elif isinstance(code, str):
        kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel()
        kernel = kernel_manager.kernel
        kernel_client = kernel_manager.client()
        kernel_client.start_channels()

        console = RichJupyterWidget()
        console.kernel_manager = kernel_manager
        console.kernel_client = kernel_client

        console.execute("from rfg_python import * \n" + code)
        console.show()