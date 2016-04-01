import random
import string
from unittest import TestCase

# Create your tests here.
from selenium import webdriver


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        self.browser.get('http://localhost:8000/#/login')

        name = self.browser.find_element_by_id('username')
        name.send_keys('alejo2')

        name = self.browser.find_element_by_id('password')
        name.send_keys('alejandro')

        self.browser.find_element_by_id('id_login').click()
        self.browser.implicitly_wait(5)

        self.assertEquals('http://localhost:8000/#/login',self.browser.current_url,'login mal')

    def test_detalle(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_id('id_detalle5').click()
        self.browser.implicitly_wait(3)
        self.assertEquals('http://localhost:8000/#/detail/5',self.browser.current_url,'url mal')

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_register(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()
        self.browser.implicitly_wait(3)
        name = self.browser.find_element_by_id('id_name')
        name.send_keys('ALejo')

        last_name = self.browser.find_element_by_id('id_last_name')
        last_name.send_keys('perez')

        years = self.browser.find_element_by_id('id_years_of_experience')
        years.send_keys('3')

        phone_number = self.browser.find_element_by_id('id_phone_number')
        phone_number.send_keys('3103211293')

        email = self.browser.find_element_by_id('id_email')
        email.send_keys('email@eae.dd')

        imageFileUrl = self.browser.find_element_by_id('id_imageFileUrl')
        imageFileUrl.send_keys('http://evolvedms.com/images/ARP-Logo-EvolvedMS.jpg')

        username = self.browser.find_element_by_id('id_username')
        username.send_keys(''.join(random.choice(string.lowercase) for i in range(10)))

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('password')

        self.browser.find_element_by_id('id_button_register').click()
        self.browser.implicitly_wait(3)

        self.assertIsNone(self.browser.find_element_by_id('id_button_register').click())


