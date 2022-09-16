
from unicodedata import name
from bs4 import BeautifulSoup
import urllib.request
quote_page = 'https://www.drupal.org/project/project_module?f%5B0%5D=&f%5B1%5D=&f%5B2%5D=&f%5B3%5D=&f%5B4%5D=sm_field_project_type%3Afull&f%5B5%5D=&f%5B6%5D=&text=&solrsort=iss_project_release_usage+desc&op=Search'
weburl = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(weburl, 'html.parser')
name_box = soup.find('div', attrs={'class': 'node'}).find('h2').find('a').get('href')
print(name_box)
#project page

project_url = "https://www.drupal.org"+ name_box
print(project_url)
projecturl = urllib.request.urlopen(project_url)
soup2 = BeautifulSoup(projecturl, 'html.parser')
name_box  = soup2.find('div',attrs={'class':'user-picture'}).find('a').get('href')
print(name_box)

#profile page

profile_url = "https://www.drupal.org" + name_box
print(profile_url)
profileurl = urllib.request.urlopen(profile_url)
soup3 = BeautifulSoup(profileurl, 'html.parser')
name_box  = soup3.find('h1',attrs={'id':'page-title'}).text
print(name_box)
social_box = soup3.find('div',attrs={'class':'field-name-field-social-links'}).findAll('div', attrs={'class':'field-item'})
for social in social_box:
    print(social.find('a').get('href'))
