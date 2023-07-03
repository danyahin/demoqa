from pages.droppable import Droppable
import time
from selenium.webdriver import ActionChains


def test_drag_drop(browser):
    page = Droppable(browser)
    action_chains = ActionChains(browser)

    page.visit()
    assert not page.drop.check_css('backgroundColor')
    action_chains.drag_and_drop(page.drag.find_element(), page.drop.find_element()).perform()
    time.sleep(1.5)
    assert page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    action_chains.drag_and_drop_by_offset(page.drag.find_element(), -200, 0).perform()
    time.sleep(3)
    assert page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
