from selenium import webdriver
# 表 11-3 selenium 的 WebDriver 方法，用于寻找元素
# 方法名                                                 返回的 WebElement 对象/列表
# browser.find_element_by_class_name(name)              使用 CSS 类 name 的元素
# browser.find_elements_by_class_name(name)
# browser.find_element_by_css_selector(selector)        匹配 CSS selector 的元素
# browser.find_elements_by_css_selector(selector)
# browser.find_element_by_id(id)                        匹配 id 属性值的元素
# browser.find_elements_by_id(id)
# browser.find_element_by_link_text(text)               完全匹配提供的 text 的<a>元素
# browser.find_elements_by_link_text(text)
# browser.find_element_by_partial_link_text(text)       包含提供的 text 的<a>元素
# browser.find_elements_by_partial_link_text(text)
# browser.find_element_by_name(name)                    匹配 name 属性值的元素
# browser.find_elements_by_name(name)
# browser.find_element_by_tag_name(name)                匹配标签 name 的元素
# browser.find_elements_by_tag_name(name)               (大小写无关，<a>元素匹配'a'和'A')

# 表 11-4 WebElement 的属性和方法
# 属性或方法                  描述
# tag_name                  标签名，例如 'a'表示<a>元素
# get_attribute(name)       该元素 name 属性的值
# text                      该元素内的文本，例如<span>hello</span>中的'hello'
# clear()                   对于文本字段或文本区域元素，清除其中输入的文本
# is_displayed()            如果该元素可见，返回 True，否则返回 False
# is_enabled()              对于输入元素，如果该元素启用，返回 True，否则返回 False
# is_selected()             对于复选框或单选框元素，如果该元素被选中，选择 True，否则返回 False
# location                  一个字典，包含键'x'和'y'，表示该元素在页面上的位置

# 表 11-5 selenium.webdriver.common.keys 模块中常用的变量
# 属性                                               含义
# Keys.DOWN, Keys.UP, Keys.LEFT,Keys.RIGHT          键盘箭头键
# Keys.ENTER, Keys.RETURN                           回车和换行键
# Keys.HOME, Keys.END,                              Home 键、End 键、PageUp 键和 Page Down 键
# Keys.PAGE_DOWN,Keys.PAGE_UP
# Keys.ESCAPE, Keys.BACK_SPACE,Keys.DELETE          Esc、Backspace 和字母键
# Keys.F1, Keys.F2, . . . , Keys.F12                键盘顶部的 F1到 F12键
# Keys.TAB                                          Tab 键

# browser = webdriver.Safari()
# browser.get('https://inventwithpython.com')
# try:
#     elem = browser.find_element_by_class_name('bookcover')
#     print('Found <%s> element with that class name!' % elem.tag_name)
# except:
#     print('Was not able to find and element with that name.')

# browser = webdriver.Safari()
# browser.get('https://inventwithpython.com')
# linkElem = browser.find_element_by_link_text('Read It Online')
# print(type(linkElem))
# # <class 'selenium.webdriver.remote.webelement.WebElement'>
# linkElem.click() # follows the "Read It Online" link

# browser = webdriver.Safari()
# browser.get('http://gmail.com')
# emailElem = browser.find_element_by_id('Email')
# emailElem.send_keys('not_my_real_email@gmail.com')
# passwordElem = browser.find_element_by_id('Passwd')
# passwordElem.send_keys('12345')
# passwordElem.submit()


from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)  # scrolls to bottom
htmlElem.send_keys(Keys.HOME)  # scrolls to top
