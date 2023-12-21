# coding: utf-8
# !/usr/bin/python3



import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

def test_basic_headless_selenium_example():
    """Test selenium installation by opening python website.
    (inspired by https://selenium-python.readthedocs.io/getting-started.html)
    """
    opts = Options()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    driver.get("https://www.tutorialspoint.com/index.htm")
    search = driver.find_element_by_name('key')
    search.send_keys("google search through python")
    search.send_keys(Keys.RETURN) # hit return after you enter search text
    time.sleep(5) # sleep for 5 seconds so you can see the results
    driver.close()