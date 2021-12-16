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
        global w_x
        global h_y
        global driver

        driver = houji_config().get_driver()

        w_x = driver.get_window_size()['width']
        h_y = driver.get_window_size()['height']
        print(driver.get_window_size())

        global create_chile_flag 

        create_chile_flag = 1


    def login(self):

        driver.implicitly_wait(500)

        el1 = driver.find_element(By.CLASS_NAME, 'android.widget.EditText')

        driver.implicitly_wait(500)

        el1.click()

        driver.implicitly_wait(500)

        time.sleep(1)

        el1.set_text("15221532245")

        time.sleep(1)

        driver.implicitly_wait(500)

        driver.find_element(By.CLASS_NAME,'android.widget.CheckBox').click()

        driver.implicitly_wait(500)

        driver.find_element(By.CLASS_NAME,'android.widget.Button').click()

        driver.implicitly_wait(500)

        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="输入验证码"]').get_attribute('content-desc'),'输入验证码')

        ve_code = str(input("ve_code:"))

        # a = 57/576
        # b = 417/1024

        a = 155/1080
        b = 10121/1920

        print(a*w_x)
        print(b*h_y)
        driver.tap([(a*w_x, b*h_y)],2)

        for i in ve_code:
            driver.press_keycode(int(i)+7)
            time.sleep(1)

        time.sleep(1)

        el2 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]").get_attribute('content-desc')

        self.assertEqual(el2.replace("\n", ""), str(ve_code))

        driver.implicitly_wait(500)

        driver.find_element(By.ACCESSIBILITY_ID,"确定").click()

    def new_account_enter_create_child(self):
        
        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="Gululu支持多个家庭成员，快点创建第一个家庭成员开始好习惯之旅吧！"]').get_attribute('content-desc'), 'Gululu支持多个家庭成员，快点创建第一个家庭成员开始好习惯之旅吧！')
        driver.find_element(By.ACCESSIBILITY_ID,"添加账号").click()



    def member_view_enter_create_child(self):

        #-------------------------member list------------

        driver.implicitly_wait(500)

        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="欢迎来到"]').get_attribute('content-desc'),'欢迎来到')


        driver.implicitly_wait(500)

        
        for i in range(10):

            TouchAction(driver).press(x=576*100/w_x,y=1024*900/h_y).move_to(x=576*100/w_x,y=1024*500/h_y).wait(30).move_to(x=576*100/w_x,y=50*1024/h_y).release().perform()


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

        global childname

        childname = str(time.time())[6:10]

        el3.set_text(childname)

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

            TouchAction(driver).press(x=204*576/w_x, y=633*1024/h_y).move_to(x=204*576/w_x, y=584*1024/h_y).move_to(x=204*576/w_x, y=274*1024/h_y).wait(30).release().perform()


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
    


    def pair_device(self):

        #-------------------------pairing process------------

        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="开启设备并充电 打开USB充电口将产品连接至电源"]').get_attribute('content-desc'),'开启设备并充电 打开USB充电口将产品连接至电源')

        driver.implicitly_wait(500)

        driver.find_element(By.ACCESSIBILITY_ID,"下一步").click()

        driver.implicitly_wait(500)

        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="连接设备... 请确认设备靠近手机"]').get_attribute('content-desc'),'连接设备... 请确认设备靠近手机')

        driver.find_element(By.ACCESSIBILITY_ID,"下一步").click()

        driver.implicitly_wait(500)

        # driver.find_elements(By.XPATH,'//android.view.View[@content-desc="30:92:F6:4C:15:79 A302-001C -57 dBm"]') #配对001c设备

        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("30:92:F6:4C:15:79 A302-001C -57 dBm"))')

        driver.implicitly_wait(500)

        driver.find_element(By.ACCESSIBILITY_ID,"下一步").click()

        driver.implicitly_wait(500)

        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="配对成功！"]').get_attribute('content-desc'),'配对成功！')

        driver.implicitly_wait(500)

        driver.find_element(By.ACCESSIBILITY_ID,"下一步").click()

        driver.implicitly_wait(500)

        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="开机使用 只要车子进入运动状态，设备就会自动开启工作，收集运动数据"]').get_attribute('content-desc'),'开机使用 只要车子进入运动状态，设备就会自动开启工作，收集运动数据')

        driver.implicitly_wait(500)

        driver.find_element(By.ACCESSIBILITY_ID,"下一步").click()

        driver.implicitly_wait(500)
        pair_xpth = '//android.view.View[@content-desc="同步数据 单击车辆的功能键，让设备处于工作状态，打开手机App并靠近车辆，数据会自动传输"]'
        self.assertEqual(driver.find_element(By.XPATH,pair_xpth).get_attribute('content-desc'),'同步数据 单击车辆的功能键，让设备处于工作状态，打开手机App并靠近车辆，数据会自动传输')

        driver.implicitly_wait(500)

        driver.find_element(By.ACCESSIBILITY_ID,"下一步").click()

        driver.implicitly_wait(500)

        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="开启车头灯 长按设备的功能键3秒以上开启车头灯，再次单击功能键车头灯关闭"]').get_attribute('content-desc'),'开启车头灯 长按设备的功能键3秒以上开启车头灯，再次单击功能键车头灯关闭')

        driver.implicitly_wait(500)

        driver.find_element(By.ACCESSIBILITY_ID,"下一步").click()

        driver.implicitly_wait(500)

        self.assertEqual(driver.find_element(By.XPATH,'//android.view.View[@content-desc="设置成功!"]').get_attribute('content-desc'),'设置成功!')

        driver.implicitly_wait(500)

        driver.find_element(By.ACCESSIBILITY_ID,"开始使用").click()

        driver.implicitly_wait(500)

        self.assertEqual(driver.find_element(By.ID,'caf49539-6fb4-453f-ac30-d4240e435b90').get_attribute('content-desc'),childname)



    def run_tests(self):

        self.login()

        self.member_view_enter_create_child()

        self.create_child()

        driver.implicitly_wait(500)

        global create_chile_flag

        if create_chile_flag == 1:

            driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[0].click()#click "x" enter member view

            driver.implicitly_wait(500)

            create_chile_flag =  create_chile_flag + 1

            TestHouji().member_view_enter_create_child()

            driver.implicitly_wait(500)

            TestHouji().pair_device()

            create_child()

        else:

            driver.find_element(By.ACCESSIBILITY_ID,"添加设备").click() #enter device pairing page

            pair_device()
    

    def test_new_account_pair_device(self):

        self.run_tests()
    


if __name__ == "__main__":

     unittest.main()

