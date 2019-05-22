from selenium import webdriver

#search_query = input("Enter the search query:")
search_query = 'بهنام ریاحی'
#search_query = 'behnam riahi'
search_query = search_query.replace(' ', '+') #structuring our search query for search url.

executable_path = "/home/behnam/Downloads/geckodriver"

profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)

while 1:
	browser = webdriver.Firefox(executable_path=executable_path,firefox_profile= profile)
	browser.minimize_window()
	for i in range(20):
	    browser.get("https://www.google.com/search?q=" + search_query + "&start=" + str(10 * i))
	    matched_elements = browser.find_elements_by_xpath('//a[starts-with(@href, "http://behnamriahi.ir")]')
	    if matched_elements:
	        matched_elements[0].click()
	        break
	    check_robot = browser.find_elements_by_xpath('//form[starts-with(@id, "captcha-form")]')
	    if check_robot:
	    	break
