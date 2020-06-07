# import pytest
#
# from selenium import webdriver
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome",
#                      choices=["chrome", "firefox", "opera", "yandex"])
#     parser.addoption("--executor", action="store", default="192.168.56.1")
#
#
# @pytest.fixture
# def firefox(request):
#     wd = webdriver.Firefox()
#     request.addfinalizer(wd.quit)
#     return wd
#
#
# @pytest.fixture
# def chrome(request):
#     wd = webdriver.Chrome()
#     request.addfinalizer(wd.quit)
#     return wd
#
#
# @pytest.fixture
# def remote(request):
#     browser = request.config.getoption("--browser")
#     executor = request.config.getoption("--executor")
#     wd = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
#                           desired_capabilities={"browserName": browser})  # "platform": "linux"
#     wd.maximize_window()
#     request.addfinalizer(wd.quit)
#     return wd

from selenium import webdriver
import pytest
import keyring


@pytest.fixture
def remote(request):
    desired_cap = {
        'browser': 'IE',
        'browser_version': '11.0',
        'os': 'Windows',
        'os_version': '7',
        'resolution': '1024x768',
        'name': 'Bstack-[Python] Sample Test'
    }
    key = keyring.get_password("browserstack", "sh")
    wd = webdriver.Remote(
        command_executor=f'https://{key}.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)

    # wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd
