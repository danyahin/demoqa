from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)
        self.full_name_textarea = WebElement(driver, '#userName')
        self.current_address_textarea = WebElement(driver, 'textarea#currentAddress')
        self.submit_btn = WebElement(driver, '#submit')
        self.result_name = WebElement(driver, '#name')
        self.result_current_address = WebElement(driver, 'p#currentAddress')
