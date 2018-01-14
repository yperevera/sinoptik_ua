from selenium.webdriver import Chrome
from time import sleep
import sqlite3
import os
import ast
import logging


# ---- logs config ----------- #
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# create a file handler
handler = logging.FileHandler('sinoptik_parser.log', 'w')
handler.setLevel(logging.DEBUG)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)
# ---------------------------- #

logger.info("Initializing..")
logger.info("Define global variables.")
# ---- variables ------------- #
db_file = "sinoptik_ua.db"
sql_counter = 0
#data = {'continent': 0, 'country': 0, 'region': 0, 'area': 0, 'city': 0} # region = oblast'; area = rayon
data = {'region': 0, 'area': 0, 'city': 0}
# ---------------------------- #

logger.info("Check if data file exists.")
# ---- load data from file --- #
if "data.txt" not in os.listdir():
    logger.info("Data file is not exists. Create new one.")
    with open("data.txt", "w") as f:
        f.close()
    logger.info("Data file was created.")
else:
    logger.info("Data file is exists. Load data from it.")
    with open("data.txt", "r") as f:
        data = f.read()
        data = ast.literal_eval(data)
    logger.info("Data was successfully loaded from existing file.")
# ---------------------------- #


def db_request(query=None, insert=False):
    try:
        logger.info("DB request. Create DB connection (if DB is NOT exists create new one).")
        # create connection and db if not exists
        conn = sqlite3.Connection(db_file)
        logger.info("DB request. Create DB cursor.")
        # create cursor
        cur = conn.cursor()
        if query == None:
            logger.info("DB request. Create a new table.")
            # create table if not exists
            query = '''CREATE TABLE IF NOT EXISTS city_ids(
                       id integer PRIMARY KEY,
                       city_id integer NOT NULL,
                       city_name text NOT NULL,
                       area_name text,
                       region_name text NOT NULL,
                       country_name text NOT NULL);'''
        else:
            if not insert:
                logger.info("Request DB. Verify. Send request to verify of existance of data.")
                cur.execute(query)
                logger.info("Request DB. Verify. Get response.")
                response = cur.fetchall()
                logger.info("Request DB. Verify. Verify response.")
                if response == []:
                    logger.info("Request DB. Verify. No such record.")
                    
                    return True, "OK."
                else:
                    if len(response) == 1:
                        logger.info("Request DB. Verify. Record is presented.")
                        return False, "Exists."
                    else:
                        logger.info("Request DB. Verify. More than 1 such record are presented.")
                        return False, "Exists > 1."   
            else:
                logger.info("Request DB. Insert. Send request to add new data.")
                cur.execute(query)
                logger.info("Request DB. Insert. Commit.")
                conn.commit()
            
    except:
        logger.info("Request DB. Except.")
        print("DB creation error!")
    finally:
        logger.info("Request DB. Finally. Close DB connection.")
        # close db connection
        conn.close()


def browser_run():
    logger.info("Browser. Run Chrome browser.")
    driver = Chrome()
    logger.info("Browser. Maximize browser window.")
    driver.maximize_window()
    logger.info("Browser. Go to the main page.")
    driver.get("https://sinoptik.ua/%D1%83%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0")
    logger.info("Browser. Setup implicitly wait. 30s.")
    driver.implicitly_wait(30)
    
    logger.info("Browser. Return driver.")
    return driver


def parser(driver):
    logger.info("Parser. Define local variables.")
    li_side_xpath = "//div[@class='jspPane']//li/a"
    li_bottom_xpath = "//div[@class='clearfix'][1]//li"
    data_city_xpath = "//div[@id='blockDays']"

    current_region = ""
    current_area = ""
    current_city = ""
    data_city_id = ""

    logger.info("Parser. Get list of regions.")
    regions = driver.find_elements_by_xpath(li_side_xpath)
    logger.info("Parser. Start loop1, begins from last NOT parsed region.")
    for i1 in range(data['region'], len(regions)):
        logger.info("Parser. Loop1. Save current region name.")
        current_region = regions[i1].get_attribute('innerText')
        logger.info("Parser. Loop1. Update 'data' region value.")
        data['region'] = i1
        logger.info("Parser. Loop1. Go to the region {}.".format(i1))
        regions[i1].click()
        logger.info("Parser. Loop1. Sleep. 1s.")
        sleep(1)
        logger.info("Parser. Loop1. Get list of areas.")
        areas = driver.find_elements_by_xpath(li_side_xpath)
        logger.info("Parser. Loop1. Start loop2, begins from last NOT parsed area.")
        for i2 in range(data['area'], len(areas)):
            logger.info("Parser. Loop1. Loop2. Save current area name.")
            current_area = areas[i2].get_attribute('innerText')
            logger.info("Parser. Loop1. Loop2. Update 'data' area value.")
            data['area'] = i2
            logger.info("Parser. Loop1. Loop2. Go to the area {}.".format(i2))
            areas[i2].click()
            logger.info("Parser. Loop1. Loop2. Sleep. 1s.")
            sleep(1)
            logger.info("Parser. Loop1. Loop2. Get list of cities.")
            cities = driver.find_elements_by_xpath(li_bottom_xpath)
            logger.info("Parser. Loop1. Loop2. Start loop3, begins from last NOT parsed city.")
            for i3 in range(data['city'], len(cities)):
                logger.info("Parser. Loop1. Loop2. Loop3. Save current city name.")
                current_city = areas[i3].get_attribute('innerText')
                logger.info("Parser. Loop1. Loop2. Loop3. Update 'data' city value.")
                data['city'] = i3

                ################
                logger.info("Parser. Loop1. Loop2. Loop3. Scroll down the page.")
                page = driver.find_element_by_css_selector('body')
                page.send_keys(Keys.END)
                ################

                logger.info("Parser. Loop1. Loop2. Loop3. Go to the city {}.".format(i3))
                cities[i3].click()
                logger.info("Parser. Loop1. Loop2. Loop3. Sleep. 1s.")
                sleep(1)
                logger.info("Parser. Loop1. Loop2. Loop3. Get data_city_id value.")
                data_city_id = driver.find_element_by_xpath(data_city_xpath).get_attribute('data-city-id')

                logger.info("Parser. Loop1. Loop2. Loop3. Check city_id record in DB.")
                query = '''SELECT * FROM city_ids WHERE city_id='{}';'''.format(data_city_id)
                status, msg = db_request(query)
                if status:
                    logger.info("Parser. Loop1. Loop2. Loop3. Record to the DB.")
                    query = '''INSERT INTO city_ids(
                                  city_id,
                                  city_name,
                                  area_name,
                                  region_name,
                                  country_name) VALUES(
                                  {}, '{}', '{}', '{}', "Украина");'''.format(
                                      int(data_city_id),
                                      current_city,
                                      current_area,
                                      current_region)
                    db_request(query, True)
                else:
                    if msg == "Exists.":
                        logger.info("Parser. Loop1. Loop2. Loop3. Skip.")
                    else:
                        logger.info("ATTENTION! Parser. Loop1. Loop2. Loop3. At least 2 records with the same ID!")

                logger.info("Parser. Loop1. Loop2. Loop3. Go back to the previous page.")
                driver.back()
                logger.info("Parser. Loop1. Loop2. Loop3. Sleep. 1s.")
                sleep(1)
                if sql_counter % 100 == 0:
                    print(sql_counter, "records id DB. ()")
                    ans = input("Would you like to continue?(y/n) ")
                    if ans == "y":
                        if (i3 + 1) == len(cities):
                            data['city'] = 0
                            if (i2 + 1) == len(areas):
                                data['area'] = 0
                                if (i1 + 1) == len(regions):
                                    with open("data.txt", "w") as f:
                                        f.write(data)
                                    logger.info("Parser. Loop1. Loop2. Loop3. Data file was updated. ALL cities in Ukraine is successfully parsed.")
                                else:
                                    data['region'] = (i1+1)
                                    with open("data.txt", "w") as f:
                                        f.write(data)
                            else:
                                data['area'] = (i2+1)
                                with open("data.txt", "w") as f:
                                    f.write(data)
                        else:
                            data['city'] = (i3+1)
                            with open("data.txt", "w") as f:
                                f.write(data)
                        logger.info("Parser. Loop1. Loop2. Loop3. Data file was updated. Exit.")
                        return


def runner():
    try:
        logger.info("Runner. Create DB.")
        db_request()
        logger.info("Runner. Run browser.")
        driver = browser_run()
        logger.info("Runner. Start parser.")
        parser(driver)
    #except:
        #logger.info("Runner. Except.")
        #driver.quit()


if __name__ == "__main__":
    logger.info("Start parser.")
    runner()
    logger.info("Finished.")
