import random
import string
from unittest import TestCase

# Create your tests here.
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

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
        self.assertIsNone(self.browser.find_element_by_id('id_button_register').click())

    def test_detalle(self):
        self.browser.get('http://localhost:8000')

        id_detalle = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_detalle5"))
        )
        id_detalle.click()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_name_detail"))
        )

        self.assertEquals('http://localhost:8000/#/detail/5', self.browser.current_url, 'url mal')

    def test_login(self):
        self.browser.get('http://localhost:8000/#/login')
        self.browser.implicitly_wait(1)

        name = self.browser.find_element_by_id('username')
        name.send_keys('alejo2')

        name = self.browser.find_element_by_id('password')
        name.send_keys('alejandro')

        self.browser.find_element_by_id('id_login').click()
        self.assertEquals('http://localhost:8000/#/login', self.browser.current_url, 'login mal')

    def test_comentario(self):
        self.browser.get('http://localhost:8000/#/comments/5')
        self.browser.implicitly_wait(1)

        user_email = self.browser.find_element_by_id('userEmail')
        user_email.send_keys('a@a.com')

        comentario = self.browser.find_element_by_id('comment')
        comentario.send_keys('Mi comentario de prueba')

        self.browser.find_element_by_id('btnEnviar').click()
        self.assertEquals('Enviando...', self.browser.find_element_by_id('areaMensaje').text, 'comentario mal')

    def test_edicion(self):
        self.test_login()

        self.browser.find_element_by_id('id_perfil').click()
        self.browser.implicitly_wait(1)

        name = self.browser.find_element_by_id('name')
        old_name = name.text
        name.send_keys('alejo23')

        self.assertNotEqual(old_name, self.browser.find_element_by_id('name'), 'edicion mal')

    def test_busqueda(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(1)

        last_name = self.browser.find_element_by_id('id_busqueda')
        last_name.send_keys('alejo2')

        self.assertIsNone(self.browser.find_element_by_id('id_detalle7').click())
