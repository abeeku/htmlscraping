import urllib2

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

page = urllib2.urlopen(wiki)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page)

print soup.title

print '\n'

print soup.title.string

print '\n'

print soup.a
print '\n'

all_tables = soup.find_all('table')

right_table = soup.find('table', class_='wikitable sortable plainrowheaders')
ar=[]

br=[]

cr=[]

dr=[]

er=[]

fr=[]

gr=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states = row.findAll('th') # to store second column data
    if len(cells) == 6:
        ar.append(cells[0].find(text=True))
        br.append(states[0].find(text=True))
        cr.append(cells[1].find(text=True))
        dr.append(cells[2].find(text=True))
        er.append(cells[3].find(text=True))
        fr.append(cells[4].find(text=True))
        gr.append(cells[5].find(text=True))

#import pandas to convert list to data frame

import pandas as pd

df = pd.DataFrame(ar,columns = ['Number'])

df['State/UT'] = br
df['Admin_Capital'] = cr
df['Legistlative_Capital'] = dr
df['Judiciary_Capital'] = er
df['Year_Capital'] = fr
df['Former_Capital'] = gr

print df


