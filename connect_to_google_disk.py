import time
import os
from selenium import webdriver
from config import LINK


def check_new_files():
    new_files = 0
    downloaded_files = []
    f = open('downloaded_files.txt','r+')
    for file_name in f.readlines():
        downloaded_files.append(str(file_name)[:-1])
    f.close()
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/14.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5];FBNV/1"
    if (os.path.isdir('C:\images')) is not True:
        os.mkdir('C:\images')
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", user_agent)
    profile.set_preference("browser.download.folderList",2)
    profile.set_preference("browser.download.dir", 'C:\images') #Set the last directory used for saving a file from the "What should (browser) do with this file?" dialog.
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg") #list of MIME types to save to disk without asking what to use to open the file
    driver1 = webdriver.Firefox(profile, executable_path='geckodriver.exe')
    driver1.set_window_size(360,640)
    driver1.get(LINK)
    time.sleep(5)
    for link in driver1.find_elements_by_class_name("a-N-Bb-xb-Mc"):
        link.click()
        time.sleep(4)
        name_of_file1 =  "C:\images" + "\shit" + driver1.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[1]/div[3]/div[1]').text
        name_of_file = name_of_file1.replace("shit", '')
        if name_of_file in downloaded_files:
            driver1.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[1]/div[1]/div').click()
            time.sleep(4)
            continue
        else:
            downloaded_files_for_check = open('downloaded_files.txt', 'a')
            downloaded_files_for_check.write(name_of_file + '\n')
            downloaded_files_for_check.close()
            new_files +=1
            print('new image was found')
            print(name_of_file)
        time.sleep(4)
        driver1.find_element_by_xpath("/html/body/div[6]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div").click()
        time.sleep(10)
        driver1.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[1]/div[1]/div').click()
        time.sleep(4)
    driver1.close()
    return new_files

