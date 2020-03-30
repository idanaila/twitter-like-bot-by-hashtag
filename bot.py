from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class twitter:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #for IE browser
        #self.bot = webdriver.Ie(executable_path = r'C:\Users\me\Documents\IEDriverServer')
        self.bot = webdriver.Firefox(executable_path = r'C:\Users\me\Documents\geckodriver')

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        #close the prompt shown in the bottom of the page
        closebottomprompt = bot.find_element_by_xpath('//div[@class="css-18t94o4 css-1dbjc4n r-1niwhzg r-11mg6pl r-sdzlij r-1phboty r-rs99b7 r-18kxxzh r-1q142lx r-1w2pmg r-1n0xq6e r-1mnahxq r-1vsu8ta r-aj3cln r-1fneopy r-o7ynqc r-6416eg r-lrvibr"]').click()
        time.sleep(5)
        #will search for credentials fields
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        #will clear credentials fields in case they are already completed
        email.clear()
        password.clear()
        #will sent the credentials and hit
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
    def like(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(5)
        for i in range(1, 100):
            #scroll by entire document
            #bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            bot.execute_script("window.scrollTo(0, 48)")
            time.sleep(5)
            tweets = bot.find_elements_by_xpath('//div[@class="css-18t94o4 css-1dbjc4n r-1777fci r-11cpok1 r-1ny4l3l r-bztko3 r-lrvibr" and @data-testid="like"]')
            for x in range(0, len(tweets)):
                #tweets = bot.find_elements_by_xpath('//div[@class="css-18t94o4 css-1dbjc4n r-1777fci r-11cpok1 r-1ny4l3l r-bztko3 r-lrvibr" and @data-testid="like"]')
                if tweets[x].is_displayed():
                    tweets[x].click()
                    time.sleep(4)
                    
            
            
tw = twitter('xxx@gmail.com', 'xxx')
tw.login()
tw.like('programming')
