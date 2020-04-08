from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, \
visibility_of_element_located, presence_of_element_located_s
from time import sleep

class Usuario:
    def __init__(self, driver):
        self.driver = driver
        self.CLICK_IES = (By.ID, "aba_mantida")
        self.IN_CPF = (By.ID,"txt_nu_cpf")
        self.IN_SENHA = (By.ID,"txt_no_senha")

    def find(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))

    def finds(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located_s(*locator))

    def find_reduce(self, *locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))

    def find_v(self, *locator, timeout=2):
        return WebDriverWait(self.driver, timeout).until(visibility_of_element_located(*locator))


    def frame_switch_id(self, id):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_id(id))

    def frame_switch_name(self, name):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_name(name))

    def validar_click(self,clique_certo = None):
        try:
            self.find(clique_certo).click()
        except Exception as x:
            print(x)
            sleep(2)
            return self.validar_click(clique_certo)

    def validar_click_reduce(self,clique_certo = None):
        try:
            self.find_reduce(clique_certo).click()
        except IOError as x:
            print(x)
            sleep(2)
            return self.validar_click_reduce(clique_certo)

    def validar_click_imediato(self,clique_certo = None):
        try:
            clique_certo.click()
        except IOError as x:
            print(x)
            sleep(2)
            return self.validar_click_imediato(clique_certo)

    # Clicando na IES
    def clicando_na_ies(self):
        return self.validar_click(self.CLICK_IES)

    # Escrevendo o login
    def username(self, cpf):
        input_cpf = self.find(self.IN_CPF)
        input_cpf.clear()
        input_cpf.send_keys(cpf)
        return sleep(1)

    # Escrevendo a senha
    def senha(self, senha):
        input_senha = self.find(self.IN_SENHA)
        input_senha.clear()
        input_senha.send_keys(senha)
        return sleep(1)

    # Enter para entrar
    def entrar_no_sistema(self):
        entrar = self.find(self.IN_SENHA)
        entrar.send_keys(Keys.ENTER)
        return sleep(1)
    pass