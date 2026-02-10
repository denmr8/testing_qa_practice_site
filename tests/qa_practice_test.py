from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Login_Page

def test_positive_login():
    driver=webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        login_page = Login_Page(driver)
        login_page.open()
        login_page.find_login_elements()
        login_page.login('qa_testers@qabrains.com', 'Password123')
        
        
        success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Login Successful')]")))

        assert success_message.is_displayed(), "Повідомлення про успішний вхід не знайдено!"
    
    finally:
        driver.quit()
        
def test_negative_login():
    driver=webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        login_page = Login_Page(driver)
        login_page.open()
        login_page.find_login_elements()
        login_page.login('qa_testers@qabrains.com', '1258d445') 
        
        unsuccess_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Your password is invalid!')]")))
        
        assert unsuccess_message.is_displayed(), "Повідомлення Your password is invalid! не знайдено!"
    finally:
        driver.quit()
        
        
def test_write_comment():
    driver=webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        login_page = Login_Page(driver)
        login_page.open()
        COMMENT_XPATH = (By.XPATH, "//textarea[@placeholder='Write Comment...']")
        text_area = wait.until(EC.visibility_of_element_located(COMMENT_XPATH))
          
        text_area.click()      
        text_area.send_keys('Beautifull')
        button=driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
        button.click()
    finally:
        driver.quit()


# def test_navigation():
#     driver=webdriver.Chrome()
#     wait = WebDriverWait(driver, 20)

#     try:
#         login_page = Login_Page(driver)
#         login_page.open()
#         BLOCK_TOPICS = (By.XPATH, "//a[contains(text(), 'QA Topics')]")
#         block1=wait.until(EC.element_to_be_clickable(BLOCK_TOPICS))
#         block1.click()
#         wait.until(EC.url_contains("topics"))
#         assert "topics" in driver.current_url
#         print("Тест успешно пройден!")
#     finally:
#         driver.quit()

def test_navigation():
    driver=webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    try:
        login_page = Login_Page(driver)
        login_page.open()
        
        BLOCK_TOPICS = (By.XPATH, "//a[contains(text(), 'QA Topics')]")
        
        link = wait.until(EC.element_to_be_clickable(BLOCK_TOPICS))
        link.click()

        wait.until(lambda d: d.current_url != "https://qabrains.com/practice") 
        
        current_url = driver.current_url.lower()
        print(f"\nРеальный URL после клика: {current_url}")

        assert "practice" in driver.current_url.lower()
        print("Тест реально пройден!")
    finally:
        driver.quit()

