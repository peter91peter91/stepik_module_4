import time
from selenium.common.exceptions import NoSuchElementException
class BasePage():
    #ключевым словом __init__ объявляется конструктор — метод, который вызывается, когда мы создаем объект.
    def __init__(self, browser, url, timeout=10):   #для неявного ожидания
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    #открывает  нужную страницу в браузере, используя метод get().
    def open(self):
        self.browser.get(self.url)     #url="http://selenium1py.pythonanywhere.com/"   к примеру будет в тесте
        #time.sleep(2)

"""
, browser прилетает из conftest.py,   #url  прилетает из конкретного запущенного теста!!!!!!!!!!!!!!
Создавая класс  class MainPage(BasePage): мы его назначаем наследником BasePage, а так как в BasePage содержится конструктор, то инициализируя класс MainPage (в тестах) нужно обязательно передать browser, link которые пойдут в конструктор BasePage.

Только не совсем могу понять почему в BasePage имя url а в тестах уже link. Ведь можно было назвать и в BasePage и в тестах либо url либо link одинаково.
https://blog.testproject.io/2019/07/16/develop-page-object-selenium-tests-using-python/
"""
