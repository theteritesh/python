class Email:
    def DisplayEmail(self):
        print("Email")

class Gmail(Email):
    def DisplayGmail(self):
        print("Gmail")

class Yahoo(Email):
    def DisplayYahoo(self):
        print("Yahoo")

obj1=Gmail()
obj1.DisplayEmail()
obj1.DisplayGmail()
obj2=Yahoo()
obj2.DisplayEmail()
obj2.DisplayYahoo()