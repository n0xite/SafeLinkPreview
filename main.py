from selenium import webdriver
from colorama import Fore, Back, Style
from pyfiglet import Figlet
from selenium.webdriver.chrome.service import Service
import ChromeDriverManager
from time import sleep


link = ''
webdriverPath = r'C:\Users\n000x\PycharmProjects\SLP'


def Init():
    slpSign = Figlet(font='isometric4')

    print(Fore.BLUE + slpSign.renderText('SLP'))

class Driver:
    service = Service(webdriverPath)
    driver = webdriver.Chrome(service=service)
    driverOptions = webdriver.ChromeOptions()
    driverOptions.add_argument("--headless")
    driverOptions.add_argument("--disable-gpu")
    driverOptions.add_argument("--no-sandbox")


    def slp(d):
        d.get(link)

if __name__ == "__main__":
    Init()
