# Завдання: за допомогою браузера (Selenium) відкрити форму за наступним посиланням:
# https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link
# заповнити і відправити її.
# Зберегти два скріншоти: заповненої форми і повідомлення про відправлення форми.
# В репозиторії скріншоти зберегти.

import os

from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_profile_path = os.getcwd() + "/chrome_profiles/profile1"
link = "https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link"

options = ChromeOptions()
options.add_argument("--no sandbox")

options.add_argument(f"--user-data-dir={chrome_profile_path}")

if not os.path.exists(chrome_profile_path):
    os.makedirs(chrome_profile_path)

wd = Chrome(options=options, executable_path=os.getcwd() + "/chromedriver")

wd.get(link)
input_field = wd.find_element(By.CSS_SELECTOR, "input[jsname=YPqjbf]")
while not EC.presence_of_element_located(input_field):
    sleep(5)

input_field.send_keys("Oleh")

wd.save_screenshot("filled_form.png")

send_button = wd.find_element(By.CSS_SELECTOR, "div[role=button ]")

send_button.click()

wd.save_screenshot("sent_form.png")
