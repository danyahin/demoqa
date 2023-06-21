from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time


def test_go_to_page_elements(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()
    assert demo_page.equal_url()
#     demo_page.click_on_the_btn_elements()
    demo_page.btn_elements.click()
    elem_page = ElementsPage(browser)
    time.sleep(5)
    assert elem_page.equal_url()
