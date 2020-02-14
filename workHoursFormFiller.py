from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC, ui
from time import sleep
from datetime import datetime, timedelta
import calendar

def fill():
    username = ''
    password = ''

    driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.get('https://cloud.corehr.com/pls/coreportal_nuimlive/cp_por_public_main_page.display_login_page')



    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "p_username"))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ext-gen1019"))).send_keys(password)


    submit = driver.find_element_by_tag_name('form')
    submit.submit()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/span/div/div[2]/div[1]/span/div/div/div[2]/div/a"))).click()

    element = driver.find_element_by_css_selector('.x-btn.x-unselectable.x-box-item.x-btn-default-small.x-icon-text-left.x-btn-icon-text-left.x-btn-default-small-icon-text-left')
    driver.execute_script("arguments[0].click();", element)

    iframes = driver.find_element_by_id("component-1151")

    # Switching to that frame
    driver.switch_to.frame(iframes)

    sleep(3)

    # Export click
    driver.find_element_by_xpath("/html/body/form[2]/div/div[5]/div[2]/div/table/tbody/tr[1]/td[1]/select/option[15]").click()

    driver.find_element_by_id("module1").send_keys("EE402")
    driver.find_element_by_id("date1").send_keys("12/02/2020")
    driver.find_element_by_id("from1").send_keys("14:00")
    driver.find_element_by_id("to1").send_keys("17:00")
    driver.find_element_by_name("p_declaration_chk").click()
    elem=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@onclick,'NEW')]/img[contains(@src,'coreimages/img/portal_button')]")))
    elem.click()

    # If you need to switch out of the frame to go back to the original HTML block
    driver.switch_to.default_content()


def get_weds():
    weds = {}
    now = datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    for x in range(1, days_in_month):


        today = datetime(2020, 3, x)
        offset = (today.weekday() - 2) % 7
        last_wednesday = today - timedelta(days=offset)
        weds[last_wednesday.strftime("%Y-%m-%d")] = 1
        print(last_wednesday)
    print(weds)

get_weds()

