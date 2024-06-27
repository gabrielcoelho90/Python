from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

PROMISED_DOWN = 280
PROMISED_UP = 120
# CHROME_DRIVER_PATH ="/Users/gabriel/Desktop/"
TWITTER_PASSWORD = "#Coelhomec248"
TWITTER_LOG = "21979798100"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        speed_driver = webdriver.Chrome(options=chrome_options)
        speed_driver.get("https://www.speedtest.net/")
        speed = speed_driver.find_element(By.CSS_SELECTOR, "a.js-start-test")
        speed.click()
        input("enter when ready")
        self.down = speed_driver.find_element(By.CSS_SELECTOR,
                                              "span.result-data-large.number.result-data-value.download"
                                              "-speed").text
        print(f"Down: {self.down}")
        self.up = speed_driver.find_element(By.CSS_SELECTOR,
                                            "span.result-data-large.number.result-data-value.upload-speed").text
        print(f"Up:{self.up}")

    def tweet_at_provider(self):
        tweet_driver = webdriver.Chrome(options=chrome_options)
        tweet_driver.get("https://twitter.com")
        time.sleep(5)
        login_button = tweet_driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                           '1]/div/div/div[3]/div[5]/a/div/span/span')
        login_button.click()
        time.sleep(5)
        phone = tweet_driver.find_element(By.CSS_SELECTOR, "label.css-175oi2r")
        phone.click()
        phone.send_keys(TWITTER_LOG)
        next_button = tweet_driver.find_element(By.CSS_SELECTOR, "div.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r"
                                                                 "-lrvibr.r-ywje51.r-usiww2.r-13qz1uu.r-2yi16.r"
                                                                 "-1qi8awa.r-ymttw5.r-1loqt21.r-o7ynqc.r-6416eg.r"
                                                                 "-1ny4l3l")
        next_button.click()
        time.sleep(3)
        password_container = tweet_driver.find_element(By.CLASS_NAME, "r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r"
                                                                      "-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3"
                                                                      ".r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7")
        password_container.send_keys(TWITTER_PASSWORD)
        time.sleep(3)
        confirm_button = tweet_driver.find_element(By.CLASS_NAME, "css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r"
                                                                  "-19yznuf.r-64el8z.r-1dye5f7.r-1loqt21.r-o7ynqc.r"
                                                                  "-6416eg.r-1ny4l3l")
        confirm_button.click()
        time.sleep(3)
        post_area = tweet_driver.find_element(By.CLASS_NAME,
                                              "public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
        post_area.click()
        post_area.send_keys(
            f"@Claronetempresa, por que pago por no mínimo {PROMISED_DOWN}Mbps de download e {PROMISED_UP}Mbps"
            f" de upload, mas só tenho disponíveis diariamente {self.down}Mbps e {self.up}Mbps?")
        post_it = tweet_driver.find_element(By.CLASS_NAME, "css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r"
                                                           "-19u6a5r.r-2yi16.r-1qi8awa.r-ymttw5.r-1loqt21.r-o7ynqc.r"
                                                           "-6416eg.r-1ny4l3l")
        post_it.click()

internet = InternetSpeedTwitterBot()
internet.get_internet_speed()
internet.tweet_at_provider()
