import pathlib, json, inquirer, subprocess, sys

runs: dict = json.loads(pathlib.Path("../data/runs.json").read_text())["runs"]

question = [
    inquirer.List("app_selector",
        message="Select the app to launch.",
        choices=runs.keys()
    )
]
answer = inquirer.prompt(question)

subprocess.run([sys.executable, runs[answer[question[0].name]]+".py"])