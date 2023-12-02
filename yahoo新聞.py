import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#options = webdriver.ChromeOptions()
#options.add_argument('--headless')




input_text = "經濟"

# 正則表達
match = re.search(fr"({input_text})", input_text)

if match:
    search_keyword = match.group()
else:
    search_keyword = None

if search_keyword:
    driver = webdriver.Chrome()#options=options) 


    driver.get("https://tw.news.yahoo.com/")
    
    # 定位搜尋框
    search_box = driver.find_element(By.XPATH, '//*[@id="ybar-sbq"]')
    
    # 在搜尋框中輸入搜尋內容
    search_box.send_keys(search_keyword)
    search_box.send_keys(Keys.RETURN)
    

   
   ## 模擬滾動頁面，觸發更多新聞的加載

    time.sleep(5)


    if search_box.send_keys(Keys.RETURN):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")




   # # 等待一些時間，讓新聞加載完成
    driver.implicitly_wait(5)

    

    num_of_results = 40  # 設定想要獲取的資料數量
    titles = driver.find_elements(By.CSS_SELECTOR, '#stream-container-scroll-template li div h3 a')[:num_of_results]
    links = driver.find_elements(By.CSS_SELECTOR, '#stream-container-scroll-template li div h3 a')[:num_of_results]




    
    for index, (title, link) in enumerate(zip(titles, links), start=1):
        title_text = title.text
        link_href = link.get_attribute("href")
        # time = times[i].get_attribute("datetime")

       # if not 'https://tw.news.yahoo.com/' in link_href:
       #    continue
       # 

       
        print(f"編號: {index}")
        print(f"標題: {title_text}\n")
        print(f"連結: {link_href}\n\n")
        # print(f"時間: {time}\n")

   

else:
    print("未找到關鍵字")
