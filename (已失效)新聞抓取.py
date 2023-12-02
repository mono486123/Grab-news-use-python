import re
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

# 输入的文本
input_text = input("輸入新聞關鍵字(快捷> 1=台灣，2=台南，3=台東，4=經濟)  :")

if input_text=="1":
    input_text="台灣"

elif input_text=="2":
    input_text="台南"

elif input_text=="3":
    input_text="台東"

elif input_text=="4":
    input_text="經濟"
else:
    input_text

# 使用正则表达式提取关键字
match = re.search(fr"({input_text})", input_text)

if match:
    search_keyword = match.group()

else:
    search_keyword = None



if search_keyword:
            # 启动Chrome浏览器
    driver = webdriver.Chrome()
    # 打开Google新闻
    driver.get("https://news.google.com")
    # 找到搜索框并输入关键字，然后按Enter
    search_box = driver.find_element(By.XPATH, '//input[@aria-label="搜尋主題、地點和來源"]')
    search_box.send_keys(search_keyword)
    search_box.send_keys(Keys.RETURN)
    # 等待一些时间以便页面加载完成
    driver.implicitly_wait(10)
    # 提取搜索结果标题、链接和时间
    search_results = driver.find_elements(By.CSS_SELECTOR, "a.VDXfz")
    titles = driver.find_elements(By.CSS_SELECTOR, "h3.ipQwMb.ekueJc.RD0gLb")
    time_elements = driver.find_elements(By.CSS_SELECTOR, "time.WW6dff")
    # 创建一个列表来保存匹配的结果
    results = []
    for i, result in enumerate(search_results):
        title= titles[i].text
        link = result.get_attribute("href")
        time = time_elements[i].get_attribute("datetime")
        
      
        if time.endswith('Z'):
            time = time[:-1]  # 去掉末尾的 'Z'
        news_time = datetime.fromisoformat(time)
        cutoff_date = datetime.now() - timedelta(days=1)
        if news_time >= cutoff_date:
            results.append((title, link, time))
    # 按时间排序结果
    results.sort(key=lambda x: x[2])
    save_directory = r"C:\Users\jack8\Dropbox\我的電腦 (LAPTOP-GNOUPD9G)\Downloads\python儲存檔案\新聞\新聞文字檔"
      
    current_time = datetime.now().strftime("%Y-%m-%d  %H-%M-%S")
    # 使用下划线替代文件名中的冒号
    file_name = f"{input_text}_{current_time} 新聞.txt".replace(":", "_")
    file_path = os.path.join(save_directory, file_name)
    # 创建一个文本文件来保存结果
    with open(file_path, "w", encoding="utf-8") as file:
        for title, link, time in results:
            file.write(f"標題: {title}\n")
            file.write(f"連結: {link}\n")
            file.write(f"時間: {time}\n\n")
    # 关闭浏览器
    driver.quit()
       
else:
    print("未找到關鍵字")
