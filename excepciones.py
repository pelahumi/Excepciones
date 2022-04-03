import re

class Email():
    def __init__(self):
        self.email = str(input("Vicente: "))

    def compobar(self):
        try:
            print("Comprobando el correo electrónico")

        except:
            pass

        else:
            comprobacion = re.search("@", self.email)
            c1 = re.search(".es", self.email)
            c2 = re.search(".com", self.email)

            if comprobacion == None:
                print("El correo introducido no es válido")

            


            

correo = Email()
correo.compobar()



            



