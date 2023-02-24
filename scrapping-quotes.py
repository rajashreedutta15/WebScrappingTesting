from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

quotes_page = 'https://bluelimelearning.github.io/my-fav-quotes/'
uClient = uReq(quotes_page)
page_html = uClient.read()
uClient.close
page_soup = soup(page_html, "html.parser")
quotes = page_soup.findAll("div", {"class" : "quotes"})

for i in quotes:
    fav_quote = i.findAll("p", {"class" : "aquote"})
    aquote = fav_quote[0].text.strip()

    fav_authors = i.findAll("p", {"class" : "author"})
    author = fav_authors[0].text.strip()

    print(aquote)
    print(author)

    

