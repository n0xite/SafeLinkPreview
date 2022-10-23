from colorama import Fore
from pyfiglet import Figlet
import socket
import configparser
from time import sleep

config = configparser.ConfigParser()
config.read('../config.ini')


class Com:
    server = config['IP']['ServerIP']
    port = config['IP']['Port']


    def Client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.server, int(self.port)))

        while True:
            data = s.recv(2048).decode('utf-8')
            dataU = str(data)
            if not dataU:
                print('Breaking')
                break
            match dataU:
                case '#MOTD':
                    print(Fore.BLUE + 'Welcome to Safe Link Preview! Please input a link to preview (ex. https://www.google.com): ' + Fore.CYAN)
                    link = input()
                    if link:
                        s.send(link.encode('utf-8'))
                        sleep(5)
                        fileHandler('SLP.png', s)
                case '#HMSG':
                    print(Fore.GREEN + 'Example: \n link https://www.google.com')



def fileHandler(f, s):
    file = open(f, "wb")
    img_chunk = s.recv(2048)
    while img_chunk:
        file.write(img_chunk)
        img_chunk = s.recv(2048)

    file.close()



def Init():
    slpSign = Figlet(font='isometric1')

    print(Fore.BLUE + slpSign.renderText('SLP'))

    print('\n' + '\n' + '\n')




if __name__ == "__main__":
    print('Initializing connection...')
    sleep(1)
    Com.Client(Com())
