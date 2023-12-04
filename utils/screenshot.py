import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.logger import setup_logger
logger = setup_logger(logger_name='screenshot')


def screenshot(url, file_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    
    time.sleep(2)

    # Obtém a altura total da página
    total_height = int(driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );"))

    # Define o tamanho da janela do navegador para cobrir a página inteira
    driver.set_window_size(1920, total_height)

    driver.save_screenshot(file_name)

    driver.quit()
