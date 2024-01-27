import pytest
from selenium import webdriver


# @pytest.fixture(params=["chrome", "safari"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "safari":
        my_driver = webdriver.Safari()
    else:
        raise TypeError(f"Expected 'chrome' or 'safari', but got '{browser}'")
    yield my_driver
    print(f"closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser to use for the tests (chrome or safari)")


@pytest.fixture
def driver_NC():
    print(f"creating driver")
    my_driver = webdriver.Chrome()
    yield my_driver
    print(f"closing driver")
    my_driver.quit()


