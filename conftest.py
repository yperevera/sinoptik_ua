import pytest
from selenium.webdriver import Chrome

def pytest_addoption(parser):
   parser.addoption("--driver", action="store", default="chrome", help="Type in browser type.")
   parser.addoption("--url", action="store", default="https://sinoptik.ua/", help="Type main url.")


@pytest.fixture(scope="module")
def driver(request):
   driver = request.config.getoption("--driver")
   if driver == "chrome":
      driver = Chrome()
      driver.get("about:blank")
      driver.implicitly_wait(10)
      driver.maximize_window()
      return driver
   else:
      print("Only Chrome browser is supported at the moment.")


@pytest.fixture(scope="module")
def main_url(request):
   return request.config.getoption("--url")
