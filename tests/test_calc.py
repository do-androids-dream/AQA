import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import os


class CalculatorTests(unittest.TestCase):

    def setUp(self):
        device = os.environ.get('DEVICE')
        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": device,
            "appPackage": "com.google.android.apps.nexuslauncher",
            "appActivity": ".Calculator",
            "language": "en",
            "locale": "US",
            "noReset": True
        }
        appium_server_url = 'http://localhost:4723'
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        reset_result = '//android.widget.ImageButton[@content-desc="clear"]'
        self.driver.find_element(by=AppiumBy.XPATH, value=reset_result).click()

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_positive_addition(self):
        test_elements = [
            '//android.widget.ImageButton[@content-desc="5"]',
            '//android.widget.ImageButton[@content-desc="plus"]',
            '//android.widget.ImageButton[@content-desc="3"]'
        ]
        result_preview = '//android.widget.TextView[@resource-id="com.google.android.calculator:id/result_preview"]'
        expected = "8"

        for element in test_elements:
            self.driver.find_element(by=AppiumBy.XPATH, value=element).click()

        result = self.driver.find_element(by=AppiumBy.XPATH, value = result_preview).text
        self.assertEqual(result, expected)

    def test_positive_subtraction(self):
        test_elements = [
            '//android.widget.ImageButton[@content-desc="1"]',
            '//android.widget.ImageButton[@content-desc="0"]',
            '//android.widget.ImageButton[@content-desc="minus"]',
            '//android.widget.ImageButton[@content-desc="5"]'
        ]
        result_preview = '//android.widget.TextView[@resource-id="com.google.android.calculator:id/result_preview"]'
        expected = "5"

        for element in test_elements:
            self.driver.find_element(by=AppiumBy.XPATH, value=element).click()
        result = self.driver.find_element(by=AppiumBy.XPATH, value = result_preview).text
        self.assertEqual(result, expected)

    def test_negative_zerodivision(self):
        test_elements = [
            '//android.widget.ImageButton[@content-desc="3"]',
            '//android.widget.ImageButton[@content-desc="divide"]',
            '//android.widget.ImageButton[@content-desc="0"]',
            '//android.widget.ImageButton[@content-desc="equals"]'
        ]
        result_preview = '//android.widget.TextView[@resource-id="com.google.android.calculator:id/result_preview"]'
        expected = "Can't divide by 0"

        for element in test_elements:
            self.driver.find_element(by=AppiumBy.XPATH, value=element).click()

        result = self.driver.find_element(by=AppiumBy.XPATH, value=result_preview).text
        self.assertEqual(result, expected)

    def test_negative_tolarge(self):
        element = '//android.widget.ImageButton[@content-desc="9"]'
        operation = [
            '//android.widget.ImageButton[@content-desc="power"]',
            '//android.widget.ImageButton[@content-desc="equals"]'
            ]
        result_preview = '//android.widget.TextView[@resource-id="com.google.android.calculator:id/result_preview"]'
        expected = "Value too large"

        for i in range(2):
            for _ in range(6):
                self.driver.find_element(by=AppiumBy.XPATH, value=element).click()
            self.driver.find_element(by=AppiumBy.XPATH, value=operation[i]).click()

        result = self.driver.find_element(by=AppiumBy.XPATH, value=result_preview).text
        self.assertEqual(result, expected)


if __name__ == "main":
    unittest.main()
