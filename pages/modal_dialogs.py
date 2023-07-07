from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.icon = WebElement(driver, '#app > header > a')
        self.btns_submenu_alerts = WebElement(driver, 'div > div:nth-child(3) > div > ul.menu-list > li')
        self.small_modal_btn = WebElement(driver, '#showSmallModal')
        self.large_modal_btn = WebElement(driver, '#showLargeModal')
        self.small_modal_window = WebElement(driver, '.modal-sm')
        self.small_close_btn = WebElement(driver, '#closeSmallModal')
        self.large_modal_window = WebElement(driver, '.modal-lg')
        self.large_close_btn = WebElement(driver, '#closeLargeModal')
