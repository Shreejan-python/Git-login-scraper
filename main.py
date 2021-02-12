from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path = 'D:\Chrome Driver\chromedriver.exe'

browser = webdriver.Chrome(path)
url = 'https://github.com/login'
browser.get(url)

loginid = input("Give your login id : ")
login = browser.find_element_by_id("login_field")
login.send_keys(loginid)

l2 = input("Give your password : ")
password = browser.find_element_by_id("password")
password.send_keys(l2)
browser.find_element_by_name("commit").click()