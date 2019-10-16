from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import time
import os

browser = webdriver.Firefox();

browser.get("http://result.dghs.gov.bd/mbbs")




#roll_number=191890
#roll_number=110001
roll_number = 110001

while(True):
    time.sleep(1)

    roll_number+=1

    pyautogui.press('tab')
    pyautogui.typewrite(str(roll_number))
    pyautogui.press('enter')
    pyautogui.press('enter')        

    time.sleep(2)

    #selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [id="rockartists"]

    try:
        table=browser.find_element_by_id("rockartists")
        row=table.find_elements_by_tag_name("td")
        #[0] [1]

        write_str=row[1].text+' '+row[0].text

        with open("name.txt","a") as myfile:
            myfile.write(write_str+'\n')
    except NoSuchElementException:
        continue


            # while(True):
        #     time.sleep(1)
        #     roll_number+=1
        #     pyautogui.press('tab')
        #     pyautogui.typewrite(str(roll_number))
        #     pyautogui.press('enter')
        #     pyautogui.press('enter')

