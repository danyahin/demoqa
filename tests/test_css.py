from pages.text_box import TextBox


def test_text_box_submit(browser):
    page = TextBox(browser)

    page.visit()
    assert page.submit_btn.check_css('color', 'rgba(255, 255, 255, 1)')
    assert page.submit_btn.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert page.submit_btn.check_css('borderColor', 'rgb(0, 123, 255)')
