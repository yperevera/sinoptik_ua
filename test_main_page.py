import tests.tests as tests

# Test 1 Verify that main page can be opened
def test_open_main_page(driver, main_url):
    tests.open_url(driver, main_url)

# Test 2 Verify that ALL main elements are displayed or not (if expected)
def test_main_page_elements_presence(driver):
    tests.verify_main_page_elements_presence(driver)

# Test 3 Verify logo
def test_top_logo(driver):
    tests.verify_logo(driver)

# Test 4 Verify search form
def test_search_form(driver):
    tests.verify_search_form(driver)

# Test 5 Verify platform switch
def test_platform_switch(driver):
    tests.verify_platform_switch(driver)

# Test 6 Verify localization option
def test_localization_option(driver):
    tests.verify_localization_option(driver)

# Test 7 Verify city and region
def test_city_and_region(driver):
    tests.verify_city_and_region(driver)

# Test 8 Verify top menu
def test_top_menu(driver):
    tests.verify_top_menu(driver)

# Test 9 Verify left column
def test_left_column(driver):
    tests.verify_left_column(driver)
