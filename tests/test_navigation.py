from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    page_home = DemoQa(browser)
    page_elem = ElementsPage(browser)

    page_home.visit()
    page_home.btn_elements.click()
    page_elem.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert page_elem.equal_url()
