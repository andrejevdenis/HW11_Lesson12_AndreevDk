from selene import browser, have, be
import allure

from utils import attach


class Assert_results:

   @allure.step("Assert filled data with expected")
   def in_submit_form(self, value):
        browser.config.timeout = 12
        with allure.step("Assert header name"):
            browser.element('[class="modal-header"]').should(have.text('Thanks for submitting the form'))
        with allure.step("Assert FirstName LastName"):
            browser.element('[class="table-responsive"]').should(have.text(f'{value.first_name} {value.last_name}'))
        with allure.step("Assert Email"):
            browser.element('[class="table-responsive"]').should(have.text(value.email))
        with allure.step("Assert Gender"):
            browser.element('[class="table-responsive"]').should(have.text(value.gender))
        with allure.step("Assert Mobile number"):
            browser.element('[class="table-responsive"]').should(have.text(value.mobile_num))
        with allure.step("Assert Date of Birth"):
            browser.element('[class="table-responsive"]').should(have.text(f'{value.date_of_birth.get('day')} {value.date_of_birth.get('month')},{value.date_of_birth.get('year')}'))
        with allure.step("Assert Subject"):
            browser.element('[class="table-responsive"]').should(have.text(f'{value.subject}, {value.subject1}'))
        with allure.step("Assert Hobbies"):
            if value.hobbies.get('Sports') == 'y':
                browser.element('[class="table-responsive"]').should(have.text('Sports'))
            if value.hobbies.get('Reading') == 'y':
                browser.element('[class="table-responsive"]').should(have.text('Reading'))
            if value.hobbies.get('Music') == 'y':
                browser.element('[class="table-responsive"]').should(have.text('Music'))
        with allure.step("Assert Uploaded file"):
            browser.element('[class="table-responsive"]').should(have.text(value.file))
        with allure.step("Assert Adress"):
            browser.element('[class="table-responsive"]').should(have.text(value.adress))
        with allure.step("Assert State and city"):
            browser.element('[class="table-responsive"]').should(have.text(f'{value.state} {value.city}'))
