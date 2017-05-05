from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

# to create buyer list
buyers = tree.xpath('//div[@title="buyer-name"]/text()')

# to create price list
prices = tree.xpath('//span[@class="item-price"]/text()')


#proofs
print 'Buyers: ', buyers
print '\n\n'
print 'Prices: ', prices
