from playwright.sync_api import Playwright, sync_playwright, expect

# Общий синтаксический формат для записи сценария: codegen [параметры] [url] - в терминале
# playwright codegen --viewport-size=800,600 [url] - размер открываемого окна браузера
# playwright codegen -o lesson.py [url] - указать файл, в который будете сохранен записанный код, добавив аргумент -о или --output и указав имя файла

# Фикстура page предоставляет новую веб-страницу для запуска теста и функции для работы с ней
def test_add_todo_fixture(page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    # pytest --headed  - выполнить в режиме headed


