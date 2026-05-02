from .base_page import Base_Page

from .locators import ProfilePageLocators

from selenium.webdriver.common.keys import Keys

from pathlib import Path




class ProfilePage(Base_Page):
    def button_add(self):
        button_add = self.browser.find_element(*ProfilePageLocators.BUTTON_ADD)
        button_add.click()

    def create_pet_input_name(self):
        input_name = self.browser.find_element(*ProfilePageLocators.INPUT_NAME)
        input_name.send_keys('Golem')

    def create_pet_dropdown_type(self):
        dropdown_type = self.browser.find_element(*ProfilePageLocators.DROPDOWN_TYPE_PET)
        dropdown_type.click()

    def create_pet_dropdown_type_dog(self):
        dropdown_type_dog = self.browser.find_element(*ProfilePageLocators.DROPDOWN_TYPE_DOG)
        dropdown_type_dog.click()

    def create_pet_dropdown_type_cat(self):
        dropdown_type_cat = self.browser.find_element(*ProfilePageLocators.DROPDOWN_TYPE_CAT)
        dropdown_type_cat.click()

    def create_pet_dropdown_type_reptile(self):
        dropdown_type_reptile = self.browser.find_element(*ProfilePageLocators.DROPDOWN_TYPE_REPTILE)
        dropdown_type_reptile.click()

    def create_pet_dropdown_type_hamster(self):
        dropdown_type_hamster = self.browser.find_element(*ProfilePageLocators.DROPDOWN_TYPE_HAMSTER)
        dropdown_type_hamster.click()

    def create_pet_input_age(self):
        input_age = self.browser.find_element(*ProfilePageLocators.INPUT_AGE)
        input_age.send_keys('4')

    def create_pet_dropdown_gender(self):
        dropdown_gender = self.browser.find_element(*ProfilePageLocators.DROPDOWN_GENDER)
        dropdown_gender.click()

    def create_pet_dropdown_male(self):
        dropdown_male = self.browser.find_element(*ProfilePageLocators.DROPDOWN_GENDER_MALE)
        dropdown_male.click()

    def create_pet_dropdown_female(self):
        dropdown_female = self.browser.find_element(*ProfilePageLocators.DROPDOWN_GENDER_FEMALE)
        dropdown_female.click()

    def create_pet_button_cancel(self):
        button_cancel = self.browser.find_element(*ProfilePageLocators.BUTTON_CANCEL)
        button_cancel.click()

    def create_new_pet_button_submit(self):
        button_submit = self.browser.find_element(*ProfilePageLocators.BUTTON_SUBMIT)
        button_submit.click()

    def create_new_pet_button_edit(self):
        button_edit = self.browser.find_element(*ProfilePageLocators.BUTTON_EDIT)
        button_edit.click()

    def create_new_pet_button_profile(self):
        button_profile = self.browser.find_element(*ProfilePageLocators.BUTTON_PROFILE)
        button_profile.click()

    def delete_pet_golem(self):
        delete_pet = self.browser.find_element(*ProfilePageLocators.BUTTON_DELETE_PET_GOLEM)
        delete_pet.click()

    def delete_pet_golem_button_yes(self):
        button_yes = self.browser.find_element(*ProfilePageLocators.BUTTON_DELETE_PET_GOLEM_YES)
        button_yes.click()

    def edit_new_pet_golem(self):
        edit_pet = self.browser.find_element(*ProfilePageLocators.BUTTON_EDIT)
        edit_pet.click()

    def edit_input_name_new_pet_golem(self):
        input_new_name_pet_golem = self.browser.find_element(*ProfilePageLocators.EDIT_INPUT_NAME_NEW_PET_GOLEM)
        input_new_name_pet_golem.click()
        input_new_name_pet_golem.send_keys(Keys.CONTROL + 'a')
        input_new_name_pet_golem.send_keys(Keys.DELETE)
        input_new_name_pet_golem.send_keys('Zmey')

    def dropdown_edit_type_new_pet_golem(self):
        dropdown_edit_type = self.browser.find_element(*ProfilePageLocators.DROPDOWN_EDIT_TYPE_NEW_PET_GOLEM)
        dropdown_edit_type.click()

    def dropdown_new_type_pet_golem(self):
        new_type_pet = self.browser.find_element(*ProfilePageLocators.DROPDOWN_NEW_TYPE_PET_GOLEM)
        new_type_pet.click()


    def edit_new_pet_button_add_avatar(self):
        button_add_avatar = self.browser.find_element(*ProfilePageLocators.EDIT_NEW_PET_BUTTON_ADD_AVATAR)

        file_path = Path(__file__).resolve().parents[1] / "snake.jpg"

        print(file_path)
        button_add_avatar.send_keys(str(file_path))

    def edit_new_pet_button_add_avatar_click(self):
        add_avatar_click = self.browser.find_element(*ProfilePageLocators.ADD_AVATAR_CLICK)
        add_avatar_click.click()


    def edit_new_pet_golem_button_save(self):
        button_save = self.browser.find_element(*ProfilePageLocators.EDIT_NEW_PET_BUTTON_SAVE)
        button_save.click()
