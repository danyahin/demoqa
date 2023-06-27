from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.first_textfield = WebElement(driver, '#section1Content > p')
        self.first_text_line = WebElement(driver, '#section1Heading')  # "What is Lorem Ipsum?" Line
        self.second_textfield_p1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.second_textfield_p2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.third_textfield = WebElement(driver, '#section3Content > p')
