from pages.base_page import BasePage
from components.components import WebElement


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.form_element = WebElement(driver, '#userForm')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)')
        self.user_number = WebElement(driver, '#userNumber')
        self.hobbies_music = WebElement(driver, '#hobbiesWrapper > div > div:nth-child(3)')
        self.current_address_textarea = WebElement(driver, '#currentAddress')
        self.select_state = WebElement(driver, '#state > div')
        self.select_state_textarea = WebElement(driver, '#react-select-3-input')
        self.select_city_textarea = WebElement(driver, '#react-select-4-input')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
#         self.fantom_locator = WebElement(driver, '#state > div[class=" css-2613qy-menu"]')
        self.fantom_locator = WebElement(driver, '#state > div:nth-child(3)')
        self.fantom_locator_2 = WebElement(driver, '//div[@id="state"]/div[@class=" css-2613qy-menu"]', 'xpath')
        self.btn_NCR = WebElement(driver, "//*[contains(text(), 'NCR')]", 'xpath')
