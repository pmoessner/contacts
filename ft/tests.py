from selenium import webdriver

browser = webdriver.Firefox()
browser.find_element_by_tag_name('body')
assert 'Django' in body.text

browser.quit()
