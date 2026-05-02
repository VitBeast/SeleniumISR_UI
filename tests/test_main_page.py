import pytest

from pages.main_page import Main_Page

import time

from tests.test_login_page import test_go_to_login


@pytest.mark.regression
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = Main_Page(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(3)
    # browser.save_screenshot('result5.png')


@pytest.mark.smoke
def test_go_to_profile_page(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = Main_Page(browser, link)
    page.open()
    page.go_to_click_logo_pets()
    time.sleep(3)
    page.go_to_profile_page()
    time.sleep(1)
    # browser.save_screenshot('result_go_to_profile_page.png')


@pytest.mark.skip
def test_go_to_quit(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = Main_Page(browser, link)
    page.open()
    page.go_to_click_logo_pets()
    time.sleep(1)
    page.go_to_quit()
    time.sleep(3)
    # browser.save_screenshot('result_quit.png')


@pytest.mark.regression
def test_dropdown_by_pets(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = Main_Page(browser, link)
    page.open()
    page.go_to_click_logo_pets()
    time.sleep(1)
    page.go_to_dropdown_by_pets()
    time.sleep(1)
    page.go_to_dropdown_by_dog()
    time.sleep(1)
    # browser.save_screenshot('result_dropdown_by_dog')
    page.go_to_dropdown_by_pets()
    page.go_to_dropdown_by_cat()
    time.sleep(1)
    # browser.save_screenshot('result_dropdown_by_cat')
    page.go_to_dropdown_by_pets()
    page.go_to_dropdown_by_reptile()
    time.sleep(1)
    # browser.save_screenshot('result_dropdown_by_reptile')
    page.go_to_dropdown_by_pets()
    page.go_to_dropdown_by_hamster()
    time.sleep(1)
    # browser.save_screenshot('result_dropdown_by_hamster.png')
    page.go_to_dropdown_by_pets()
    page.go_to_dropdown_by_parrot()
    time.sleep(1)
    # browser.save_screenshot('result_dropdown_by_hamster.png')


@pytest.mark.skip
def test_search_input_name(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = Main_Page(browser, link)
    page.open()
    page.go_to_click_logo_pets()
    page.go_to_search_input_name_pets()
    time.sleep(1)
    # browser.save_screenshot('result_search_input_pets.png')


@pytest.mark.xfail
def test_put_like_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = Main_Page(browser, link)
    page.open()
    page.go_to_click_logo_pets()
    page.go_to_put_like_pet()
    time.sleep(3)
    # browser.save_screenshot('result_like_pet.png')


@pytest.mark.xfail
def test_add_comment_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = Main_Page(browser, link)
    page.open()
    page.go_to_click_logo_pets()
    page.go_to_open_pet()
    page.go_add_comment_pet()
    page.go_to_button_save_comment()
    time.sleep(3)
    # browser.save_screenshot('result_save_comment.png')


@pytest.mark.smoke
def test_page_forward_page_backward(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = Main_Page(browser, link)
    page.open()
    page.go_to_click_logo_pets()
    time.sleep(1)
    page.go_to_page_forward()
    time.sleep(1)
    # browser.save_screenshot('result_page_forward.png')
    page.go_to_page_end()
    time.sleep(1)
    # browser.save_screenshot('result_page_end.png')
    page.go_to_page_back()
    time.sleep(1)
    # browser.save_screenshot('result_page_back.png')
    page.go_to_page_start()
    time.sleep(1)
    # browser.save_screenshot('result_page_start.png')




