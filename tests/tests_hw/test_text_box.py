from pages.text_box import TextBox


def test_text_box(browser):
    page = TextBox(browser)

    page.visit()
    a = 'Name Fullname'
    b = 'Current Address'
    page.full_name_textarea.send_keys(a)
    page.current_address_textarea.send_keys(b)
    page.submit_btn.click()
    assert ('Name:' + a) == page.result_name.get_text()
    assert ('Current Address :' + b) == page.result_current_address.get_text()
