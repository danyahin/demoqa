from pages.text_box import TextBox
import time


def test_clear(browser):
    page = TextBox(browser)

    page.visit()
    page.full_name_textarea.send_keys('Ivanov Ivan')
    time.sleep(1)
    page.full_name_textarea.clear()
    time.sleep(2)
    a = page.full_name_textarea.get_text()
    assert page.full_name_textarea.get_text() == ''
