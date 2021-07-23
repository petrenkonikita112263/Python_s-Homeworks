import bs4
import requests as req

URL_LINK = "https://www.thegoldbugs.com/blog"

resp = req.get(URL_LINK)
soup = bs4.BeautifulSoup(resp.text, "lxml")
# print(soup.prettify())

blog_content = soup.select(".sqs-block-content > pre")
# print(blog_content)
text = blog_content[0]
# print(text)
text = text.contents[0]
# print(text)

text.split("-----")
result = [sentence[0] for sentence in text.split("-----")[1:]]
# print(result)
url_link = "".join(result)
print(url_link)
