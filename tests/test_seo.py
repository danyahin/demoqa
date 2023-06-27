from pages.demoqa import DemoQa


def test_check_title_demo(browser):
    page = DemoQa(browser)

    page.visit()
    assert page.get_title() == 'DEMOQA'
