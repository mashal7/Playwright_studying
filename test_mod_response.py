import time
from playwright.sync_api import expect
from pyexpat.errors import messages


# Фикстура page предоставляет новую веб-страницу для запуска теста и функции для работы с ней
def test_mock_tags(page):
    page.route("**/api/tags", lambda route: route.fulfill(path="data.json"))
    page.goto('https://demo.realworld.io/')

