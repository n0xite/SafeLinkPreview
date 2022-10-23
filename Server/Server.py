from selenium import webdriver
import configparser
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import socket


config = configparser.ConfigParser()
config.read(r'../config.ini')
webdriverPath = config['BINARIES']['PathToWebdriver']
binary = FirefoxBinary(config['BINARIES']['PathToFirefoxBinary'])

class Com:
    host = config['IP']['ServerIP']
    port = config['IP']['Port']

    def Server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((str(self.host), int(self.port)))

        s.listen(1)
        client_s , addr = s.accept()
        client_s.send('#MOTD'.encode('utf-8'))
        print("Sending #MOTD")
        print('Connected: ' + str(addr))

        while True:
            data = client_s.recv(2048).decode('utf-8')
            dataU = str(data)
            print('Command received: ' + dataU)
            if not dataU:
                break
            match dataU:
                case 'exit':
                    s.close()
                    client_s.send('Exiting'.encode('utf-8'))
                    break
                case 'help':
                    client_s.send('#HMSG'.encode('utf-8'))
                    print('Sending #HMSG')
                case _:
                    Driver.slp(Driver(),dataU)
                    print('Processing')
                    sleep(2)
                    fileHandler('SLP.png', client_s)
                    sleep(1)
                    print('Finished!')



def fileHandler(f, s):
    file = open(f, "rb")
    img_data = file.read(2048)
    while img_data:
        s.send(img_data)
        img_data = file.read(2048)


    file.close()





class Driver:
    driverOptions = Options()
    driverOptions.headless = False
    driver = webdriver.Firefox(service=Service(webdriverPath), firefox_binary=binary, options=driverOptions)


    def slp(self, l):
        self.driver.get(l)
        sleep(3)
        self.driver.save_screenshot('SLP.png')
        self.driver.close()


if __name__ == "__main__":
    print('Listening...')
    sleep(1)
    Com.Server(Com())

