from pages.alerts import Alerts
import time


def test_alerts(browser):
    page = Alerts(browser)

    page.visit()
    assert not page.alert()
    page.alert_btn.click()
    time.sleep(2)
    assert page.alert()
    page.alert().accept()


def test_alert_text(browser):
    page = Alerts(browser)

    page.visit()
    page.alert_btn.click()
    time.sleep(2)
    assert page.alert().text == 'You clicked a button'
    page.alert().accept()
    assert not page.alert()


def test_confirm(browser):
    page = Alerts(browser)

    page.visit()
    page.confirm_btn.click()
    time.sleep(2)
    page.alert().dismiss()
    assert page.confirm_result.get_text() == 'You selected Cancel'


def test_prompt(browser):
    page = Alerts(browser)

    page.visit()
    page.prompt_btn.click()
    time.sleep(2)
    x = 'many people'
    page.alert().send_keys(x)
    page.alert().accept()
    assert page.prompt_result.get_text() == 'You entered ' + x
