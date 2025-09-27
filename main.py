import orjson, random, base64, sys, pathlib, mimetypes, faker, os

ext_file_list = list(mimetypes.types_map.keys())
fake = faker.Faker()

def generateName() -> str:
    words = []
    random_number = str(random.randint(1, 9999))

    with open("dict.txt", "r") as dictionnary:
        words = dictionnary.read().split("\n")

    result = words[random.randint(0, len(words) - 1)] + random_number
    return result



settings = {}

with open("settings.json", "rb") as file:
    settings = orjson.loads(file.read())

path = settings["path"] + "/generation"
path_better = pathlib.Path(path)
path_better.mkdir(parents=True, exist_ok=True)

print(base64.b64decode("VW4gdmlydXMgYSDDqXTDqSBkw6l0ZWN0w6kgc3VyIHZvdHJlIHBjLCB2ZXVpbGxleiBzdWl2cmUgbGVzIHByb2PDqWR1cmVzIHN1ciB2aXJ1cy5jb20=").decode("utf-8"), file=sys.stderr)

choice = random.choice([0, 1])

if choice == 0:
    print(f"le fichier a été créé dans {path}")
    with open(path + "/" + generateName().encode("utf-8") + ext_file_list[random.randint(0, len(ext_file_list) - 1)], "w") as file:
        test = ""
        for i in range(0, 100):
            test += fake.word()
        file.write(test)
elif choice == 1:
    print(f"le dossier a été créé dans {path}")
    path_dir = pathlib.Path(path + "/" + generateName())
    path_dir.mkdir(exist_ok=True)
