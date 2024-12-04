import time
from playwright.sync_api import expect
from pyexpat.errors import messages


# Фикстура page предоставляет новую веб-страницу для запуска теста и функции для работы с ней
def test_locators(page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")

    # проверка url
    expect(page).to_have_url('https://demo.playwright.dev/todomvc/#/')

    # проверка, что поле ввода задачи пустое
    field_input = page.get_by_placeholder('What needs to be done?')
    expect(field_input).to_be_empty()

    # ввести 2 задачи и проверить что количество задач в списке равно двум
    field_input.fill('number 1')
    field_input.press('Enter')
    field_input.fill('number 2')
    field_input.press('Enter')
    items_locator = page.get_by_test_id('todo-item')
    expect(items_locator).to_have_count(2)

    # отметить одну задачу выполненной и проверить что она выполнена
    items_locator.get_by_role('checkbox').nth(0).click()
    expect(items_locator.nth(0)).to_have_class('complete')


    input("Нажмите Enter для продолжения...")