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


def test_page_elements(browser):
    demo_elements = ElementsPage(browser)

    demo_elements.visit()
    assert demo_elements.main_header.get_text() == 'Elements'
    assert demo_elements.icon.exist()
    assert demo_elements.btn_sidebar_elements.exist()
    assert demo_elements.btn_sidebar_first_textbox.exist()
