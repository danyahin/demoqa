from pages.elements_page import ElementsPage
import time


def test_visible_btn_sidebar(browser):
    elem_page = ElementsPage(browser)

    elem_page.visit()
#     elem_page.btn_sidebar_elements.click()
#     time.sleep(3)
#     assert elem_page.btn_sidebar_first_textbox.exist()
    assert elem_page.btn_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    elem_page = ElementsPage(browser)

    elem_page.visit()
    assert elem_page.btn_sidebar_first_checkbox.visible()
    elem_page.btn_sidebar_elements.click()
    time.sleep(2)
    assert not elem_page.btn_sidebar_first_checkbox.visible()
