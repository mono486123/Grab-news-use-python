from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')




input_text = input("輸入文字:" )

if input_text:
    driver = webdriver.Chrome(options=options) 


    driver.get("https://tw.news.yahoo.com/")
    
    # 定位搜尋框
    search_box = driver.find_element(By.XPATH, '//*[@id="ybar-sbq"]')
    
    # 在搜尋框中輸入搜尋內容
    search_box.send_keys(input_text)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

   # # 等待一些時間，讓新聞加載完成
    driver.implicitly_wait(5)
 
    titles = driver.find_elements(By.XPATH, '//h3/a')
    links = driver.find_elements(By.XPATH, '//h3/a')

     # 建一个列表来保存匹配的结果
    results = []

    for index, (title, link) in enumerate(zip(titles, links), start=1):
        # Extract title information
        title_text = title.text if title else "N/A"
        results.append({'編號': index, '標題': title_text})
    
        # Extract link information
        link_href = link.get_attribute("href") if link else "N/A"
        results.append({'連結': link_href})
    
        # Print combined information
        print(f"編號: {index}")
        print(f"標題: {title_text}")
        print(f"連結: {link_href}\n\n")
    
        
    
    




else:
    print("未找到關鍵字")