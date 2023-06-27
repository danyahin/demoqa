from pages.form_page import FormPage
import time


def test_login_form(browser):
    page = FormPage(browser)
    page.visit()
    assert not page.modal_dialog.exist()
    time.sleep(2)
    page.first_name.send_keys('Tester')
    page.last_name.send_keys('Testosteronovich')
    page.user_email.send_keys('lublu@fgds.com')
    page.gender_radio_1.click()
    page.user_number.send_keys('8005553535')
    time.sleep(3)
    page.btn_submit.click()
    time.sleep(2)
    assert page.modal_dialog.exist()
    page.btn_close_modal.click()
    assert not page.modal_dialog.exist()
