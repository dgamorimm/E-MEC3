from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, \
visibility_of_element_located, presence_of_element_located_s
from time import sleep
from selenium.webdriver.support.ui import Select

class Navegacao:
    def __init__(self, driver):
        self.driver = driver
        self.CLICK_IES = (By.CLASS_NAME, "corDetalhe_2")
        self.SELECT_PESQUISA = (By.ID, "tp_pesquisa")
        self.IN_PESQUISA = (By.ID, "data-PESQUISARCURSO-no_pesquisa")
        self.VALIDA_CARREGAMENTO = (By.CLASS_NAME, "loading")
        self.CLICK_CURSO = ""

    def find(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))

    def finds(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located_s(*locator))

    def find_reduce(self, *locator, timeout=1):
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

    # Clicando na Unesa
    def clicando_na_unesa(self):
        self.validar_click(self.CLICK_IES)
        return sleep(1)

    # pesquisa por código
    def filtrar_por_codigo(self):
       select_pesquisa = Select(self.find(self.SELECT_PESQUISA))
       select_pesquisa.select_by_value("co_ies_curso")

    def validar_loading(self):
        sleep(2)
        try:
            while True:
                self.find_reduce(self.VALIDA_CARREGAMENTO)
        except:
            return

    def pesquisar_por_codigo(self,codigo):
       pesquisa = self.find(self.IN_PESQUISA)
       pesquisa.clear()
       pesquisa.send_keys(codigo)
       pesquisa.send_keys(Keys.ENTER)
       sleep(2)

    def clicar_no_curso(self,id):
        self.CLICK_CURSO = (By.ID, str(id))
        self.validar_click(self.CLICK_CURSO)

