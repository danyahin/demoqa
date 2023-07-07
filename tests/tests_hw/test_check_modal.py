from pages.modal_dialogs import ModalDialogs
import time
import pytest


def test_check_modal(browser):
    page = ModalDialogs(browser)
    if not page.code_status():
        pytest.skip(reason=f"Страница {page.base_url} недоступна")
    page.visit()
    assert page.small_modal_btn.exist()
    assert page.large_modal_btn.exist()
    assert page.small_modal_btn.get_text() == 'Small modal'
    assert page.large_modal_btn.get_text() == 'Large modal'
    page.small_modal_btn.click()
    time.sleep(0.3)
    assert page.small_modal_window.exist()
    page.small_close_btn.click()
    time.sleep(0.3)
    assert not page.small_modal_window.exist()
    page.large_modal_btn.click()
    time.sleep(0.3)
    assert page.large_modal_window.exist()
    page.large_close_btn.click()
    time.sleep(0.3)
    assert not page.large_modal_window.exist()
