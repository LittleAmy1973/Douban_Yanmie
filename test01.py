import re
from urllib import request
import requests
import soup as soup
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://movie.douban.com/")
#assert "Python" in driver.title
elem = driver.find_element_by_name("search_text")
elem.clear()
elem.send_keys("湮灭")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
#driver.close()

sreach_window=driver.current_window_handle

#获得网址
xpath_urls = '//div[@class="item-root"]/a'
urls_pre = driver.find_elements_by_xpath(xpath_urls)
url = urls_pre[0].get_attribute("href")
print(url)
#print(type(url))

driver.close()
driver = webdriver.Chrome()
driver.get(url)

elem = driver.find_elements_by_id("info")

print(elem[0].text)

















































'''
#解压网址
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read()
page_info = page_info.decode('utf-8')
soup = BeautifulSoup(page_info, 'html.parser')

print(soup)
#读出info的信息
for k in soup.find_all('div',id='info'):#,string='更多'
    print(k)



'''














'''
for link in driver.find_elements_by_xpath("//div[@class='item-root']"):
    print(link)
'''

'''
a = driver.find_element_by_xpath("//div[@class='item-root']/a[0]")
print(a)
'''
'''
driver.get("http://"+url)
#sreach_window=browser.current_window_handle
elem = driver.find_element_by_xpath("//div[@id='info']")

print(elem)
'''


'''
for link in driver.find_elements_by_xpath("//*[@href]"):
    print (link.get_attribute('href'))
'''
#driver.find_elements_by_xpath("//div[@class='item-root']/a")