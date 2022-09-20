
from unicodedata import name
from bs4 import BeautifulSoup
import urllib.request
quote_page = 'https://www.drupal.org/project/project_module?f%5B0%5D=&f%5B1%5D=&f%5B2%5D=&f%5B3%5D=&f%5B4%5D=sm_field_project_type%3Afull&f%5B5%5D=&f%5B6%5D=&text=&solrsort=iss_project_release_usage%20desc&op=Search'
count = 0
while(count<=1000):
    project_url_list = []
    weburl = urllib.request.urlopen(quote_page)
    soup = BeautifulSoup(weburl, 'html.parser')
    project_box = soup.findAll('div', attrs={'class': 'node'})
    for name in project_box:
        url = "https://www.drupal.org"+ name.find('h2').find('a').get('href')
        project_url_list.append(url)

    for project_url in project_url_list:
        projecturl = urllib.request.urlopen(project_url)
        soup2 = BeautifulSoup(projecturl, 'html.parser')
        profile_box  = soup2.findAll('div',attrs={'class':'user-picture'})
        profile_url_list = []
        for profile in profile_box:
            profile_url_list.append("https://www.drupal.org" + profile.find('a').get('href'))
    
        #print project url
        #print all details 
        for profile_url in profile_url_list:
            profileurl = urllib.request.urlopen(profile_url)
            soup3 = BeautifulSoup(profileurl, 'html.parser')
            name_box  = soup3.find('h1',attrs={'id':'page-title'}).text
            print(count, name_box, end=" ")
            count = count + 1
            print(profile_url, end= " ")
            try:
                social_box = soup3.find('div',attrs={'class':'field-name-field-social-links'}).findAll('div', attrs={'class':'field-item'})
                for social in social_box:
                    if(social.find('a').text.strip()=='LinkedIn' or social.find('a').text.strip()=='Twitter'):
                        print(social.find('a').get('href'), end=" ")
            except:
                print("Social media links not provided",end=" ")
            print(project_url)
    page_number = 0
    page_number = page_number + 1
    quote_page='https://www.drupal.org/project/project_module?page='+str(page_number)+'&f%5B0%5D=&f%5B1%5D=&f%5B2%5D=&f%5B3%5D=&f%5B4%5D=sm_field_project_type%3Afull&f%5B5%5D=&f%5B6%5D=&text=&solrsort=iss_project_release_usage%20desc&op=Search'
