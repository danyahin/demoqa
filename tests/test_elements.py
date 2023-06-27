from pages.elements_page import ElementsPage


def test_find_elements(browser):
    page = ElementsPage(browser)

    page.visit()
    assert page.btns_first_menu.check_count_elements(9)
