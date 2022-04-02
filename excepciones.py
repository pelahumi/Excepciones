import re

class Email():
    def __init__(self):
        self.email = input("Vicente:","\n")

    def compobar(self):
        re.search(". * @. * \ .. *", self.email)
        
