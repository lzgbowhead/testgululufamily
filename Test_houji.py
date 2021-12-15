# -*- coding: utf-8 -*-
from unittest.suite import TestSuite
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.webdriver.common.touch_action import TouchAction
import time
import unittest
from selenium.webdriver.common.by import By
import warnings
from houji_conf import houji_config

class TestHouji(unittest.TestCase):
    def setUp(self):
        global driver
        driver = get_driver()
        global create_chile_flag 
        create_chile_flag = 1

    def login(self):
        time.sleep(1)
        el1 = driver.find_element(By.CLASS_NAME, 'android.widget.EditText')
        driver.implicitly_wait(500)
        el1.click()
        driver.implicitly_wait(500)
        el1.send_keys("15221532245")
        driver.implicitly_wait(500)
        driver.find_element(By.CLASS_NAME,'android.widget.CheckBox').click()
        driver.implicitly_wait(500)
        driver.find_element(By.CLASS_NAME,'android.widget.Button').click()
        driver.implicitly_wait(500)
        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="输入验证码"]').get_attribute('content-desc'),'输入验证码')
        # el2 = driver.find_element(By.CLASS_NAME,'android.view.View')
        # el2.click()
        # el2.send_keys()


    def member_view_enter_create_child(self):
        #-------------------------member list------------
        driver.implicitly_wait(500)
        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="欢迎来到"]').get_attribute('content-desc'),'欢迎来到')

        driver.implicitly_wait(500)

        for i in range(10):
            TouchAction(driver).press(x=100,y=900).move_to(x=100,y=500).wait(30).move_to(x=100,y=50).release().perform()
        
        driver.implicitly_wait(500)

        driver.find_element(By.ACCESSIBILITY_ID,"添加账号").click()


    def create_child(self):
        warnings.simplefilter("ignore", ResourceWarning)
        #-------------------------creata nickname------------
        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="设置昵称"]').get_attribute('content-desc'),'设置昵称')
        el3 = driver.find_element(By.CLASS_NAME,"android.widget.EditText")
        el3.click()
        driver.implicitly_wait(500)
        el3.clear()
        time.sleep(1)
        el3.set_text(str(time.time())[6:10])
        driver.implicitly_wait(10000)
        driver.find_element(By.CLASS_NAME,"android.widget.Button").click()
        driver.implicitly_wait(500)

        #-------------------------choose gender------------
        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="您的性别是？"]').get_attribute('content-desc'),'您的性别是？')

        driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[2].click() #1为男孩，2为女孩

        driver.find_element(By.ACCESSIBILITY_ID,"下一步").click()
        driver.implicitly_wait(500)

        #-------------------------select date of birth------------
        time.sleep(1)
        for i in range(3):
            TouchAction(driver).press(x=204, y=633).move_to(x=204, y=584).move_to(x=204, y=274).wait(30).release().perform()

        driver.implicitly_wait(500)
        driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[8].click()
        driver.implicitly_wait(500)
        driver.find_element(By.ACCESSIBILITY_ID,"下一步").click()
        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="您的出生年月"]').get_attribute('content-desc'),'您的出生年月')
        TouchAction(driver).press(x=150, y=633).move_to(x=150, y=584).move_to(x=150, y=274).wait(30).release().perform()
        TouchAction(driver).press(x=425, y=633).move_to(x=425, y=584).move_to(x=425, y=274).wait(30).release().perform()
        driver.find_element(By.ACCESSIBILITY_ID,"下一步").click()
        #-------------------------member created successfully------------
        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="太棒啦!"]').get_attribute('content-desc'),'太棒啦!')
        driver.implicitly_wait(500)
        global create_chile_flag

        if create_chile_flag == 1:
            driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[0].click()#click "x" enter member view
            driver.implicitly_wait(500)
            create_chile_flag =  create_chile_flag + 1
            TestHouji().test_member_view_enter_create_child()
            driver.implicitly_wait(500)
            TestHouji().test_create_child()
        else:
            driver.find_element(By.ACCESSIBILITY_ID,"添加设备").click() #enter device pairing page
    

    def pair_device(self):
        pass


        
        



# if __name__ == "__main__":
#     #  unittest.main()
#      suite = unittest.TestSuite()
#      suite.addTest(TestHouji('test_member_view_enter_create_child'))
#      suite.addTest(TestHouji('test_create_child'))
#      runner = unittest.TextTestRunner()
#      runner.run(suite)

    def run_tests(self):
        # self.login()
        self.member_view_enter_create_child()
        self.create_child()
    
    def test_houji(self):
        run_tests()

