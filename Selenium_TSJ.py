# -------------------------------------------------------------------載入相關模組
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# -------------------------------------------------------------------設定Chrome Driver 的執行檔案路徑
# Chrome 114版載點 : https://google-chrome.cn.uptodown.com/windows/download/104298869
options = Options()
options.executable_path = "D:\Selenium\chromedriver.exe"
options.add_argument("--auto-open-devtools-for-tabs")  # 開啟F12

# -------------------------------------------------------------------建立Driver 物件實體，用程式操作 瀏覽器 運作
driver = webdriver.Chrome(options=options)
driver.maximize_window() # 視窗最大化

# -------------------------------------------------------------------指定存取網址
url="https://tsj.tw/"
driver.get(url)
time.sleep(1)


# -------------------------------------------------------------------抓按鍵與點數
blow = driver.find_element(By.ID, 'click')
blow_count = driver.find_element(By.XPATH, "//h4[2]")

# -------------------------------------------------------------------抓商品
props = driver.find_elements(By.XPATH, "//i")
props = [props[0],props[3],props[6]]

# -------------------------------------------------------------------抓價格
prices=[]
prices.append(driver.find_element(By.XPATH, "//table[1]/tbody/tr[2]/td[4]"))
prices.append(driver.find_element(By.XPATH, "//table[1]/tbody/tr[3]/td[4]"))
prices.append(driver.find_element(By.XPATH, "//table[1]/tbody/tr[4]/td[4]"))

# -------------------------------------------------------------------
for i in range(500):
    blow.click() #吹一下
    count = int(blow_count.text.replace("您目前擁有", "").replace("技術點", "")) #目前點數
    for j in range(3):
        price = int(prices[j].text.replace("技術點", "")) #目前價格
        if count >= price:
            props[j].click()
            break


time.sleep(10)
# -------------------------------------------------------------------關閉此次執行的WebDriver
driver.close()