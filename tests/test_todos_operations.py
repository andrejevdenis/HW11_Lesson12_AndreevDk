from pages.resources import RegistrationPage
from pages.assert_res import Assert_results
from data.users import test_user


def test_complete_todo(browser_management):
    registration_page = RegistrationPage()
    asert_results = Assert_results()
    # Шаги выполнения
    registration_page.register(test_user)
    # Проверки
    asert_results.in_submit_form(test_user)