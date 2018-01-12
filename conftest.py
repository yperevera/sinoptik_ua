import pytest
from selenium.webdriver import Chrome 

def pytest_addoption(parser):
   parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")
   parser.addoption("--url", action="store", default="https://sinoptik.ua/", help="main url")
   #parser.addoption("--username", action="store", default="manager", help="username")
   #parser.addoption("--password", action="store", default="test", help="password")


@pytest.fixture(scope="module", autouse=True)
def driver(request):
   browser = request.config.getoption("--driver")
   if browser == 'chrome':
       browser = Chrome()
       browser.get("about:blank")
       browser.implicitly_wait(10)
       browser.maximize_window()
       return browser
   else:
       print("Only chrome is supported at the moment.")


@pytest.fixture(scope="module")
def url(request):
   return request.config.getoption("--url")


#@pytest.fixture(scope="module")
#def username(request):
   #return request.config.getoption("--username")


#@pytest.fixture(scope="module")
#def password(request):
   #return request.config.getoption("--password")
