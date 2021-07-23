import os

root_dir = os.getcwd()
# print(root_dir)

for sub_dir, dirs, files in os.walk(root_dir):
    for file in files:
        filepath = sub_dir + os.sep + file
        if filepath.endswith(".txt"):
            print(filepath)
