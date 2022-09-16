
from unicodedata import name
from bs4 import BeautifulSoup
import urllib.request
project_url_list = []
profile_url_list = []
quote_page = 'https://www.drupal.org/project/project_module?f%5B0%5D=&f%5B1%5D=&f%5B2%5D=&f%5B3%5D=&f%5B4%5D=sm_field_project_type%3Afull&f%5B5%5D=&f%5B6%5D=&text=&solrsort=iss_project_release_usage%20desc&op=Search'
weburl = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(weburl, 'html.parser')
project_box = soup.findAll('div', attrs={'class': 'node'})
for name in project_box:
    project_url_list.append("https://www.drupal.org"+ name.find('h2').find('a').get('href'))
#project page

for project_url in project_url_list:
    projecturl = urllib.request.urlopen(project_url)
    soup2 = BeautifulSoup(projecturl, 'html.parser')
    profile_box  = soup2.findAll('div',attrs={'class':'user-picture'})
    for profile in profile_box:
        profile_url_list.append("https://www.drupal.org" + profile.find('a').get('href'))
# profile page

for profile_url in profile_url_list:
    profileurl = urllib.request.urlopen(profile_url)
    soup3 = BeautifulSoup(profileurl, 'html.parser')
    name_box  = soup3.find('h1',attrs={'id':'page-title'}).text
    print(name_box)
    try:
        social_box = soup3.find('div',attrs={'class':'field-name-field-social-links'}).findAll('div', attrs={'class':'field-item'})
        for social in social_box:
            print(social.find('a').get('href'))
    except:
        print("no social media")
