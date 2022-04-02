import re

class Email():
    def __init__(self):
        self.email = str(input("Vicente: "))

    def compobar(self):

        try:
            re.search(". * @. * \ .. *", self.email)
        
        except None:
            print("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
            


correo = Email()
print(correo.compobar())

