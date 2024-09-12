import os

FOLDER = "short"

for proc in os.listdir(FOLDER):
    proc_path = os.path.join(FOLDER, proc)

    proc_content = open(proc_path, "r").read().strip().replace("\n", " ").replace("\r", " ").strip()

    print(proc_path.replace("\\", "/"), "\t", proc_content)
