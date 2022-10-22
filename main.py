from selenium import webdriver
from colorama import Fore
from pyfiglet import Figlet
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import re

webdriverPath = r'C:\Users\n000x\PycharmProjects\SLP\SafeLinkPreview\geckodriver.exe'
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')


def Init():
    slpSign = Figlet(font='isometric1')

    print(Fore.BLUE + slpSign.renderText('SLP'))

    print('\n' + '\n' + '\n')
    global link
    link = input(Fore.BLUE + 'Welcome to Safe Link Preview! Please provide a link to preview: ' + Fore.CYAN)
    return link



class Driver:
    driverOptions = Options()
    driverOptions.headless = True
    driver = webdriver.Firefox(service=Service(webdriverPath), firefox_binary=binary, options=driverOptions)

    def slp(self, l):
        self.driver.get(l)
        sleep(3)
        self.driver.save_screenshot('SLP.png')
        print(Fore.GREEN + 'Processing ...')
        sleep(1)
        print(Fore.GREEN + 'Finished !')
        self.driver.close()


if __name__ == "__main__":
    Init()
    Driver.slp(Driver(),link)
