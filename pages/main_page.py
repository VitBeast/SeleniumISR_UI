
from .locators import MainPageLocators

from .base_page import Base_Page

from selenium.webdriver.common.keys import Keys

class Main_Page(Base_Page):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_profile_page(self):
        button_profile = self.browser.find_element(*MainPageLocators.BUTTON_PROFILE)
        button_profile.click()

    def go_to_click_logo_pets(self):
        logo_pets = self.browser.find_element(*MainPageLocators.LOGO_PETS)
        logo_pets.click()

    def go_to_quit(self):
        button_quit = self.browser.find_element(*MainPageLocators.BUTTON_QUIT)
        button_quit.click()

    def go_to_dropdown_by_pets(self):
        dropdown_by_pets = self.browser.find_element(*MainPageLocators.DROPDOWN_BY_PETS)
        dropdown_by_pets.click()

    def go_to_dropdown_by_dog(self):
        dropdown_by_dog = self.browser.find_element(*MainPageLocators.DROPDOWN_BY_DOG)
        dropdown_by_dog.click()

    def go_to_dropdown_by_cat(self):
        dropdown_by_cat = self.browser.find_element(*MainPageLocators.DROPDOWN_BY_CAT)
        dropdown_by_cat.click()

    def go_to_dropdown_by_reptile(self):
        dropdown_by_reptile = self.browser.find_element(*MainPageLocators.DROPDOWN_BY_REPTILE)
        dropdown_by_reptile.click()

    def go_to_dropdown_by_hamster(self):
        dropdown_by_hamster = self.browser.find_element(*MainPageLocators.DROPDOWN_BY_HAMSTER)
        dropdown_by_hamster.click()

    def go_to_dropdown_by_parrot(self):
        dropdown_by_parrot = self.browser.find_element(*MainPageLocators.DROPDOWN_BY_PARROT)
        dropdown_by_parrot.click()

    def go_to_search_input_name_pets(self):
        search_input_name = self.browser.find_element(*MainPageLocators.SEARCH_INPUT_NAME)
        search_input_name.send_keys('Bunny' + Keys.ENTER)

    def go_to_put_like_pet(self):
        like_pet = self.browser.find_element(*MainPageLocators.LIKE_PET)
        like_pet.click()

    def go_to_open_pet(self):
        button_details = self.browser.find_element(*MainPageLocators.BUTTON_DETAILS)
        button_details.click()

    def go_add_comment_pet(self):
        input_comment = self.browser.find_element(*MainPageLocators.INPUT_COMMENT)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", input_comment)
        input_comment.send_keys('Best animal!!!><!!!')

    def go_to_button_save_comment(self):
        button_save = self.browser.find_element(*MainPageLocators.BUTTON_SAVE_COMMENT)
        button_save.click()

    def go_to_page_forward(self):
        page_forward = self.browser.find_element(*MainPageLocators.ICON_PAGE_FORWARD)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", page_forward)
        page_forward.click()

    def go_to_page_end(self):
        page_end = self.browser.find_element(*MainPageLocators.ICON_PAGE_FORWARD_END)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", page_end)
        page_end.click()

    def go_to_page_back(self):
        page_back = self.browser.find_element(*MainPageLocators.ICON_PAGE_BACK)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", page_back)
        page_back.click()

    def go_to_page_start(self):
        page_start = self.browser.find_element(*MainPageLocators.ICON_PAGE_BACK_TO_START)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", page_start)
        page_start.click()

