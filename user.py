import datetime
import pymongo


class User:
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['CarDB']
        self.login = ""
        self.password = ""
        self.email = ""
        self.experience = 0
        self.reg_date = datetime.date.today().strftime("%d/%m/%Y")
        self.rent_count = 0

        while True:
            ans = input("Login or Registration or Exit [l/r/e]: ")
            if ans == "l":
                if self.logined() == 0:
                    break
            if ans == "r":
                if self.registration() == 0:
                    break
            if ans == "e":
                break


    def __str__(self):
        return self.login + " " + self.password + " " + self.email + " " + str(self.experience) + " " + self.reg_date + " " + str(self.rent_count)

    def logined(self):
        collection = self.db["users"]
        user = collection.find_one({"login": input("Login: ")})
        password = input("Password: ")

        if user is None:
            print("Wrong login")
            return 1

        if user["password"] != password:
            print("Wrong password")
            return 1

        self.login = user["login"]
        self.password = user["password"]
        self.email = user["email"]
        self.experience = user["experience"]
        self.reg_date = user["reg_date"]
        self.rent_count = user["rent_count"]
        return 0

    def registration(self):
        collection = self.db["users"]
        self.login = input("Login: ")

        if collection.find_one({"login": self.login}):
            print("This login already exist")
            return 1

        self.password = input("Password: ")
        self.email = input("E-mail: ")
        self.experience = int(input("Years of drive experience: "))
        self.reg_date = datetime.date.today().strftime("%d/%m/%Y")
        self.rent_count = 0

        new_user = {
            "login": self.login,
            "password": self.password,
            "email": self.email,
            "experience": self.experience,
            "reg_date": self.reg_date,
            "rent_count": self.rent_count
        }
        collection.insert_one(new_user)
        return 0

u = User()
print(u)