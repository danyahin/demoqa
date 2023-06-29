from pages.form_page import FormPage


def test_login_form_validate(browser):
    page = FormPage(browser)

    page.visit()
    assert page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert page.user_email.get_dom_attribute('pattern') == "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    page.btn_submit.click_force()
    assert page.form_element.get_dom_attribute('class') == 'was-validated'
