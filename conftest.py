import os
import pytest
from datetime import datetime
pytest_plugins = ["pytest_playwright"]

@pytest.fixture()
def browser_fixture():
    return {
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

# import pytest
# from playwright.sync_api import sync_playwright
#
# # Фикстура для браузера, открывается один раз на всю сессию
# @pytest.fixture(scope="session")
# def browser():
#     playwright = sync_playwright().start()
#     browser = playwright.chromium.launch(headless=False)  # Открываем браузер
#     yield browser
#     browser.close()  # Уберите эту строку, чтобы не закрывать браузер
#     playwright.stop()
#
# # # Фикстура для страницы, открывается для каждого теста
# @pytest.fixture(scope="function")
# def page(browser):
#     context = browser.new_context()  # Создаем новый контекст
#     page = context.new_page()  # Создаем новую страницу
#     yield page
#     context.close()  # Уберите эту строку, чтобы контекст не закрывался

# Хук для создания скриншотов в случае, если тест завершается с ошибкой
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     Хук pytest для создания скриншота в случае провала теста.
#     Выполняется после каждого теста, анализируя его результат.
#     """
#     outcome = yield  # Приостанавливает выполнение до завершения теста
#     report = outcome.get_result()  # Получает отчет о выполнении теста
#
#     # Проверяем, завершился ли тест с ошибкой
#     if report.when == "call" and report.failed:
#         # Получаем объект 'page' из аргументов теста, если он был передан через фикстуру
#         page = item.funcargs.get("page", None)
#
#         if page:  # Если страница была создана и передана в тест
#             # Генерируем путь для сохранения скриншота
#             timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
#             folder_path = os.path.abspath('screens')
#             screenshot_path = os.path.join(folder_path, f"{item.name}_{timestamp}.png")
#
#             # Делаем скриншот текущего состояния страницы
#             page.screenshot(path=screenshot_path)
#
#             # Выводим сообщение о сохранении скриншота в консоль
#             print(f"Screenshot saved for failed test: {screenshot_path}")




