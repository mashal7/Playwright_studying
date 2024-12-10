import time
from playwright.sync_api import expect
from pyexpat.errors import messages


# Фикстура page предоставляет новую веб-страницу для запуска теста и функции для работы с ней
def test_replace_from_har(page):
    page.goto("https://reqres.in/")

    # Настраивает Playwright на использование файла HAR (example.har) для подмены сетевых запросов.
    # Когда на странице делаются сетевые запросы, Playwright будет использовать данные из HAR,
    # вместо отправки реальных запросов.
    page.route_from_har("example.har")

    # Находит элемент с атрибутом data-id="users-single". Это локатор для элемента,
    # который, предположительно, вызывает запрос (например, для загрузки информации о пользователе).
    users_single = page.locator('li[data-id="users-single"]')


    users_single.click()

    # Находит элемент, содержащий текст ответа от сервера, который отображается после выполнения запроса.
    response = page.locator('[data-key="output-response"]')

    # Проверяет, что текст "Open Solutions" содержится в элементе, обозначенном локатором response.
    expect(response).to_contain_text("Open Solutions")

# для создания файла HAR, отфильтровать и сохранить вызовы только эндпонитов API
# playwright open --save-har=example.har --save-har-glob="**/api/**" https://reqres.in