from playwright.sync_api import Playwright, sync_playwright, expect

# Общий синтаксический формат для записи сценария: codegen [параметры] [url] - в терминале
# playwright codegen --viewport-size=800,600 [url] - размер открываемого окна браузера
# playwright codegen -o lesson.py [url] - указать файл, в который будете сохранен записанный код, добавив аргумент -о или --output и указав имя файла

def test_add_todo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False) # запуск браузера chromium, браузер chromium отображался и был видимым при запуске кода
    context = browser.new_context()                      # создает изолированный сеанс браузера
    page = context.new_page()                            # открывает новую страницу(tab) в браузере
    page.goto("https://demo.playwright.dev/todomvc/#/")  # открыть веб-сайт
    page.get_by_placeholder("What needs to be done?").click()   # находит в DOM дереве веб-элемент c атрибутом тега placeholder и значением атрибута
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")    # вводит значения, переданные ему в качестве аргумента в веб-элемент
    page.get_by_placeholder("What needs to be done?").press("Enter")   # эмулирует нажатие клавиши Enter на клавиатуре
    page.get_by_role("link", name="Completed").click()  # эмулирует клик левой кнопкой мышки по веб-элементу

    # ---------------------
    # context.close()
    # browser.close()

