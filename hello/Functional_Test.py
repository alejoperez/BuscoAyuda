from unittest import TestCase
from selenium import webdriver


class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda',self.browser.title)
'''
    def test_register(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_link_text('Registrarte')
        link.click()

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
        username.send_keys('username')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('password')

        self.browser.find_element_by_id('id_button_register').click()
        self.browser.implicitly_wait(3)

        self.assertIsNone(self.browser.find_element_by_id('id_button_register'))

'''

def test_ver_detalle(self):

        link = self.browser.find_element_by_id('id_detalle2')
        link.click()

        self.assertEqual('carro',self.browser.find_element_by_id('id_nombre').text,'Nombre invalido')


