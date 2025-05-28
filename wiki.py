import requests
from bs4 import BeautifulSoup

# Wikipedia URL
url = "https://en.wikipedia.org/wiki/List_of_programming_languages"

# Send a GET request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all programming language names (they are inside <li> tags under specific divs)
languages = soup.select("div.div-col li a")

# Print the first 20 programming languages
for i, lang in enumerate(languages[:20], start=1):  
    print(f"{i}. {lang.get_text()}")
