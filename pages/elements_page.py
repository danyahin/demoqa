from pages.base_page import BasePage
from components.components import WebElement


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
        self.icon = WebElement(self.driver, '#app > header > a')
        self.middle_field = WebElement(self.driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')
        self.main_header = WebElement(self.driver, 'div.main-header')
        self.btn_sidebar_elements = WebElement(self.driver, 'div > div:nth-child(1) > span > div > div.header-text')
        self.btn_sidebar_first_textbox = WebElement(self.driver, 'div:nth-child(1) > div > ul > #item-0 > span')
        self.btn_sidebar_first_checkbox = WebElement(self.driver, 'div:nth-child(1) > div > ul > #item-1 > span')
