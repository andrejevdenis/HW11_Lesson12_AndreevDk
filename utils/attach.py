import os

import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):

    browser.driver.save_screenshot(
        os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'temp/image.png')))
    allure.attach.file(
        f"{os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'temp/image.png'))}",
        name="ScreenShot", attachment_type=AttachmentType.PNG)

def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    allure.attach(browser.driver.page_source, name="Html", attachment_type=AttachmentType.HTML)


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')