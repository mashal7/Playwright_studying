import time
from playwright.sync_api import expect
from pyexpat.errors import messages

#  необходимо изменить передаваемый данные
def test_network(page):
    # Настраивает перехват всех запросов, содержащих в URL подстроку register
    # лямбда-обработчик вызывается при перехвате соответствующего запроса.
    # route.continue_(post_data=...) изменяет тело запроса (в данном случае, отправляются данные: {"email": "user","password": "secret"}).
    # Вместо исходного тела запроса, серверу передается модифицированное тело
    page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))

    page.goto('https://reqres.in/')
    page.get_by_text(' Register - successful ').click()


