import cmd, orjson, pathlib, shutil


class helper_term(cmd.Cmd):
    intro = "Welcome to Random File Generator Helper"
    prompt = ">>> "

    def __init__(self):
        super().__init__()
        self.settings = {}
        self.groups_path = pathlib.Path("groups")
        self.groups_path.mkdir(exist_ok=True)
        with open("settings.json", "r") as file:
            self.settings = orjson.loads(file.read())

        self.path = pathlib.Path(self.settings["path"]) / "generation"


    def do_exit(self, arg):
        """
Quit the helper
Syntaxe: exit
        """
        print("Goodbye !")
        return True

    def do_find(self, arg):
        """
Find file with the ext of file (like .png)
Syntaxe: find <ext>
        """
        path = pathlib.Path(self.settings["path"])
        file_list = list(path.walk())

        for dirpath, dirname, filename in file_list:
            for i, e in enumerate(filename):
                if e.endswith(arg):
                    print(f"{e} -> {dirpath/e}")

    def do_delall(self, arg):
        """
Delete all file and directory in generation directory
Syntaxe: delall
        """
        shutil.rmtree(self.path)
        self.path.mkdir()

    def do_group(self, arg):
        """
Create group with the generation dir content and name it or delete it
Syntaxe: group create <name> / group del <name> / group delall / group list / group rename <target> <new_name>
        """
        args = str.split(arg, " ")
        if args[0] == "create":
            shutil.copytree(self.path, self.groups_path / args[1])
            shutil.rmtree(self.path)
            self.path.mkdir(exist_ok=True)
        elif args[0] == "del":
            if self.exist_dir(args[1]):
                shutil.rmtree(self.groups_path / args[1])
        elif args[0] == "delall":
            shutil.rmtree(self.groups_path)
            self.groups_path.mkdir(exist_ok=True)
        elif args[0] == "list":
            dirs = [d.name for d in self.groups_path.iterdir() if d.is_dir()]
            for i in dirs:
                print(i)
        elif args[0] == "rename":
            if self.exist_dir(args[1]):
                shutil.copytree(self.groups_path / args[1], self.groups_path / args[2])
                shutil.rmtree(self.groups_path / args[1])

    def default(self, line):
        print(f"Command not found: {line}")

    def exist_dir(self, target_file):
        for dirpath, dirname, filename in self.groups_path.walk():
            for i in dirname:
                if target_file == i:
                    return True

        return False

if __name__ == '__main__':
    helper_term().cmdloop()