import time
from playwright.sync_api import expect
from pyexpat.errors import messages


# Фикстура page предоставляет новую веб-страницу для запуска теста и функции для работы с ней
def test_network(page):
    page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))
    page.goto('https://reqres.in/')
    page.get_by_text(' Register - successful ').click()


