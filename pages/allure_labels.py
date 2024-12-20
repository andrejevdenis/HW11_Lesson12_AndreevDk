import allure
from allure_commons.types import Severity

def dynamic_labels():
    allure.dynamic.tag("Web")
    allure.dynamic.label('owner', 'AndreevDK')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Task: Open")
    allure.dynamic.story("HW10_lesson11")
    allure.dynamic.link("https://demoqa.com/automation-practice-form", name="Source page")

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://demoqa.com/automation-practice-form", name="Source page")
def decorator_labels():
    pass