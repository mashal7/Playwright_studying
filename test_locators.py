import time

# Фикстура page предоставляет новую веб-страницу для запуска теста и функции для работы с ней
def test_locators(page) -> None:
    page.goto("https://webdriveruniversity.com/Popup-Alerts/index.html")
    # Ожидание полной загрузки страницы
    #page.wait_for_load_state("networkidle", timeout=30000)
    #page.wait_for_load_state('load', timeout=100000)  # Ожидаем завершения загрузки страницы
    #page.wait_for_load_state('domcontentloaded', timeout=1000000)  # Ожидает, когда DOM будет полностью загружен (быстрее, чем load).

    # page.locator('#username').fill('mashal7')
    # page.locator('#password').fill('qwerty123')
    # page.locator('#log-in').click()

    # Метод page.on('dialog', handler)
    # dialog — это событие, которое возникает, когда на странице появляется диалог.
    # handler — это функция, которая вызывается, когда появляется диалог. Функция обработчика получает объект типа Dialog

    # pytest --headed  - выполнить в режиме headed

    def test_dialogs(page):
        # функция-обработчик для диалогов
        def dialog_handler(dialog):
            print(f'Dialog message: {dialog.type}')
            print(f'Dialog message: {dialog.message}')

            # проверка типа диалога и обработка
            if dialog.type == 'alert':
                dialog.accept()
            if dialog.type == 'confirm':
                dialog.dismiss()
            if dialog.type == 'prompt':
                dialog.type('OK')
                dialog.accept()

        # обработчик для события диалог
        page.on('dialog', dialog_handler)

        # генерация alert (клик по кнопке)
        #page.locator('#button1').click() #alert
        page.locator('#button4').click() #confirm


    test_dialogs(page)
    input("Нажмите Enter для продолжения...")
