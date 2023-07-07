import pytest
from pages.radio_button import RadioButton
from pages.demoqa import DemoQa
import time


@pytest.mark.skip
def test_decor(browser):
    page = DemoQa(browser)

    page.visit()
    assert page.level_5_headers.check_count_elements(6)
    for elem in page.level_5_headers.find_elements():
        assert len(elem.text) > 0


# @pytest.mark.skipif(True, reason='Просто потому что')
def test_radio_btns(browser):
    page = RadioButton(browser)
    if not page.code_status():
        pytest.skip(reason=f"Страница {page.base_url} недоступна")

    page.visit()
    base_result = 'You have selected '
    page.yes_radio_div.click()
    time.sleep(1)
    assert page.radio_btn_result.get_text() == base_result + 'Yes'
    page.impressive_radio_div.click()
    time.sleep(1)
    assert page.radio_btn_result.get_text() == base_result + 'Impressive'
    assert 'disabled' in page.no_radio_div.get_dom_attribute('class')
