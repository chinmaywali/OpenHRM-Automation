
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(5)


def login():
    driver.find_element(By.NAME, "username").send_keys("Admin")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("admin123")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    act_title = driver.title
    exp_title = "OrangeHRM"
    if act_title == exp_title:
        print("Login Test Passed")
    else:
        print("Login Test False")


login()


def forgot_pass():
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input').send_keys("Admin")
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]').click()
    time.sleep(5)
    driver.back()
    time.sleep(5)
    driver.back()
    time.sleep(5)
    print("Forgot Password Test Passed")


def Help():
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/div/button/i').click()
    time.sleep(5)
    h = driver.window_handles
    par = h[0]
    chi = h[1]
    driver.switch_to.window(par)
    time.sleep(5)
    print("Help Test Passed")

def logout():
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
    time.sleep(5)
    print("logout Test Passed")


def about():
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[1]/a').click()
    time.sleep(7)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/button').click()
    time.sleep(5)
    print("About Test Passed")



def support():
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[2]/a').click()
    time.sleep(5)
    driver.back()
    time.sleep(5)
    print("Support Test Passed")


def account():
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
    time.sleep(5)
    about()

    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
    time.sleep(5)
    support()

    Help()

    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
    time.sleep(5)
    logout()

    forgot_pass()


    driver.quit()


account()
