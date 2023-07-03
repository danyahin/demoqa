from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.no_rows_found_msg = WebElement(driver, 'div.rt-noData')
        self.rows_delete_btns = WebElement(driver, '[title="Delete"]')
