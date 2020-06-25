from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date
import time
import platform
import setting
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getdriver():
    options = webdriver.ChromeOptions()
    if(platform.system() == 'Linux'):
        options.binary_location = '/usr/bin/chromium-browser'
    # options.add_argument("headless")
    # options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--no-sandbox")
    # options.add_argument('--disable-notifications')
    path = "./chromedriver/chromedriver_" + platform.system()
    browser = webdriver.Chrome(path, chrome_options=options)
    return browser


def searcha(browser, video_name, video_title, video_description):
    driver = browser
    driver.get(
        'https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')

    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="identifierId"]').send_keys('cy.test.py@gmail.com')
    time.sleep(5)
    driver.find_element_by_id("identifierNext").click()
    time.sleep(10)
    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('7858306yin')
    time.sleep(5)
    driver.find_element_by_id("passwordNext").click()
    time.sleep(10)
    driver.get('https://www.youtube.com/upload')
    time.sleep(15)
    driver.find_element_by_xpath('//*[@id="select-files-button"]/div').click()
    time.sleep(10)

    keyboard.write(video_name)
    time.sleep(5)
    keyboard.press_and_release('enter')

    time.sleep(10)
    driver.find_element_by_xpath(
        '/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-mention-textbox[1]/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div').send_keys(video_title)
    time.sleep(5)
    driver.find_element_by_xpath(
        '/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-mention-textbox[2]/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div').send_keys(video_description)
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="made-for-kids-group"]/paper-radio-button[1]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="next-button"]/div').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="next-button"]/div').click()
    time.sleep(10)
    driver.find_element_by_xpath(
        '//*[@id="privacy-radios"]/paper-radio-button[3]').click()
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="done-button"]').click()
    time.sleep(5)


def crawlvideolink():
    browser = getdriver()
    video_name = 'Your video full dir'
    video_title = 'Your video title'
    video_description = 'Your video description'

    try:
        searcha(browser, video_name, video_title, video_description)
    except:
        browser.close()
        browser.quit()
    finally:
        browser.close()
        browser.quit()


if __name__ == "__main__":
    start_time = time.time()
    try:
        crawlvideolink()
    except Exception as e:
        pass

    print("--- %s seconds ---" % round(time.time() - start_time, 2))
