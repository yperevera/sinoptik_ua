import tests.tests as tests

# Test 1 Verify that main page can be opened
def test_open_main_page(driver, main_url):
    tests.open_url(driver, main_url)

# Test 2 Verify that ALL main elements are displayed or not (if expected)
def test_main_page_elements_presence(driver):
    tests.verify_main_page_elements_presence(driver)

# Test 3 Verify logo attributes, tags, values
def test_top_logo(driver):
    tests.verify_logo(driver)

# Test 4 Verify search form attributes, tags, values
def test_search_form(driver):
    tests.verify_search_form(driver)
