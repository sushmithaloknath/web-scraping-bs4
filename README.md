# web-scraping-bs4
Programming Languages Scraper with BeautifulSoup

This Python script scrapes the list of programming languages from the Wikipedia page [List of programming languages](https://en.wikipedia.org/wiki/List_of_programming_languages) using the BeautifulSoup library. It extracts and prints the first 20 programming language names from the page.

---

## Features

- Sends an HTTP GET request to the Wikipedia page.
- Parses the HTML content to find programming language names.
- Extracts and prints the first 20 programming languages listed on the page.

---

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

---

## Installation

Install the required Python libraries using pip:

```bash
pip install requests beautifulsoup4
Usage
Run the script using Python:
python wiki.py

Output will display the first 20 programming languages from Wikipedia, for example:
1. A.NET (A#/A sharp)
2. A-0 System
3. A+ (A plus)
4. ABAP
5. ABC
6. ACC
7. Accent (Rational Synergy)
8. Action!
9. ActionScript
10. Actor
11. Ada
12. ISO/IEC 8652
13. Adenine (Haystack)
14. AdvPL
15. Agda
16. Agilent VEE
17. Agora
18. AIMMS
19. Aldor
20. Alef
