import time
from playwright.sync_api import expect
from pyexpat.errors import messages


# Фикстура page предоставляет новую веб-страницу для запуска теста и функции для работы с ней
def test_replace_from_har(page):
    page.goto("https://reqres.in/")
    page.route_from_har("example.har")
    users_single = page.locator('li[data-id="users-single"]')
    users_single.click()
    response = page.locator('[data-key="output-response"]')
    expect(response).to_contain_text("Open Solutions")


