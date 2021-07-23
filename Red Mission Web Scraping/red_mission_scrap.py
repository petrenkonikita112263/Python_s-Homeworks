import bs4
import requests as req

URL_LINK = "https://www.thegoldbugs.com/blog"

resp = req.get(URL_LINK)
soup = bs4.BeautifulSoup(resp.text, "lxml")
print(soup.prettify())
