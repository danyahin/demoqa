from pages.links import Links
import time


def test_window_tab(browser):
    page = Links(browser)

    page.visit()
    assert page.home_link.exist()
    assert page.home_link.get_text() == 'Home'
    assert page.home_link.get_dom_attribute('href') == 'https://demoqa.com'
    assert len(browser.window_handles) == 1
    page.home_link.click()
    assert len(browser.window_handles) == 2
