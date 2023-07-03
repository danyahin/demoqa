from pages.web_tables import WebTables


def test_webtables(browser):
    page = WebTables(browser)

    page.visit()
    assert not page.no_rows_found_msg.exist()
    # while page.rows_delete_btns.exist():
    #     page.rows_delete_btns.click()
    for i in range(len(page.rows_delete_btns.find_elements())):
        if not page.rows_delete_btns.exist():
            break
        page.rows_delete_btns.click()

    # for elem in page.rows_delete_btns.find_elements():
    #     elem.click()
#         browser.execute_script("arguments[0].click();", elem)
    assert page.no_rows_found_msg.exist()

