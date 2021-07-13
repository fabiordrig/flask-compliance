from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def get_info():
    # options = Options()
    # options.headless = True
    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.get(
        "https://www3.tjrj.jus.br/consultaprocessual/#/consultapublica#cpfcnpj")
    driver.switch_to.frame("mainframe")

    driver.find_element_by_id('filtroOrigem3').click()
    driver.find_element_by_id('itemAutocompletefiltroOrigem30').click()
    driver.find_element_by_id('cpfCnpj').send_keys('40892421851')

    driver.find_element_by_id('botaoPesquisarProcesso').click()

    # driver.switch_to.default_content()
