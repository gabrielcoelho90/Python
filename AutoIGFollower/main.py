from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

USERNAME = "fornopreaquecido"
PASSWORD = "#Fortuna248"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com")

# login
username = driver.find_element(By.NAME, "username")
username.click()
username.send_keys(USERNAME)
time.sleep(3)
password = driver.find_element(By.NAME, "password")
password.click()
password.send_keys(PASSWORD)
login_button = driver.find_element(By.CSS_SELECTOR, "button._acan._acap._acas._aj1-._ap30")
login_button.click()
time.sleep(5)
not_now = driver.find_element(By.CSS_SELECTOR, "div._ac8f")
not_now.click()
time.sleep(3)
notification_off = driver.find_element(By.CSS_SELECTOR, "button._a9--._ap36._a9_1")
notification_off.click()

# search content page
time.sleep(2)
search_colum = driver.find_elements(By.CSS_SELECTOR, "div.x9f619.x3nfvp2.xr9ek0c.xjpr12u.xo237n4.x6pnmvc.x7nr27j"
                                                     ".x12dmmrz.xz9dl7a.xn6708d.xsag5q8.x1ye3gou.x80pfx3.x159b3zp"
                                                     ".x1dn74xm.xif99yt.x172qv1o.x10djquj.x1lhsz42.xzauu7c.xdoji71"
                                                     ".x1dejxi8.x9k3k5o.xs3sg5q.x11hdxyr.x12ldp4w.x1wj20lx.x1lq5wgf"
                                                     ".xgqcy7u.x30kzoy.x9jhf4c")
search_colum[2].click()
time.sleep(2)
search_bar = driver.find_element(By.CSS_SELECTOR, 'input.x1lugfcp.x19g9edo.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x972fbf'
                                                  '.xcfux6l.x1qhh985.xm0m39n.x9f619.x5n08af.xl565be.x5yr21d.x1a2a7pz'
                                                  '.xyqdw3p.x1pi30zi.xg8j3zb.x1swvt13.x1yc453h.xh8yej3.xhtitgo'
                                                  '.xs3hnx8.x1dbmdqj.xoy4bel.x7xwk5j')
search_bar.send_keys("tastydemais")
time.sleep(2)
profile = driver.find_element(By.CSS_SELECTOR, "div div a div div.x9f619.x1n2onr6.x1ja2u2z.x1qjc9v5.x78zum5.xdt5ytf"
                                               ".x1iyjqo2.xl56j7k.xeuugli")
profile.click()
time.sleep(4)
tastydemais = driver.find_element(By.CSS_SELECTOR, "ul.x78zum5.x1q0g3np.xieb3on li a")
tastydemais.click()
time.sleep(2)
followers = driver.find_elements(By.CSS_SELECTOR, "div.x9f619.x1n2onr6.x1ja2u2z.xdt5ytf.x2lah0s.x193iq5w.xeuugli"
                                                  ".xamitd3.x78zum5 div button")
for follow in followers:
    try:
        follow.click()
        time.sleep(1)
    except ElementClickInterceptedException:
        cancel_button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
        cancel_button.click()


# driver.quit()
