from selenium import webdriver

url = 'file:///I:/My%20Documents/articles/htmlgoodies/Web%20Scraping/demo/web_scraping_demo.html'
driver = webdriver.Chrome()
driver.get(url)
dynamicText = driver.find_element_by_css_selector("#dynamic-text")
message = dynamicText.get_attribute('innerHTML')
print("Dynamic text element says: '" + message + "'." )