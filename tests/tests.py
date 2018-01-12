from selenium.webdriver.common.by import By

# elements
top_logo_xpath = "//div[@class='bLogo']/img"
search_form_xpath = "//form[@id='form-search']"
localization_xpath = "//div[@id='sLang']"
city_name_xpath = "//div[@class='cityName cityNameShort']"
top_menu_xpath = "//div[@id='topMenu']"
main_content_block_xpath = "//div[@id='mainContentBlock']"
bottom_ad_block_xpath = "//div[@id='leftCol']/div[contains(@style, 'width')]"
other_cities_weather_xpath = "//div[@id='tenOtherCities']"
right_ad_block_xpath = "//div[@id='rightCol']"
footer_xpath = "//div[@id='footer']"
copyright_xpath = "//div[@id='copyright']"

# expected




def get_elements_list_xpath(driver, xpath):
    return driver.find_elements_by_xpath(xpath)


def get_element_xpath(driver, xpath):
    return driver.find_element_by_xpath(xpath)


def open_url(driver, main_url):
    driver.get(main_url)
    assert driver.current_url == main_url


def verify_main_page_elements_presence(driver):
    # logo
    assert get_element_xpath(driver, top_logo_xpath).is_displayed() == True
    # search form
    assert get_element_xpath(driver, search_form_xpath).is_displayed() == True
    # localization
    assert get_element_xpath(driver, localization_xpath).is_displayed() == True
    # city name
    assert get_element_xpath(driver, city_name_xpath).is_displayed() == True
    # top menu
    assert get_element_xpath(driver, top_menu_xpath).is_displayed() == True
    # main content block
    assert get_element_xpath(driver, main_content_block_xpath).is_displayed() == True
    # bottom ads block
    assert get_element_xpath(driver, bottom_ad_block_xpath).is_displayed() == True
    # other cities weather
    assert get_element_xpath(driver, other_cities_weather_xpath).is_displayed() == True
    # right ad block
    assert get_element_xpath(driver, right_ad_block_xpath).is_displayed() == True
    # footer
    assert get_element_xpath(driver, footer_xpath).is_displayed() == True
    # copyright
    assert get_element_xpath(driver, copyright_xpath).is_displayed() == True
