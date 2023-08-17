from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InstagramBot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.my_login = 'juniorvanstota3@gmail.com'
        self.my_password = 'Totavans157@'
        
    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        login_element = self.driver.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_element.click()
        login_element.send_keys(self.my_login)
        password_element = self.driver.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_element.click()
        password_element.send_keys(self.my_password)
        btn_login = self.driver.find_element('xpath', '//*[@id="loginForm"]/div/div[3]')
        btn_login.click()
        time.sleep(5)
        self.like_photos('brfootball')

        
    def like_photos(self, page):
        self.driver.get(f'https://www.instagram.com/{page}/')
        time.sleep(5)
        for i in range(1,3):
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)
        # hrefs = self.driver.find_elements(By.TAG_NAME, 'a')
        hrefs = self.driver.find_elements('xpath', '//a[@href]')
        pic_hrefs = []
        
        for elem in hrefs:
            if elem.get_attribute('href').startswith('https://www.instagram.com/p/'):
                pic_hrefs.append(elem.get_attribute('href'))
        [href for href in pic_hrefs if page in href]
        print(page + ' photos '+ str(len(pic_hrefs)))
        
        # self.driver.get('https://www.instagram.com/p/CwDMy48oq-R/')
        # time.sleep(6)


        
        # time.sleep(500)
        for pic_href in pic_hrefs:
            print(str(pic_href))
            self.driver.get(pic_href)
            time.sleep(5)
            like_button = self.driver.find_element(By.XPATH, "//*[local-name()='svg' and @aria-label='Like']")
            like_button.click()
            time.sleep(5)
            # self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')   
            # try:
            #     time.sleep(15)
            # except Exception as e:
            #     time.sleep(5)

bot = InstagramBot()
bot.login()