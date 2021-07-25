import re

with open("message_new_pen.txt") as file:
    content = file.read()

# print(content)

coordinates = re.findall(r"[\d]+.[\d]+,-[\d]+.[\d]+", content)
print(coordinates)
