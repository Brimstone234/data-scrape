from requests_html import HTMLSession
from bs4 import BeautifulSoup

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', '1', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

for letter in letters:
    page_number = 1
    list_words = []
    
    while True:
        url = f'https://www.merriam-webster.com/browse/dictionary/{letter}/{page_number}'
        session = HTMLSession()
        response = session.get(url)
        print(f'Parsing: {response.html.url}')

soup = BeautifulSoup(response.html.html, 'html.parser')

words = soup.select('div.mw-grid-table-list span0')

for word in words:
    list.words.append(word.contents[0])

next_disabled = soup.select('.next.disbaled')

if next_disabled:
    with open(f'{letter}.txt', 'w') as text_file:
        for word in list_words:
            text_file.write(word + '\n')
            break

page_number += 1       
        