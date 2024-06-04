import bs4
import requests

#result = requests.get('https://www.videoschool.com/')

#print(type(result))
#print(result.text)

#soup = bs4.BeautifulSoup(result.text, 'html.parser')

#print(soup.select('h1'))
# print(soup.select('title'))
# print(soup.select('title')[0])
# print(soup.select('title')[0].getText())
# print()
# print(soup.select('p')[5].getText())

print()
print("####********************************####")
print()
# central_block = soup.select('.fusion-text.fusion-text-1 h5')
# for h in central_block:
#     print(h.getText())
print()
print("####********************************####")
print()
result = requests.get('https://www.videoschool.com/photography/')
#result = requests.get('http://midasselect.com/')
soup = bs4.BeautifulSoup(result.text, 'html.parser')

images = soup.select('.img-responsive')[0]['src']
print(images)

image1 = requests.get(images)

f = open('my_image.jpg', 'wb')
f.write(image1.content)
f.close()



