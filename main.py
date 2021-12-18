"""
Admin interface here
"""
import pymongo
from pymongo import MongoClient
from MongoDB import CarDB


def find_car():
    print("--------Find car---------")
    print("0. Show all cars")
    print("1. By brand")
    print("2. By model")
    print("3. By type")
    print("4. By price")
    print("5. Go back")
    ans = input("?: ")
    if ans == "0":
        return mdb.show_all('cars')
    if ans == "1":
        return mdb.find_document('cars', {'name': input("Enter car brand: ")}, multiple=True)
    if ans == "2":
        return mdb.find_document('cars', {'model': input("Enter car model: ")}, multiple=True)
    if ans == "3":
        return mdb.find_document('cars', {'type': input("Enter car type: ")}, multiple=True)
    if ans == "4":
        return mdb.find_document('cars', {'price': int(input("Enter car price: "))}, multiple=True)
    if ans == "5":
        return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mdb = CarDB()
    while True:
        print("----------Menu-----------")
        print("1.Add car")
        print("2.Find car")
        print("3.Exit")
        ans = input()
        if ans == "1":
            new_car = {
                'name': input('Enter car name: '),
                'model': input('Enter car model: '),
                'type': input('Enter car type: '),
                'price': int(input('Enter car price: '))
            }
            print(mdb.insert_document('cars', new_car))
        if ans == "2":
            doc_list = find_car()
            if doc_list is None:
                continue
            i = 1
            for d in doc_list:
                print("\n\t--" + str(i) + "--")
                i += 1
                for key in d:
                    if "_" not in key:
                        print(key, "->", d[key])
        if ans == "3":
            break
