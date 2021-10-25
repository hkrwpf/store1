from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://suning.com")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("移动硬盘")
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()

h = driver.current_window_handle
driver.find_element_by_xpath("//*[@id='0000000000-10517485676']/div/div").click()
all_h = driver.window_handles

for i in all_h:
    if i != h:
        driver.switch_to.window(i)


driver.switch_to.window(all_h[1])

driver.find_element_by_xpath("//*[@id='addCart']").click()

driver.find_element_by_xpath("/html/body/div[38]/div/div[2]/div/div[1]/a").click()

driver.find_element_by_xpath("//*[@id='cart-wrapper']/div[3]/div/div/div[2]/div[2]/a").click()


