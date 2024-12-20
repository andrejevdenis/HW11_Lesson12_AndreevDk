import os.path

from selene import browser, have, be

from selenium.webdriver import Keys
import allure
from pages.allure_labels import dynamic_labels

class RegistrationPage:

    @allure.step("Fill registration form valid data")
    def register(self, value):
       dynamic_labels()
       browser.config.timeout = 12
       with allure.step("Open brwser"):
           browser.open('https://demoqa.com/automation-practice-form')
           browser.driver.fullscreen_window()
       with allure.step("Fill FirstName"):
           browser.element('[id="firstName"]').type(value.first_name)
       with allure.step("Fill LastName"):
           browser.element('[id="lastName"]').type(value.last_name)
       with allure.step("Email"):
           browser.element('[id="userEmail"]').type(value.email)
       with allure.step("Check Gender"):
           if value.gender == 'Male':
                browser.element('[for="gender-radio-1"]').click()
           elif value.gender == 'Female':
                browser.element('[for="gender-radio-2"]').click()
           else:
                browser.element('[for="gender-radio-3"]').click()
       with allure.step("Fill Mobile number"):
           browser.element('[id="userNumber"]').type(value.mobile_num).press_tab()
       with allure.step("Fill Date of Birth"):
           browser.element('[class="react-datepicker__month-select"]').element(f'[value="{value.date_of_birth.get('month_num')}"').click()
           browser.element('[class="react-datepicker__year-select"]').element(f'[value="{value.date_of_birth.get('year')}"]').click()
           browser.element(f'[class="react-datepicker__day react-datepicker__day--0{value.date_of_birth.get('day')}"]').click()
       with allure.step("Fill Subject"):
           browser.element('[id="subjectsInput"]').type(value.subject)
           browser.element('[id="react-select-2-option-0"]').click()
           browser.element('[id="subjectsInput"]').type(value.subject1)
           browser.element('[id="react-select-2-option-0"]').click()
       with allure.step("Check Hobbies"):
           if value.hobbies.get('Sports') == 'y':
               browser.element('[for="hobbies-checkbox-1"]').click()
           if value.hobbies.get('Reading') == 'y':
               browser.element('[for="hobbies-checkbox-2"]').click()
           if value.hobbies.get('Music') == 'y':
               browser.element('[for="hobbies-checkbox-3"]').click()
       with allure.step("Upload picture"):
           browser.element('[id="uploadPicture"]').set_value(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), f'resources/{value.file}')))
       with allure.step("Fill Adress"):
            browser.element('[id="currentAddress"]').type(value.adress).press_tab().press(Keys.PAGE_DOWN)
       with allure.step("Choose State"):
           browser.element('[id="state"]').click()
           if value.state == 'NCR':
               browser.element('[id="react-select-3-option-0"]').click()
           elif value.state == 'Uttar Pradesh':
               browser.element('[id="react-select-3-option-1"]').click()
           elif value.state == 'Haryana':
               browser.element('[id="react-select-3-option-2"]').click()
           elif value.state == 'Rajasthan':
               browser.element('[id="react-select-3-option-3"]').click()
       with allure.step("Choose City"):
           browser.element('[id="city"]').click()
           if value.city in ['Delhi', 'Agra', 'Karnal', 'Jaipur']:
               browser.element('[id="react-select-4-option-0"]').click()
           elif value.city in ['Gurgaon', 'Lucknow', 'Panipat', 'Jaiselmer']:
               browser.element('[id="react-select-4-option-1"]').click()
           elif value.city in ['Noida', 'Merrut']:
               browser.element('[id="react-select-4-option-2"]').click()
       with allure.step("Push Submit button"):
            browser.element('[id="submit"]').click()
