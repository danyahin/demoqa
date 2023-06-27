from pages.demoqa import DemoQa
import time


def test_window_size(browser):
    page = DemoQa(browser)

    page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(3)
    browser.set_window_size(1000, 1000)
