# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建一个Selenium WebDriver实例，打开网页
driver = webdriver.Chrome()
url = "https://news.google.com/articles/CBMixwFodHRwczovL3R3Lm5ld3MueWFob28uY29tLyVFNSU4RiVCMCVFNSU4RCU5NzMxJUU1JTgwJThCJUU4JUI3JUFGJUU1JThGJUEzJUU4JUE5JUE2JUU4JUJFJUE2JUU2JUE5JTlGJUU4JUJCJThBJUU3JTlCJUI0JUU2JThFJUE1JUU1JUI3JUE2JUU4JUJEJTg5LTUlRTUlQTQlQTklRTUlODMlODUxJUU5JTgxJTk1JUU4JUE2JThGLTAyMDgwMzY2Ni5odG1s0gHPAWh0dHBzOi8vdHcubmV3cy55YWhvby5jb20vYW1waHRtbC8lRTUlOEYlQjAlRTUlOEQlOTczMSVFNSU4MCU4QiVFOCVCNyVBRiVFNSU4RiVBMyVFOCVBOSVBNiVFOCVCRSVBNiVFNiVBOSU5RiVFOCVCQiU4QSVFNyU5QiVCNCVFNiU4RSVBNSVFNSVCNyVBNiVFOCVCRCU4OS01JUU1JUE0JUE5JUU1JTgzJTg1MSVFOSU4MSU5NSVFOCVBNiU4Ri0wMjA4MDM2NjYuaHRtbA?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"  # 请替换成您的目标网页链接
driver.get(url)

# 按 "itemprop" 属性查找目标元素
search_result = None
try:
    search_result = driver.find_element(By.CSS_SELECTOR, "[itemprop='articleBody'], div.caas-body, div.article-content.article-content_level-0,div.story[itemprop='articleBody']")
except:
    pass

# 检查是否找到目标元素
if search_result:
    text_content = search_result.text
    print(text_content)
    print("寫出大綱")
else:
    print("未找到目標元素")

# 关闭浏览器
driver.quit()
