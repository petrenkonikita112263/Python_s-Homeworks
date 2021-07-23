import os
import re


def create_result_file():
    with open("./founded_links.txt", "w") as result_file:
        result_file.write("")


root_dir = os.getcwd()
# print(root_dir)
create_result_file()

for sub_dir, dirs, files in os.walk(root_dir):
    if sub_dir != root_dir:
        for file in files:
            filepath = sub_dir + os.sep + file
            if filepath.endswith(".txt"):
                # print(filepath)
                with open(filepath) as f:
                    f_content = f.read()
                    # print(f_content)
                    urls = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
                                      f_content)
                    # print(urls)
                    with open("./founded_links.txt", "a") as result_file:
                        result_file.writelines(f"{urls}\n")
