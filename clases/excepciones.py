import re

class Email():
    def __init__(self):
        self.usuario = str(input("Usuario: "))
        self.email = str(input("Correo electrónico: "))

    def compobar(self):
        
        try:
            print("Comprobando el correo electrónico")

        except:
            pass

        else:
            comprobacion = re.search("@", self.email)

            if comprobacion == None:
                print("El correo introducido no es válido")
                self.__init__()
            
            n = self.punto_algo()
    
    def punto_algo(self):
        c1 = re.search(".es$", self.email)
        c2 = re.search(".com$", self.email)

        if c1 == None or c2 == None:
            print("Ciberataque, cuenta bloqueada")
        
        else:
            print("Bienvenido {}".format(self.usuario))

correo = Email()
correo.compobar()            


            




            



