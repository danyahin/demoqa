from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.add_new_record = WebElement(driver, '#addNewRecordButton')
        self.no_rows_found_msg = WebElement(driver, 'div.rt-noData')
        self.rows_delete_btns = WebElement(driver, '[title="Delete"]')
        self.dialog_add_window = WebElement(driver, 'div.modal-content')
        self.dialog_submit = WebElement(driver, '#submit')
        self.btn_previous = WebElement(driver, '.-previous > button')
        self.btn_next = WebElement(driver, '.-next> button')

        self.first_name_input = WebElement(driver, '#firstName')
        self.last_name_input = WebElement(driver, '#lastName')
        self.user_email_input = WebElement(driver, '#userEmail')
        self.user_age_input = WebElement(driver, '#age')
        self.user_salary_input = WebElement(driver, '#salary')  # зарплата
        self.user_department_input = WebElement(driver, '#department')

        self.row_4 = WebElement(driver, 'div.rt-tbody > div:nth-child(4)')
        self.edit_4 = WebElement(driver, '#edit-record-4')
        self.row_4_first_name_value = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.row_4_delete_btn = WebElement(driver, '#delete-record-4')

        self.count_of_rows_selector = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.count_of_all_rows = WebElement(driver, 'div.rt-table > div.rt-tbody > div')
        self.page_of_count = WebElement(driver, '.-totalPages')
        self.page_number_input = WebElement(driver, 'div.-pageJump > input')
