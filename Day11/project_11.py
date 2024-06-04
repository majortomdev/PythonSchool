import bs4
import requests



# below is convenient way to get it to load different pages
# basic_url = 'http://books.toscrape.com/catalogue/page-{}.html'
#
# for p in range(1,11):
#     print(basic_url.format(p))


#basic_url = 'http://books.toscrape.com/catalogue/page-{}.html'



# result = requests.get(basic_url.format('1'))
#
# soup = bs4.BeautifulSoup(result.text, 'html.parser')
#
# books = soup.select('.product_pod')
#
# #example = books[0].select('.star-rating.Three')
# example = books[0].select('a')[1]['title']


# create a URL without page #
basic_url = 'http://books.toscrape.com/catalogue/page-{}.html'

# LIST of 4 and 5 star titles
high_rated_titles = []

# ITERATE pages
for page in range (1,51):

    #CREATE soup on each page
    url_page = basic_url.format(page)
    result = requests.get(url_page)
    soup = bs4.BeautifulSoup(result.text, 'html.parser')

    # SELECT DATA of books
    books = soup.select('.product_pod')
    for book in books:
        # if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) !=0:
        #     high_rated_titles.append(book.select('a')[1]['title'])


        if book.select('.star-rating.Four') or book.select('.star-rating.Five'):
            high_rated_titles.append(book.select('a')[1]['title'])


# print(len(high_rated_titles))
for b in high_rated_titles:
    print(b)




