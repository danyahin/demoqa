from pages.herokuapp_homepage import HerokuappHomepage
from pages.heroku_add_remove import HerokuAddRemove
import time


def test_btn_add(browser):
    herokuapp_homeapge = HerokuappHomepage(browser)
    heroku_add_remove = HerokuAddRemove(browser)

    herokuapp_homeapge.visit()
    assert herokuapp_homeapge.add_remove_elements_btn.exist()
    herokuapp_homeapge.add_remove_elements_btn.click()
    time.sleep(2)
    assert heroku_add_remove.equal_url()
    assert heroku_add_remove.add_element_btn.exist()
    assert heroku_add_remove.add_element_btn.get_text() == 'Add Element'
    assert heroku_add_remove.add_element_btn.get_dom_attribute('onclick') == 'addElement()'
    btn_clicks = 4
    for i in range(btn_clicks):
        heroku_add_remove.add_element_btn.click()

    assert heroku_add_remove.added_delete_btns.check_count_elements(btn_clicks)

    for elem in heroku_add_remove.added_delete_btns.find_elements():
        assert elem.text == 'Delete'

    for index, elem in enumerate(heroku_add_remove.added_delete_btns.find_elements()):
        if index == btn_clicks:
            break
        elem.click()
        time.sleep(0.3)

    while heroku_add_remove.added_delete_btns.find_elements():
        assert False
    assert not heroku_add_remove.added_delete_btns.exist()
    time.sleep(2)
