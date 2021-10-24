from Controller import Controller
from ResourceBundle.util.Locale import Locale


class View():
    def __init__(self):
        self.ctrl = Controller()

    def setLocal(self, local):
        self.ctrl.setLocate(local)

    def inputPassword(self):
        while(True):
            print(self.ctrl.getMessage("pw"), end="")
            pw = input()
            if(self.ctrl.checkPassword(pw)):
                break
            print(self.ctrl.getMessage("errPw"))

    def inputAccNum(self):
        while(True):
            print(self.ctrl.getMessage("accNum"), end="")
            accNum = input()
            if(self.ctrl.checkAccountNumber(accNum)):
                break
            print(self.ctrl.getMessage("errAccNum"))

    def inputCaptcha(self):
        while(True):
            captGen = self.ctrl.getCaptcha()
            print(self.ctrl.getMessage('captchaGenerate'), captGen)
            print(self.ctrl.getMessage('captchaInput'), end="")
            captInput = input()
            if(self.ctrl.checkCaptcha(captGen, captInput)):
                break
            print(self.ctrl.getMessage("errCapttcha"))

    def option(self):
        while(True):
            print('''1. Vietnamese
2. English
3. Exit
''')
            print('Please choice one option: ', end='')

            choice = int(input())
            if choice == 1:
                View.setLocal(self, Locale("vi"))
                View.inputAccNum(self)
                View.inputPassword(self)
                View.inputCaptcha(self)
            elif choice == 2:
                View.setLocal(self, Locale("en"))
                View.inputAccNum(self)
                View.inputPassword(self)
                View.inputCaptcha(self)
            elif choice == 3:
                break