from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    BUTTON_PROFILE = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span.p-menuitem-text')
    LOGO_PETS = (By.CSS_SELECTOR, '#app > header > div > div > img')
    BUTTON_QUIT = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a')
    DROPDOWN_BY_PETS = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div/div')
    DROPDOWN_BY_DOG = (By.XPATH, '/html/body/div[3]/div/ul/li[1]')
    DROPDOWN_BY_CAT = (By.XPATH, '/html/body/div[3]/div/ul/li[2]')
    DROPDOWN_BY_REPTILE = (By.XPATH, '/html/body/div[3]/div/ul/li[3]')
    DROPDOWN_BY_HAMSTER = (By.XPATH, '/html/body/div[3]/div/ul/li[4]')
    DROPDOWN_BY_PARROT = (By.XPATH, '/html/body/div[3]/div/ul/li[5]')
    SEARCH_INPUT_NAME = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/div/div[2]/input')
    LIKE_PET = (By.CSS_SELECTOR, '#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > div.p-dataview-content > div > div:nth-child(4) > div > div.product-grid-item-bottom.grid.flex-row.mt-3 > div.col.flex.align-content-end.justify-content-end')
    BUTTON_DETAILS = (By.CSS_SELECTOR, '#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > div.p-dataview-content > div > div:nth-child(4) > div > div.product-grid-item-bottom.grid.flex-row.mt-3 > div:nth-child(1) > button')
    INPUT_COMMENT = (By.CSS_SELECTOR, '#app > main > div.flex.xl\\:w-8.w-full.m-auto.mt-5.flex-wrap > div > div > div.p-card-content > form > div > div > div.p-editor-content.ql-container.ql-snow > div.ql-editor.ql-blank')
    BUTTON_SAVE_COMMENT = (By.CSS_SELECTOR, '#app > main > div.flex.xl\\:w-8.w-full.m-auto.mt-5.flex-wrap > div > div > div.p-card-content > form > div > button')
    ICON_PAGE_FORWARD = (By.CSS_SELECTOR, '#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > div.p-paginator.p-component.p-paginator-bottom > button.p-paginator-next.p-paginator-element.p-link')
    ICON_PAGE_FORWARD_END = (By.CSS_SELECTOR, '#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > div.p-paginator.p-component.p-paginator-bottom > button.p-paginator-last.p-paginator-element.p-link')
    ICON_PAGE_BACK = (By.CSS_SELECTOR, '#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > div.p-paginator.p-component.p-paginator-bottom > button.p-paginator-prev.p-paginator-element.p-link')
    ICON_PAGE_BACK_TO_START = (By.CSS_SELECTOR, '#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > div.p-paginator.p-component.p-paginator-bottom > button.p-paginator-first.p-paginator-element.p-link')



class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASS = (By.CSS_SELECTOR, '#password > input')
    LOGIN_BUTTON = (By.CLASS_NAME, 'p-button-label')



class ProfilePageLocators:
    BUTTON_ADD = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > button')
    INPUT_NAME = (By.XPATH, '//*[@id="name"]')
    DROPDOWN_TYPE_PET = (By.ID, 'typeSelector')
    DROPDOWN_TYPE_DOG = (By.CLASS_NAME, 'p-dropdown-item')
    DROPDOWN_TYPE_CAT = (By.XPATH, '/html/body/div[3]/div/ul/li[2]')
    DROPDOWN_TYPE_REPTILE = (By.XPATH, '/html/body/div[3]/div/ul/li[3]')
    DROPDOWN_TYPE_HAMSTER = (By.XPATH, '/html/body/div[3]/div/ul/li[4]')
    INPUT_AGE = (By.CSS_SELECTOR, '#age > input')
    DROPDOWN_GENDER = (By.ID, 'genderSelector')
    DROPDOWN_GENDER_MALE = (By.XPATH, '/html/body/div[3]/div/ul/li[1]')
    DROPDOWN_GENDER_FEMALE = (By.XPATH, '/html/body/div[3]/div/ul/li[2]')
    BUTTON_CANCEL = (By.CLASS_NAME, 'p-button-label')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '#app > main > div > div > form > div > div.p-card-body > div.p-card-footer > button.p-button.p-component.p-button-success')
    BUTTON_EDIT = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(4) > div > div.product-list-action > button:nth-child(1)')
    BUTTON_PROFILE = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a')
    BUTTON_DELETE_PET_GOLEM = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(4) > div > div.product-list-action > button.p-button.p-component.p-button-danger')
    BUTTON_DELETE_PET_GOLEM_YES = (By.CSS_SELECTOR, 'body > div.p-confirm-popup.p-component.p-ripple-disabled.p-confirm-popup-flipped > div.p-confirm-popup-footer > button.p-button.p-component.p-confirm-popup-accept.p-button-sm')
    BUTTON_EDIT_PET = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(4) > div > div.product-list-action > button:nth-child(1)')
    EDIT_INPUT_NAME_NEW_PET_GOLEM = (By.CSS_SELECTOR, '#name')
    DROPDOWN_EDIT_TYPE_NEW_PET_GOLEM = (By.XPATH, '/html/body/div[1]/main/div/form/div/div[2]/div[2]/div[2]/div[2]/div/div')
    DROPDOWN_NEW_TYPE_PET_GOLEM = (By.XPATH, '/html/body/div[3]/div/ul/li[3]')
    EDIT_NEW_PET_BUTTON_ADD_AVATAR = (By.CSS_SELECTOR, '#app > main > div > form > div > div.p-card-body > div.p-card-content > div.grid.m-auto.justify-content-center.mb-5 > div.w-full.justify-content-center.flex.mt-2 > div > div.col-12.justify-content-center.flex > div > span > input[type=file]')
    ADD_AVATAR_CLICK = (By.CSS_SELECTOR, '#app > main > div > form > div > div.p-card-body > div.p-card-content > div.grid.m-auto.justify-content-center.mb-5 > div.w-full.justify-content-center.flex.mt-2 > div > div.col-12.justify-content-center.flex > div > span')
    EDIT_NEW_PET_BUTTON_SAVE = (By.CSS_SELECTOR, '#app > main > div > form > div > div.p-card-body > div.p-card-footer > button')

