from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import os
driver=webdriver.Chrome()

driver.get('https://www.torrentbd.net/torrent/account-login.php?returnto=%2Ftorrent%2F')

username=driver.find_element_by_id("username")
username.clear()
username.send_keys('')

password=driver.find_element_by_id("password")
password.clear()
password.send_keys('')
driver.find_element_by_name('action').click()

torrent_id=00000

while(1):
    driver.get('https://www.torrentbd.net/torrent/torrents-details.php?id=%d' % torrent_id)
    try:
        print('try')
        driver.find_element_by_id('thanks-button').click()
        text=driver.find_element_by_id('user-sb').text
        print(text)
        os.system('echo %d >> record.txt' % torrent_id)
        torrent_id+=1
        time.sleep(60)
    except NoSuchElementException:
        torrent_id+=1
        continue
