import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
from tests.all_tests import Actions


class First():
    def start(self):
        """Запускаем драйвер"""
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service('C:\\Users\\MGaming\\PycharmProjects\\python_selenium\\chromedriver.exe')
        driver_g = webdriver.Chrome(options=options, service=g)
        base_url = "https://www.playground.ru/"
        driver_g.get(base_url)


        login_standard_user = "yastesnyatsya22"
        password_all = "qwerty12345"

        print("Открылся браузер")

        wrong_data = Actions(driver_g)
        wrong_data.negativ_auth()

        auth = Actions(driver_g)
        auth.test_autorization(login_standard_user, password_all)

        logout = Actions(driver_g)
        logout.test_logout()

        main_page = Actions(driver_g)
        main_page.test_main_page()

        expect_error = Actions(driver_g)
        expect_error.waiting_for_error()

        screenshots = Actions(driver_g)
        screenshots.make_screenshots()

        filters = Actions(driver_g)
        filters.chose_filter()

        games = Actions(driver_g)
        games.buy_game()

new = First()
new.start()


