# составить бота в инстаграмме, который будет с переодичностью в
# 2.5 часа отправлять посты в инстаграмме. Соотвественно для уведомления о том,
# что пост выложен будет использоваться бот в телеграмме, каждый раз отправляющий уведомление
# Также надо реализовать старт работы инста-боты, через команду /start тг боту

# login = ashishksyadav
# password = Omyadav2009

# Посты брать отсюда : https://drive.google.com/drive/folders/1Hdrk2BHNCZPqIE0DzbDLXqaH1BtKOMVE

from config import LOGIN, PASSWORD
from accepting_the_download_images import accept
from time import sleep
import pickle
from selenium import webdriver

# making mobile emulation
user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(profile, executable_path='geckodriver.exe')
driver.set_window_size(360,640)

# class instabot
class instabot:

    def __init__(self):
        # bot authorization
        driver.get('https://www.instagram.com/')
        sleep(2)

        # click button 'enter'
        button_enter = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/div[2]/button')
        button_enter.click()

        # The next lines tell the bot to find the fields to fill in the username and password
        username_input_instabot = driver.find_element_by_name("username")
        password_input_instabot = driver.find_element_by_name("password")

        # Filling in username and password
        username_input_instabot.send_keys(LOGIN)
        password_input_instabot.send_keys(PASSWORD)

        # LOG IN
        login_button_instabot = driver.find_element_by_xpath("//button[@type='submit']")
        try:
            # if log in is successfully
            login_button_instabot.click()
            print('instabot is ready')
        except:
            # if log in is not successfully
            print('instabot is broken')

        # We take cookies or update them
        pickle.dump(driver.get_cookies(), open("cookies_instabot.pkl", "wb"))
        sleep(5)

    def make_posts(self, image, text):
        # authorization using coockie
        cookies_for_instabot = pickle.load(open("cookies_instabot.pkl", "rb"))
        driver.get('https://www.instagram.com/')
        for cookie in cookies_for_instabot:
            driver.add_cookie(cookie)
        # upload image
        driver.find_element_by_css_selector('[data-testid="new-post-button"]').click()
        sleep(15)
        accept(image)
        sleep(15)
        driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/header/div/div[2]/button').click()
        sleep(15)
        driver.find_elements_by_tag_name('textarea')[0].send_keys(text)
        sleep(15)
        driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/header/div/div[2]/button').click()
        sleep(15)

    def set_up(self):
        cookies_for_instabot = pickle.load(open("cookies_instabot.pkl", "rb"))
        driver.get('https://www.instagram.com/')
        sleep(10)
        for cookie in cookies_for_instabot:
            driver.add_cookie(cookie)
        way_to_picture = r'C:\abstract-background-with-green-cloud.jpg'
        # upload image
        driver.find_element_by_css_selector('[data-testid="new-post-button"]').click()
        sleep(10)

    def go_home(self):
        driver.get('https://www.instagram.com/')

BOT = instabot()

