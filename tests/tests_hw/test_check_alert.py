from pages.alerts import Alerts
import time


def test_check_alert(browser):
    page = Alerts(browser)

    page.visit()
    assert page.five_seconds_waiting_alert.exist()
    page.five_seconds_waiting_alert.click()
    time.sleep(4.9)
    assert not page.alert()
    time.sleep(0.1)
    assert page.alert()
