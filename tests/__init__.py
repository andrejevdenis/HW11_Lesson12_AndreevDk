# # import json
# import os
# #
# # import allure
# # from allure import attachment_type
# from selene import browser
# #
# #
# # def attachments():
# browser.open('https://mail.yandex.ru/?uid=50719411#message/188306759419454615')
# browser.driver.fullscreen_window()
# # browser.driver.save_screenshot(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'temp/My2.png')))
# # browser.driver.save_screenshot(f'{file}/My2.png')
# #     allure.attach(browser.driver.page_source.__doc__, name="Html", attachment_type=attachment_type.HTML)
# #     allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)
# #     allure.attach(browser.driver.save_screenshot(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)),".temp/My.png"))), name="ScreenShot", attachment_type=attachment_type.PNG))
# #     # allure.attach(browser.driver.page_source, name="Html", attachment_type=attachment_type.HTML)
#
# print(browser.driver.get_log('browser'))
#
