from playwright.sync_api import Page, Route, expect

# Когда страница отправляет запрос к /api/tags, Playwright перехватывает его.
# Вместо оригинального ответа сервер возвращает модифицированный JSON с tags: ["open", "solutions"].
# После загрузки модифицированного ответа проверяется, что на странице действительно появились
# ссылки с текстом "open" и "solutions".

def test_intercepted(page: Page):

    #Перехватывает маршрут и изменяет ответ сервера
    def handle_route(route: Route):

        # Позволяет выполнить оригинальный запрос к серверу и получить его исходный ответ.
        response = route.fetch()
        json = response.json()

        # Модифицирует JSON, добавляя или изменяя данные в ключе "tags"
        json["tags"] = ["open", "solutions"]

        # Отправляет модифицированный JSON в браузер вместо оригинального ответа сервера.
        route.fulfill(json=json)

    # Настраивает перехват всех запросов, соответствующих шаблону URL **/api/tags.
    # Передает обработчик handle_route для обработки каждого перехваченного запроса.
    page.route("**/api/tags", handle_route)

    page.goto("https://demo.realworld.io/")
    sidebar = page.locator('css=div.sidebar')
    expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])

