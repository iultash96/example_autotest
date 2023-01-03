import datetime
import sys
import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Actions():
    def __init__(self, driver):
        self.driver = driver

    def test_autorization(self, login_standard_user, password_all):
        try:
            icon = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='userNotAuthorized']/header/div[1]/div[2]/a[3]")))
            icon.click()

            login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='name']")))
            login.send_keys(login_standard_user)
            print("Введен логин")

            password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
            password.send_keys(password_all)
            print("Введен пароль")

            button_login = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='signinModalWindow']/div/div/div/div[1]/form/button/b")))
            button_login.click()
            print("Нажата кнопка авторизации")

            button_login = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[1]/div[2]/div/div[1]/img")))
            button_login.click()
            print("Выполнена авторизация")
        except Exception as exception:
            self.driver.refresh()
            self.test_autorization(login_standard_user, password_all)

    def test_logout(self):
        logout_step1 = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[1]/nav/ul/li[7]/a")))
        logout_step1.click()
        print("первый шаг к выходу")

        logout_step2 = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[1]/div[2]/div/div[1]/img")))
        logout_step2.click()
        print("Второй шаг к выходу")

        logout_step3 = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[1]/div[2]/div/div[2]/div/div[3]/a[2]")))
        logout_step3.click()
        print("Вышел")
        time.sleep(2)

    def test_main_page(self):
        """Проверка пагинации"""
        open_main_page = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[1]/nav/ul/li[1]/a")))
        open_main_page.click()
        print("открыта главная страница")

        all_pages = self.driver.find_elements(By.CLASS_NAME, "nominees-list")
        x = 0
        for i in all_pages:
            x += 1
            for y in range(x):
                button_pagination = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                     "/html/body/div[1]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/button[3]/span[1]")))
                button_pagination.click()

        all_pages_back = self.driver.find_elements(By.CLASS_NAME, "nominees-list")
        p = 0
        for q in all_pages_back:
            p += 1
            for n in range(p):
                button_pagination = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                     "/html/body/div[1]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/button[1]/span[2]")))
                button_pagination.click()

        all_nominations = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/button[2]")))
        all_nominations.click()

        exit_all_nominations = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div/section/div[2]/div[2]/div/div/div[1]/div[2]/span")))
        exit_all_nominations.click()
        print("Пагинация все")

    def waiting_for_error(self):
        """Участок кода в котором ждем ошибку"""
        try:
            search = self.driver.find_element(By.XPATH, '/html/body/header/div[1]/div[2]/a[2]/span')
            search.click()
            expected_result = self.driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/section/div/div[1]/div[1]/div[1]')
            expected_result2 = expected_result.text
            print(expected_result2)
            assert expected_result2 == "сравниваю, якобы жду другого значения"

            """Участок кода в котором указываем что делать после пойманой ошибки"""
        except AssertionError as exception:
            self.driver.refresh()
            time.sleep(5)
            search2 = self.driver.find_element(By.XPATH, '/html/body/header/div[1]/div[2]/a[2]/span')
            search2.click()
            expected_result3 = self.driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/section/div/div[1]/div[1]/div[1]')
            expected_result4 = expected_result3.text
            print(expected_result4)
            assert expected_result4 == "КАК КОПИТЬ БОНУСЫ"
            print("Вот теперь после перезагрузки страницы все нормально")

    def make_screenshots(self):
        try:
            self.driver.find_element(By.XPATH, '/html/body/header/div[1]')
            now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
            name_screenshot = 'screenshot' + now_date + '.png'
            self.driver.save_screenshot('C:\\Users\\долбоеб\\PycharmProjects\\my_application\\screen\\' + name_screenshot)
            print("Скриншот был сделан")
        except NoSuchElementException as exception:
            time.sleep(1)
            self.driver.refresh()
            time.sleep(1)
            self.make_screenshots()
            print("Скриншот был сделан, после отлова ошибки")

    def negativ_auth(self):
        try:
            f = open('C:\\Users\\долбоеб\\PycharmProjects\\my_application\\data\\wrong_pass_login.txt', 'r')
            again = self.driver.find_element(By.XPATH, '/html/body/header/div[1]/div[2]/a[3]/span')
            again.click()
            for i in f:

                log = i.split()[0]
                passw = i.split()[1]

                login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='name']")))
                login.send_keys(log)
                print("Введен логин")

                password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
                password.send_keys(passw)
                print("Введен пароль")

                button_login = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='signinModalWindow']/div/div/div/div[1]/form/button/b")))
                button_login.click()
                print("Нажата кнопка авторизации")

                # check_pass = WebDriverWait(self.driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[1]/form/div[3]/span"))).text
                # check_pass2 = 'Неверный пароль.'
                #
                # check_nik = WebDriverWait(self.driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[1]/form/div[2]/span"))).text
                # check_nik2 = 'Пользователь не найден.'

                check_nik3 = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//*[@id='signinModalWindow']/div/div/div/div[1]/form/div[2]/span"))).text
                check_nik4 = 'Недопустимое значение.'


                if check_nik3 == check_nik4:
                    login.send_keys(Keys.CONTROL + "a")
                    login.send_keys(Keys.BACKSPACE)
                    password.send_keys(Keys.CONTROL + "a")
                    password.send_keys(Keys.BACKSPACE)
                else:
                    print("fine")
                    # f.close()
                print("Не верные пароли и логины не принимает")
            f.close()
        except Exception as exception:
            print("Снова исключение")
            self.driver.refresh()
            self.negativ_auth()

    def chose_filter(self):
        try:
            games = self.driver.find_element(By.XPATH, '/html/body/header/div[1]/nav/ul/li[2]/a')
            games.click()
            search_filter = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[1]/nav/ul/li[2]/a")))
            search_filter.click()
            choose_filter = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='game-list']/div/div[1]/div[1]/button")))
            choose_filter.click()
            choose_filter_menu = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/section/div/div[1]/div[1]/ul/li[1]/a")))
            choose_filter_menu.click()
            time.sleep(2)
            requaried_link = self.driver.current_url
            link_games_filters = "https://www.playground.ru/games?release=all&sort=follow_month&platform=pc"
            assert requaried_link == link_games_filters
            print("Первый фильтр отработал правильно")
            choose_data = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='game-filter']/button/span[1]")))
            choose_data.click()
            choose_filter_menu_data = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/section/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div[1]")))
            choose_filter_menu_data.click()
            choose_filter_menu_data2 = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/section/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div[3]")))
            choose_filter_menu_data2.click()
            choose_button_data = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/section/div/div[1]/div[2]/div/div/div[2]/div/button")))
            choose_button_data.click()
            time.sleep(2)
            filtr_with_data = "https://www.playground.ru/games?sort=follow_month&platform=pc&from=2020-01&to=2022-12"
            current_url_data = self.driver.current_url
            assert filtr_with_data == current_url_data
            print("Фильтр второй раз правильно отработал")
        except Exception as exception:
            self.driver.refresh()
            time.sleep(5)
            self.chose_filter()

    def buy_game(self):
        try:
            search_game_catalog = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='mainNavbar']/ul/li[10]/a")))
            search_game_catalog.click()
            chose_game_catalog = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[1]/nav/ul/li[10]/ul/li[6]/a")))
            chose_game_catalog.click()
            expected_url = "https://www.playground.ru/shop/"
            current_url = self.driver.current_url
            assert expected_url == current_url
            print("Выполнен переход на страницу игр")
            chose_game = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='contentLayout']/div[2]/div[2]/div[2]/a[1]")))
            chose_game.click()
            expected_url2 = "https://www.playground.ru/shop/cyberpunk_2077/"
            current_url2 = self.driver.current_url
            assert expected_url2 == current_url2
            print("Выполнен переход на страницу покупки")
            time.sleep(2)
            chose_buy = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='retailersOffers']/div/table/tbody/tr[1]/td[5]/a")))
            chose_buy.click()
            print("Тест пройден успешно")
        except Exception as exception:
            self.driver.refresh()
            time.sleep(4)
            self.buy_game()

