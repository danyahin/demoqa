from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    page = ModalDialogs(browser)

    page.visit()
    assert page.btns_submenu_alerts.check_count_elements(5)


def test_navigation_modal(browser):
    page = ModalDialogs(browser)
    home = DemoQa(browser)

    page.visit()
    page.refresh()
    page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    page.forward()
    home.equal_url()
    assert home.get_title() == 'DEMOQA'
    browser.set_window_size(1000, 1000)

