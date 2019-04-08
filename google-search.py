from selenium import webdriver

search_query = input("Enter the search query:")
search_query = search_query.replace(' ', '+') #structuring our search query for search url.
executable_path = "/path/to/chromedriver"
browser = webdriver.Chrome(executable_path=executable_path)


for i in range(20):
    browser.get("https://www.google.com/search?q=" + search_query + "&start=" + str(10 * i))
    matched_elements = browser.find_elements_by_xpath('//a[starts-with(@href, "http://behnamriahi.ir")]')
    if matched_elements:
        matched_elements[0].click()
        break