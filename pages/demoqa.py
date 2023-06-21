from pages.base_page import BasePage
from components.components import WebElement


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)
        self.icon = WebElement(self.driver, '#app > header > a')
        self.btn_elements = WebElement(self.driver, 'div.category-cards > div:nth-child(1)')
        self.footer = WebElement(self.driver, '#app > footer > span')

    # def clicl_on_the_icon(self):
    #     self.find_element('#app > header > a').click()

    # def click_on_the_btn_elements(self):
    #     self.find_element('#app > div > div > div.home-body > div > div:nth-child(1)').click()
