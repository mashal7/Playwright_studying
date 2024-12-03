import pytest

pytest_plugins = ["pytest_playwright"]

# @pytest.fixture()
# def browser_fixture():
#     return {
#         "viewport": {
#             "width": 1920,
#             "height": 1080,
#         }
#     }

# настройка фикстуры для управления браузером вручную

import pytest
from playwright.sync_api import sync_playwright

# Фикстура для браузера, открывается один раз на всю сессию
@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)  # Открываем браузер
    yield browser
    # Не закрываем браузер в этой фикстуре, если хотите, чтобы он остался открытым
    # browser.close()  # Уберите эту строку, чтобы не закрывать браузер
    playwright.stop()

# Фикстура для страницы, открывается для каждого теста
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()  # Создаем новый контекст
    page = context.new_page()  # Создаем новую страницу
    yield page
    # Не закрываем контекст после теста, чтобы оставить его открытым
    # context.close()  # Уберите эту строку, чтобы контекст не закрывался