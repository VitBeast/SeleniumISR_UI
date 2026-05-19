import time

from pages.profile_page import ProfilePage

from tests.test_login_page import test_go_to_login

import pytest




@pytest.mark.skip
def test_go_to_button_add(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.button_add()
    # browser.save_screenshot('result_button_add.png')


@pytest.mark.regression
def test_go_to_input_name_new_pet(browser):
    link = 'http://34.141.58.52:8080/#/pet-new/pet'
    page = ProfilePage(browser, link)
    page.open()
    page.create_pet_input_name()
    # browser.save_screenshot('result_input_name_new_pet.png')


@pytest.mark.xfail
def test_go_to_dropdown_type_pet(browser):
    link = 'http://34.141.58.52:8080/#/pet-new/pet'
    page = ProfilePage(browser, link)
    page.open()
    page.create_pet_dropdown_type()
    page.create_pet_dropdown_type_dog()
    # browser.save_screenshot('result_dropdown_dog.png')
    page.create_pet_dropdown_type()
    page.create_pet_dropdown_type_cat()
    # browser.save_screenshot('result_dropdown_cat.png')
    page.create_pet_dropdown_type()
    page.create_pet_dropdown_type_reptile()
    # browser.save_screenshot('result_dropdown_reptile.png')
    page.create_pet_dropdown_type()
    page.create_pet_dropdown_type_hamster()
    # browser.save_screenshot('result_dropdown_hamster.png')


@pytest.mark.regression
def test_create_pet_input_age(browser):
    link = 'http://34.141.58.52:8080/#/pet-new/pet'
    page = ProfilePage(browser, link)
    page.open()
    page.create_pet_input_age()
    # browser.save_screenshot('result_input_age.png')


@pytest.mark.smoke
def test_create_pet_dropdown_gender(browser):
    link = 'http://34.141.58.52:8080/#/pet-new/pet'
    page = ProfilePage(browser, link)
    page.open()
    page.create_pet_dropdown_gender()
    # browser.save_screenshot('result_dropdown_gender.png')
    page.create_pet_dropdown_male()
    # browser.save_screenshot('result_dropdown_gender_male.png')
    page.create_pet_dropdown_gender()
    page.create_pet_dropdown_female()
    # browser.save_screenshot('result_dropdown_gender_female.png')


@pytest.mark.xfail
def test_create_pet_button_cancel(browser):
    link = 'http://34.141.58.52:8080/#/pet-new/pet'
    page = ProfilePage(browser, link)
    page.open()
    page.create_pet_button_cancel()
    # browser.save_screenshot('result_button_cancel.png')


@pytest.mark.skip
def test_create_new_pet(browser):
    link = 'http://34.141.58.52:8080/#/pet-new/pet'
    page = ProfilePage(browser, link)
    page.open()
    page.create_new_pet_button_submit()
    test_go_to_login(browser)
    page.button_add()
    page.create_pet_input_name()
    page.create_pet_dropdown_type()
    page.create_pet_dropdown_type_hamster()
    page.create_pet_input_age()
    page.create_pet_dropdown_gender()
    page.create_pet_dropdown_male()
    page.create_new_pet_button_submit()
    page.create_new_pet_button_profile()
    page.create_new_pet_button_edit()
    # browser.save_screenshot('result_new_pet.png')


@pytest.mark.regression
def test_edit_new_pet(browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    test_go_to_login(browser)
    page.edit_new_pet_golem()
    page.edit_input_name_new_pet_golem()
    page.dropdown_edit_type_new_pet_golem()
    page.dropdown_new_type_pet_golem()
    page.edit_new_pet_button_add_avatar()
    page.edit_new_pet_button_add_avatar_click()
    page.edit_new_pet_golem_button_save()
    # browser.save_screenshot('result_new_avatar.png')


@pytest.mark.regression
def test_delete_pet_golem_zmey(browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    test_go_to_login(browser)
    page.delete_pet_golem()
    page.delete_pet_golem_button_yes()
    # browser.save_screenshot('result_delete_pet_golem.png')
