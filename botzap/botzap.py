from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WhatsappBot:
    def __init__(self):
        self.msg = 'Test Message boot'
        self.groups = ['Testbot1', 'Testbot2', 'Parada Gay 🏳‍🌈💗💝🎉🌈🌟🦌👨‍👨‍👦👨‍👨‍👦‍👦']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome()
        
        
    def SendMessage(self):
    #    <span dir="auto" title="Testbot2" aria-label="" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr _11JPr">Testbot2</span>
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)
        for group in self.groups:
            group = self.driver.find_element('xpath', f"//span[@title='{group}']" )
            time.sleep(2)
            group.click()
            chat_box = self.driver.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            time.sleep(2)
            chat_box.click()
            chat_box.send_keys(self.msg)
            btn_send = self.driver.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
            time.sleep(2)
            btn_send.click()
            time.sleep(5)
            
bot = WhatsappBot()
bot.SendMessage()