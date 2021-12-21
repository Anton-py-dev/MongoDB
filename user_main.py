"""
User interface here
"""
from user import User


def find_car():

    print("--------Find car---------")
    print("0. Show all cars")
    print("1. By brand")
    print("2. By model")
    print("3. By type")
    print("4. By price")
    print("5. Go back")
    print("6. Show all available cars")
    print("7. Get discount")

    ans = input("?: ")
    if ans == "0":
        doc_list = u.show_all('cars')
    if ans == "1":
        doc_list = u.find_document('cars', {'name': input("Enter car brand: ")}, multiple=True)
    if ans == "2":
        doc_list = u.find_document('cars', {'model': input("Enter car model: ")}, multiple=True)
    if ans == "3":
        doc_list = u.find_document('cars', {'type': input("Enter car type: ")}, multiple=True)
    if ans == "4":
        doc_list = u.find_by_interval('cars', int(input("Enter lower price: ")), int(input("Enter higher price: ")))
    if ans == "5":
        return None
    if ans == "6":
        doc_list = u.show_all_available('cars')
    if ans == "7":
        disc = u.calc_discount()
        if disc == 0:
            print("Нажаль для вас немає пропозицій(")
            return None
        else:
            print("Вітаємо, ви активували знижку ", u.calc_discount(), "%!")
            return None

    i = 1
    for d in doc_list:
        print("\n\t--" + str(i) + "--")
        i += 1
        for key in d:
            if "_" not in key:
                print(key, "->", d[key])

    num = input("Введіть номер авто, що хочете орендувати, або введіть 'exit', якщо хочете вийти: ")
    if num == "exit":
        return
    num = int(num)
    u.rent_car(doc_list[num-1]['_id'], int(input("Введіть к-сть днів: ")))


if __name__ == '__main__':
    u = User()
    while True:
        if u.admin:
            print("----------Menu-----------")
            print("1.Add car")
            print("2.Find car")
            print("3.Update car")
            print("4.Delete car")
            print("5.Exit")
            print("0.Get return")
            ans = input()
            if ans == "1":
                new_car = {
                    'name': input('Enter car name: '),
                    'model': input('Enter car model: '),
                    'type': input('Enter car type: '),
                    'price': int(input('Enter car price: ')),
                    '_id': input('Enter car num: '),
                    'rating': int(input('Enter car rating 1-10: ')),
                    'available': True
                }
                try:
                    print(u.insert_document('cars', new_car))
                except:
                    print("Авто з таким номером уже існує\n")

            if ans == "2":
                doc_list = find_car()

            if ans == "3":
                if u.update_document('cars', {'_id': input('Введіть номер авто, що хочете обновити: ')},
                                       {'price': input('Введіть нову ціну для авто: ')}):
                    print('Успіх!\n')

            if ans == "4":
                if u.delete_document('cars', {'_id': input('Введіть номер авто, що хочете видалити: ')}):
                    print('Успіх!\n')

            if ans == "5":
                break

            if ans == "0":
                i = 0
                doc_list = u.show_all('result')
                for d in doc_list:
                    print("\n\t--" + str(i) + "--")
                    i += 1
                    for key in d:
                        if "_" not in key:
                            print(key, "->", d[key])

        else:
            find_car()
