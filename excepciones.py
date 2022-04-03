import re

class Email():
    def __init__(self):
        self.email = str(input("Vicente: "))

    def compobar(self):

        try:
            re.search("@", self.email)
            print("Comprobando el correo electrónico")

        except:
            pass

        else:



            



