from pages.base_page import BasePage
from components.components import WebElement


class RadioButton(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)
        self.yes_radio_div = WebElement(driver, 'label[for = "yesRadio"]')
        self.impressive_radio_div = WebElement(driver, 'div.row > div > div:nth-child(2) > div:nth-child(3)')
        self.no_radio_div = WebElement(driver, 'div.row > div > div:nth-child(2) > div:nth-child(4)')
        self.radio_btn_result = WebElement(driver, 'p.mt-3')  # span.text-success
