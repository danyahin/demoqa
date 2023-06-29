from pages.text_box import TextBox


def test_placeholder(browser):
    page = TextBox(browser)

    page.visit()
    assert page.full_name_textarea.get_dom_attribute('placeholder') == 'Full Name'
