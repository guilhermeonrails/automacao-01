from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
# sleep(3)
driver.implicitly_wait(3)

text_box = driver.find_element(by=By.NAME, value='my-text')
text_box.send_keys('Python é vida!')
sleep(1)

password = driver.find_element(by=By.XPATH, value='/html/body/main/div/form/div/div[1]/label[2]/input')
password.send_keys('123456')
sleep(1)

btn = driver.find_element(by=By.CSS_SELECTOR, value='button')
btn.click()
sleep(3)

message = driver.find_element(by=By.ID, value='message').text
driver.implicitly_wait(3)
if message == 'Received!':
    print('Formulário submetido com sucesso!')
else:
    print('Tivemos um problema')

driver.get('https://www.alura.com.br/')
sleep(2)
driver.quit()