import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Fixture to initialize and teardown Chrome WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    yield driver
    
    driver.quit()
