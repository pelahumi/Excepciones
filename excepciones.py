import re

class Email():
    def __init__(self):
        self.email = str(input("Vicente: "))

    def compobar(self):
        try:
            re.search(". * @. * \ .. *", self.email)
        
        except:
            pass


correo = Email()
print(correo.compobar())

