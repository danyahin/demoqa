from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_text_1(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()
    assert demo_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_text_2(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()
    demo_page.btn_elements.click()
    elem_page = ElementsPage(browser)
    assert elem_page.middle_field.get_text() == 'Please select an item from left to start practice.'

