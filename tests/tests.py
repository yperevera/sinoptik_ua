from selenium.webdriver.common.by import By

# ----- web elements ----- #
## logo
top_logo_img_xpath = "//div[@class='bLogo']/img"
top_logo_a_xpath = "//div[@class='bLogo']/img/../a"

## search form
search_form_xpath = "//form[@id='form-search']"
search_form_tag_p1_xpath = "//p[@class='clearfix']"
search_form_tag_p1_input1_xpath = "//input[@id='search_city']"
search_form_tag_p1_input2_xpath = "//input[@class='search_city-submit']"
search_form_tag_p2_xpath = "//p[@id='form-search-examples']"

## platform switch
platform_switch_xpath = "//a[@class='itypeSwitcher']"

## localization
localization_xpath = "//div[@id='sLang']"

## city and region
city_and_region_xpath = "//div[@class='cityName cityNameShort']"

## top menu
top_menu_xpath = "//div[@id='topMenu']"
top_menu_tag_a1_xpath = "//a[@class='menu-item']"
top_menu_tag_a2_xpath = "//a[@class='otherCity']"
top_menu_tag_span_xpath = "//span[@class='tMenu']"

## left column
under_termometr_ad_xpath = "//div[@style='position:relative']"
under_termometr_ad_div_xpath = "//div[@class='under-termometr']"
under_termometr_ad_div_div_xpath = "//div[@id='adriver_210x67']"
main_content_xpath = "//div[@id='mainContentBlock']"
bottom_ad_block_xpath = "//div[@id='leftCol']/div[contains(@style, 'width')]"
other_cities_weather_xpath = "//div[@id='tenOtherCities']"


right_ad_block_xpath = "//div[@id='rightCol']"
footer_xpath = "//div[@id='footer']"
copyright_xpath = "//div[@id='copyright']"

# ------------------------ #

# ----- expected ------ #
## title
exp_title_text = "SINOPTIK: Погода в Украине, подробный прогноз погоды на неделю. Погода сегодня, завтра в Украине и Мире."

## expected logo
exp_top_logo_img_src = "https://sinst.fwdcdn.com/img/newImg/sinoptic-logo-ny-2018.png"
exp_top_logo_img_alt = "погода"
exp_top_logo_img_title = "погода"
exp_top_logo_img_size = {"width": 239, "height": 89}
exp_top_logo_a_href = "https://sinoptik.ua/"
exp_top_logo_a_title = "погода"
exp_top_logo_text = "Прогноз погоды"

## expected search form
exp_search_form_attr_action = "https://sinoptik.ua/redirector"
exp_search_form_attr_method = "get"
exp_search_form_tags_p_len = 2
exp_search_form_tag_p1_input_len = 2
exp_search_form_tag_p1_input1_autocomplete = "off"
exp_search_form_tag_p1_input1_name = "search_city"
exp_search_form_tag_p1_input1_type = "text"
exp_search_form_tag_p1_input1_placeholder = "Название населенного пункта, страны или региона"
#exp_search_form_tag_p1_input1_value = ""
exp_search_form_tag_p1_input1_class = "ac_input"
exp_search_form_tag_p1_input2_type = "submit"
exp_search_form_tag_p1_input2_value = "Погода"
exp_search_form_tag_p2_a_max_len = 6

## expected platform switch
exp_platform_switch_attr_style = "display: none;"
exp_platform_switch_attr_href = "javascript:;"
exp_platform_switch_attr_onclick = "SIN.utility.cookie('_itype','smart',{expires:1});location.reload();"
exp_platform_switch_text = "Мобильная версия сайта"

## expected localization
exp_localization_text = "Sinoptik.ua українською"
exp_localization_tag_a_len = 1
exp_localization_tag_a_rel = "alternate"
exp_localization_tag_a_hreflang = "uk"
exp_localization_tag_a_text = "українською"

## expected city and region
exp_city_and_region_tag_h1_len = 1
# 'deep' means searching for specified tag recursively (through all lower tags)
exp_city_and_region_deep_tag_strong = 1
exp_city_and_region_tag_div_len = 1
exp_city_and_region_text = "Погода в "
exp_city_and_region_tag_div_class = "currentRegion"

## expected top menu
exp_top_menu_tag_a_len = 2
exp_top_menu_tag_span_len = 1
exp_top_menu_text = "7 дней  10 дней\nпогода на карте\n"

## expected left column
exp_left_column_under_termometr_ad_tag_div_len = 1
exp_left_column_under_termometr_ad_tag_div_div_len = 1
exp_left_column_main_content_deep_tag_div_len = 98
#exp_left_column_
#exp_left_column_
#exp_left_column_
#exp_left_column_
#exp_left_column_
#exp_left_column_
#exp_left_column_



# --------------------- #


def get_elements_list_xpath(driver, xpath):
    return driver.find_elements_by_xpath(xpath)


def get_element_xpath(driver, xpath):
    return driver.find_element_by_xpath(xpath)


def get_elements_list_css(driver, css):
    return driver.find_elements_by_css_selector(css)


def open_url(driver, main_url):
    driver.get(main_url)
    # url
    assert driver.current_url == main_url
    # title
    assert driver.title == exp_title_text


def verify_main_page_elements_presence(driver):
    # logo
    assert get_element_xpath(driver, top_logo_img_xpath).is_displayed() == True
    # search form
    assert get_element_xpath(driver, search_form_xpath).is_displayed() == True
    # platform switch
    assert get_element_xpath(driver, platform_switch_xpath).is_displayed() == False
    # localization
    assert get_element_xpath(driver, localization_xpath).is_displayed() == True
    # city and region
    assert get_element_xpath(driver, city_and_region_xpath).is_displayed() == True
    # top menu
    assert get_element_xpath(driver, top_menu_xpath).is_displayed() == True
    # main content block
    assert get_element_xpath(driver, main_content_xpath).is_displayed() == True
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


def verify_logo(driver):
    img_element = get_element_xpath(driver, top_logo_img_xpath)
    img_size = img_element.size
    a_element = get_element_xpath(driver, top_logo_a_xpath)

    # img src
    assert img_element.get_attribute('src') == exp_top_logo_img_src
    # img alt
    assert img_element.get_attribute('alt') == exp_top_logo_img_alt
    # img title
    assert img_element.get_attribute('title') == exp_top_logo_img_title
    # img size of element
    assert img_size['width'] == exp_top_logo_img_size['width']
    assert img_size['height'] == exp_top_logo_img_size['height']

    # a href
    assert a_element.get_attribute('href') == exp_top_logo_a_href
    # a title
    assert a_element.get_attribute('title') == exp_top_logo_a_title
    # a text
    assert a_element.text == exp_top_logo_text


def verify_search_form(driver):
    search_form = get_element_xpath(driver, search_form_xpath)
    search_form_tag_p1 = get_element_xpath(driver, search_form_tag_p1_xpath)
    search_form_tag_p1_input1 = get_element_xpath(driver, search_form_tag_p1_input1_xpath)
    search_form_tag_p1_input2 = get_element_xpath(driver, search_form_tag_p1_input2_xpath)
    search_form_tag_p2 = get_element_xpath(driver, search_form_tag_p2_xpath)

    # form action
    assert search_form.get_attribute('action') == exp_search_form_attr_action
    # form method
    assert search_form.get_attribute('method') == exp_search_form_attr_method

    # count of 'p' tags
    assert len(get_elements_list_xpath(search_form, "p")) == exp_search_form_tags_p_len
    # first 'p' tag
    ## count of 'input' tags 
    assert len(get_elements_list_xpath(search_form_tag_p1, "input")) == exp_search_form_tag_p1_input_len
    ## first input autocomplete
    assert search_form_tag_p1_input1.get_attribute('autocomplete') == exp_search_form_tag_p1_input1_autocomplete
    ## first input name
    assert search_form_tag_p1_input1.get_attribute('name') == exp_search_form_tag_p1_input1_name
    ## first input type
    assert search_form_tag_p1_input1.get_attribute('type') == exp_search_form_tag_p1_input1_type
    ## first input placeholder
    assert search_form_tag_p1_input1.get_attribute('placeholder') == exp_search_form_tag_p1_input1_placeholder
    ## first input value
    #assert search_form_tag_p1_input1.get_attribute('value') == exp_search_form_tag_p1_input1_value, "Actual: " + search_form_tag_p1_input1.get_attribute('value') + ". Expected: " + exp_search_form_tag_p1_input1_value
    ## first input class
    assert search_form_tag_p1_input1.get_attribute('class') == exp_search_form_tag_p1_input1_class

    ## second input type
    assert search_form_tag_p1_input2.get_attribute('type') == exp_search_form_tag_p1_input2_type
    ## second input value
    assert search_form_tag_p1_input2.get_attribute('value') == exp_search_form_tag_p1_input2_value

    # second 'p' tag
    ## count of 'a' tags
    assert len(get_elements_list_xpath(search_form_tag_p2, "a")) <= exp_search_form_tag_p2_a_max_len


def verify_platform_switch(driver):
    platform_switch = get_element_xpath(driver, platform_switch_xpath)

    # a style
    assert platform_switch.get_attribute('style') == exp_platform_switch_attr_style
    # a href
    assert platform_switch.get_attribute('href') == exp_platform_switch_attr_href
    # a onclick
    assert platform_switch.get_attribute('onclick') == exp_platform_switch_attr_onclick
    # a text
    assert platform_switch.get_attribute('innerText') == exp_platform_switch_text


def verify_localization_option(driver):
    localization = get_element_xpath(driver, localization_xpath)
    localization_tag_a = get_element_xpath(localization, "a")

    # text
    assert localization.get_attribute('innerText') == exp_localization_text
    # count of 'a' tags
    assert len(get_elements_list_xpath(localization, "a")) == exp_localization_tag_a_len
    # a rel
    assert localization_tag_a.get_attribute('rel') == exp_localization_tag_a_rel
    # a hreflang
    assert localization_tag_a.get_attribute('hreflang') == exp_localization_tag_a_hreflang
    # a text
    assert localization_tag_a.get_attribute('innerText') == exp_localization_tag_a_text


def verify_city_and_region(driver):
    city_and_region = get_element_xpath(driver, city_and_region_xpath)
    city_and_region_tag_div = get_element_xpath(city_and_region, "div")

    # count of 'h1' tags
    assert len(get_elements_list_xpath(city_and_region, "h1")) == exp_city_and_region_tag_h1_len
    # count of 'strong' tags
    assert len(get_elements_list_xpath(city_and_region, "*/strong")) == exp_city_and_region_deep_tag_strong
    # count of 'div' tags
    assert len(get_elements_list_xpath(city_and_region, "div")) == exp_city_and_region_tag_div_len

    # text
    assert city_and_region.get_attribute('innerText')[:9] == exp_city_and_region_text
    # div class
    assert city_and_region_tag_div.get_attribute('class') == exp_city_and_region_tag_div_class


def verify_top_menu(driver):
    top_menu = get_element_xpath(driver, top_menu_xpath)
    top_menu_tag_a1 = get_element_xpath(driver, top_menu_tag_a1_xpath)
    top_menu_tag_a2 = get_element_xpath(driver, top_menu_tag_a2_xpath)
    top_menu_tag_span = get_element_xpath(driver, top_menu_tag_span_xpath)

    # count of 'a' tags
    assert len(get_elements_list_xpath(top_menu, "a")) == exp_top_menu_tag_a_len
    # count of 'span' tags
    assert len(get_elements_list_xpath(top_menu, "span")) == exp_top_menu_tag_span_len

    # text
    assert top_menu.get_attribute('innerText') == exp_top_menu_text

    # attribute 'class' of 'a1', 'a2' and 'span' tags was self verified by creating
    # variables 'top_menu_tag_a1', 'top_menu_tag_a2', 'top_menu_tag_span'

    # attribute 'innerText' is not valid to verify in each tag ('a1', 'a2', 'span'),
    # because actual text moves between tegs 'a1', 'a2' and 'span' unexpectedly


def verify_left_column(driver):
    under_termometr_ad = get_element_xpath(driver, under_termometr_ad_xpath)
    under_termometr_ad_div = get_element_xpath(driver, under_termometr_ad_div_xpath)
    under_termometr_ad_div_div = get_element_xpath(driver, under_termometr_ad_div_div_xpath)
    main_content = get_element_xpath(driver, main_content_xpath)

    # under termometr block
    # count of 'div' tags
    assert len(get_elements_list_xpath(under_termometr_ad, "div")) == exp_left_column_under_termometr_ad_tag_div_len

    # attribute 'class' of 'div' tag was self verified by creating
    # variable 'under_termometr_ad_div'

    ## count of 'div' tags
    assert len(get_elements_list_xpath(under_termometr_ad_div, "div")) == exp_left_column_under_termometr_ad_tag_div_div_len
    
    ## attribute 'id' of 'div' tag was self verified by creating
    ## variable 'under_termometr_ad_div_div'

    # main content block
    # count of 'div' tags (deep)
    assert len(get_elements_list_css(main_content, "div")) == exp_left_column_main_content_deep_tag_div_len, "Actual: " + str(len(get_elements_list_xpath(main_content, "*/div"))) + ". Expected: " + str(exp_left_column_main_content_deep_tag_div_len)
    


