import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     choices=["chrome", "firefox", "opera", "yandex"])
    parser.addoption("--executor", action="store", default="192.168.56.1")


@pytest.fixture
def firefox(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def chrome(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    wd = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                          desired_capabilities={"browserName": browser})  # "platform": "linux"
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd
