from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

def find_element(web_element : WebElement, by: By, value):
    try:
        # Try to find a single element
        element = web_element.find_element(by,value)
        return element
    except NoSuchElementException:
        # Handle the exception
       return None