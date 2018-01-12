import tests.tests as tests

# Test 1 verify that main page can be opened
def test_open_main_page(driver, main_url):
    tests.open_url(driver, main_url)

# Test 2 Verify that ALL main elements are displayed
def test_main_page_elements_presence(driver):
    tests.verify_main_page_elements_presence(driver)
