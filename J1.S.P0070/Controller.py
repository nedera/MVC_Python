import ResourceBundle as rb
from ResourceBundle.util.Locale import Locale
import re
import random


class Controller():

    def __init__(self):
        self.r = None

    def setLocate(self, locate):
        if(locate == Locale("en")):
            self.r = rb.get_bundle("model\En", locate)
        elif locate == Locale("vi"):
            self.r = rb.get_bundle("model\Vi", locate)

    def getMessage(self, key):
        return self.r.get(key)

    def checkAccountNumber(self, accNum):
        return bool((re.compile("\d{10}")).match(accNum) and len(accNum) == 10)

    def checkPassword(self, pw):
        return bool((re.compile("^(?=.*[0-9])(?=.*[a-zA-Z])(?=\\S+$).{8,31}$")).match(pw))

    def getCaptcha(self):
        data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        captcha = ""
        while(not len(captcha) == 5):
            captcha += random.choice(data)
        return captcha

    def checkCaptcha(self, catpchaInput, captchaGenerrate):
        return captchaGenerrate == catpchaInput