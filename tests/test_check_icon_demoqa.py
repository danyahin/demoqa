from pages.demoqa import DemoQa


def test_icon_exist(browser):
    # browser.get('https://demoqa.com/')
    # icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    #
    # if icon is None:
    #     print('Элемент не найден')
    # else:
    #     print('Элемент найден')
    demo_page = DemoQa(browser)
    demo_page.visit()
#     demo_page.clicl_on_the_icon()
    demo_page.icon.click()
    assert demo_page.equal_url()
    assert demo_page.icon.exist()
