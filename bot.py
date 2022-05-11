from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
import random
import sys

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'http://www.instagram.com'
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.login()

    

    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
        time.sleep(2) 

    def nav_user(self,user):
        self.driver.get('{}/{}/'.format(self.base_url,user))

    def nav_winnipeg(self):
        self.driver.get(self.base_url+'/explore/locations/216708652/winnipeg-manitoba/')
        time.sleep(2)

    def nav_hashtag(self,hashtag):
        self.driver.get(self.base_url+'/explore/tags/'+hashtag)
        time.sleep(2)

    def like_pic(self):
        pic_hrefs = []
        for i in range(1, 7):
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = self.driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            self.driver.get(pic_href)
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: self.driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1
    

if __name__ == '__main__':
    ig_bot = InstagramBot('garnishedbygurman','chris3paul')
    ig_bot.nav_hashtag('cooking')
    ig_bot.like_pic()

