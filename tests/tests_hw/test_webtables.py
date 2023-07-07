from pages.web_tables import WebTables
import time
import logging
from selenium.webdriver.common.keys import Keys


def test_webtables_1(browser):
    page = WebTables(browser)

    page.visit()
    assert page.add_new_record.exist()
    for i in range(1):
        page.add_new_record.click()
        time.sleep(0.3)
        assert page.dialog_add_window.exist()
        page.dialog_submit.click()
        time.sleep(0.3)
        assert page.dialog_add_window.exist()
        page.first_name_input.send_keys('Mamma')
        page.last_name_input.send_keys('Mia')
        page.user_email_input.send_keys('Pepperony@pizza.it')
        page.user_age_input.send_keys('10')
        page.user_salary_input.send_keys('300')
        page.user_department_input.send_keys('Deep Dark department')
        page.dialog_submit.click()
    assert not page.dialog_add_window.exist()
    assert page.row_4_delete_btn.exist()
    page.edit_4.click()
    assert page.dialog_add_window.exist()
    assert page.first_name_input.get_dom_attribute('value') == 'Mamma'
    assert page.last_name_input.get_dom_attribute('value') == 'Mia'
    assert page.user_email_input.get_dom_attribute('value') == 'Pepperony@pizza.it'
    assert page.user_age_input.get_dom_attribute('value') == '10'
    assert page.user_salary_input.get_dom_attribute('value') == '300'
    assert page.user_department_input.get_dom_attribute('value') == 'Deep Dark department'
    page.first_name_input.clear()
    page.first_name_input.send_keys('Mamm')
    page.dialog_submit.click()
    assert page.row_4_first_name_value.get_text() == 'Mamm'
    while page.row_4_delete_btn.exist():
        delete_4 = page.rows_delete_btns.find_elements()
        delete_4[3].click()
        time.sleep(1)
        try:
            assert not page.row_4_delete_btn.exist()
        except Exception as ex:
            logging.log(1, ex)
            break
    assert not page.row_4_delete_btn.exist()
    time.sleep(3)


def test_webtables_2(browser):
    page = WebTables(browser)
    page.visit()
    page.count_of_rows_selector.click_force()
    page.count_of_rows_selector.send_keys(Keys.UP)
    page.count_of_rows_selector.send_keys(Keys.ENTER)

    assert page.equal_url()
    assert page.count_of_all_rows.check_count_elements(5)

    assert page.btn_previous.get_dom_attribute('disabled')
    assert page.btn_next.get_dom_attribute('disabled')
    for i in range(3):
        page.add_new_record.click()
        time.sleep(0.3)
        page.first_name_input.send_keys('Mamma')
        page.last_name_input.send_keys('Mia')
        page.user_email_input.send_keys('Pepperony@pizza.it')
        page.user_age_input.send_keys('10')
        page.user_salary_input.send_keys('300')
        page.user_department_input.send_keys('Deep Dark department')
        page.dialog_submit.click()
        time.sleep(0.3)

    assert page.page_of_count.get_text() == '2'
    assert not page.btn_next.get_dom_attribute('disabled')
    page.btn_next.click()
    assert page.page_number_input.get_dom_attribute('value') == '2'
    page.btn_previous.click()
    assert page.page_number_input.get_dom_attribute('value') == '1'
