import datetime
import pymongo
from MongoDB import CarDB
import math


class User(CarDB):
    def __init__(self):
        super().__init__()
        self.login = ""
        self.password = ""
        self.admin = False
        self.email = ""
        self.experience = 0
        self.reg_date = datetime.datetime.today()
        self.rent_count = 0
        self.lvl = 0
        self.discount = 0

        ans = input("Login or Registration or Exit [l/r/e]: ")
        if ans == "l":
            self.logined()
        if ans == "r":
            self.registration()
        if ans == "e":
            return

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
        self.admin = user["admin"]
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
        self.admin = False
        self.experience = int(input("Years of drive experience: "))
        self.reg_date = datetime.datetime.today()
        self.rent_count = 0

        new_user = {
            "login": self.login,
            "password": self.password,
            "admin": self.admin,
            "email": self.email,
            "experience": self.experience,
            "reg_date": self.reg_date,
            "rent_count": self.rent_count
        }
        collection.insert_one(new_user)
        return 0

    def calc_discount(self):
        user_time = datetime.datetime.today() - self.reg_date
        days = user_time.days + 1
        self.discount = math.floor(math.log(days, 2))
        return self.discount

    def rent_car(self, num, days):
        this_car = self.find_document('cars', {'_id': num})
        deposit = math.floor(this_car['price'] * 60 / (self.rent_count + 1) / (self.experience + 1))
        full_price = this_car['price'] * days
        discount = math.ceil(full_price * self.discount / 100)
        complete_price = full_price - discount
        print("Ціна: ", full_price, " Знижка: -", discount, " Зі знижкою:", complete_price, "Залог: ", deposit)
        ans = input("1.Оплатити\n2.Відмінити\n?: ")
        if ans == "1":
            self.update_document('cars', {'_id': num}, {'available': False})
            self.inc_count({'login': self.login})
            print("Операція успішна!")

            mydate = datetime.datetime.now()
            mydate.strftime("%b")
            collection = self.db['result']
            if collection.find_one({'month': mydate.strftime("%b")}) is None:
                self.insert_document('result', {'month': mydate.strftime("%b"), 'total': 0})
            self.sum_inc({'month': mydate.strftime("%b")}, complete_price)
