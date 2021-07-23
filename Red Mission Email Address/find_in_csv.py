import pandas as pd

df = pd.read_csv("download_link.csv", header=None)
# print(df)
# print(df[2])
url_link = "".join(df[2])

with open("download_link_to_pdf_file.txt", "w") as file:
    file.write(url_link)
