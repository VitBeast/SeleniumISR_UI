import pytest
from selenium import webdriver
# еще можно ставить в фикстуру (scope='class') (autouse=True)

@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
