from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    page = Accordion(browser)
    page.visit()
    assert page.first_textfield.visible()
    page.first_text_line.click()
    time.sleep(2)
    assert not page.first_textfield.visible()


def test_visible_accordion_default(browser):
    page = Accordion(browser)
    page.visit()
    assert not page.second_textfield_p1.visible()
    assert not page.second_textfield_p2.visible()
    assert not page.third_textfield.visible()
