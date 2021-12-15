from appium import webdriver


class houji_config(object):
    @classmethod
    def get_driver(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.bowhead.houji",
            "appActivity": "com.bowhead.houji.MainActivity",
            'platformVersion': '6',
            'noReset': True,
            'fullReset': False,
            'unicodeKeyboard':True,
            'resetKeyboard':True,
            'newCommandTimeout': 600000,
            'newCommandTimeout':200,
            'automationName' : 'UiAutomator2'
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        return driver