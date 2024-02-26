from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def fetch_exchange_rate(date, currency_code):
    # 指定WebDriver路径
    driver_path = 'C:\\Users\\19668\\Downloads\\chromedriver_win32\\chromedriver.exe'
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        driver.get('https://www.boc.cn/sourcedb/whpj/')
        # 等待页面加载完成
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pjname"))
        )

        # 输入日期
        date_input = driver.find_element(By.NAME, 'erectDate')
        date_input.clear()
        date_input.send_keys(date)

        # 输入货币代码
        currency_input = driver.find_element(By.NAME, 'pjname')
        currency_input.send_keys(currency_code)

        # 点击查询
        search_button = driver.find_element(By.CLASS_NAME, 'main1')
        search_button.click()

        # 等待结果加载
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='table']/tbody/tr[2]/td[7]"))
        )
        time.sleep(2)  # 额外等待时间确保数据加载

        # 获取现汇卖出价
        sell_price = driver.find_element(By.XPATH, "//table[@class='table']/tbody/tr[2]/td[7]").text

        # 打印并保存结果
        print(sell_price)
        with open('result.txt', 'w') as file:
            file.write(sell_price)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 yourcode.py <YYYYMMDD> <CurrencyCode>")
    else:
        date = sys.argv[1]
        currency_code = sys.argv[2]
        fetch_exchange_rate(date, currency_code)
