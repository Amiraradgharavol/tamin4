products = []
def read_file():
    f = open("de.text", "r")
    for line in f :
        result = line.split(",")
        my_dic = {"id":result[0], "name":result[1],
        "price": result[2], "count": result[3]}
        products.append(my_dic)

def show_menu():
    print("1- add")
    print("2- remove")
    print("3-search")
    print("4-edit")
    print("5-show list")
    print("6-buy")
    print("7-exit")

def add():
    id = input()
    name = input()
    price = input()
    count = input()

    new_dic = {"id":id, "name": name, "price": price,"count": count}
    products.append(new_dic)
    print(products)
def remove():
    show_list()
    remove_item = input("enter your id:")
    for product in products:
        if product["id"] == remove_item or product["name"] == remove_item:
            products.remove(product)
            print("removed")
    else:
        print("not found")

def search():
    key = input("entr your key: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            print(product)
            break
        else:
            print("not found")


def edit():
    show_list()
    editor = input("enter your id :")
    for product in products:
        if product["id"] == editor or product["name"] == editor:
            print("sucsess")
        u_product = input("which part to edit: ")
        if u_product =="id":
            id = int(input("enter new id:"))
            product["id"] = id
            break
        elif u_product == "name":
            name = input("enter new name:")
            product["name"] = name
            break
        elif u_product == "price":
            price = int(input("enter new price: "))
            product["price"] = price
            break
        elif u_product == "count":
            count = int(input("plz enter new count: "))
            product["count"] = count
            break
        else:
            print("not found this item")



def show_list():
    print("id\tname\tprice\tcount")
    for product in products:
        print(product["id"], "\t", product["name"], "\t",
         product["price"])
def buy():
    buy_list = []
    price = int()
    while True:
        user_list = input("do you want to countinue buy? yes or no")
        if user_list == "yes":
            price("choose your product:")
            for product in products:
                price(product)
        user_input = input("enter product:")
        for product in products:
            if product["id"] ==  user_input or product["name"] ==user_input:
                print(product)
                break
            else:
                print("this product is out of stock")
                exit()
                print("we have product[count]")
                number_user = int(input("how many do need?"))
                c = int(product["count"])
                if number_user > c:
                    print("the number of you want is out of stock plz try again")
                elif number_user <= c:
                    buy_list.append({"id": product["id"], "name": product["name"],
                    "price": product["price"], "count": number_user})
                    count = int(product["count"]) - number_user
                    products.remove(products)
                    products.append({"id": product["id"], "name": product["name"],
                    "price": product["price"], "count":
                    str(count)})
                    price += int(number_user)* int(product["price"])
                elif user_list == "n":
                    print(buy_list)
                    print("your total cost is:", price)
                    break
                else:
                    print("your input is not corrcet")



def save_to_databas():
    ...


read_file()

while True:
    show_menu()


    user_choice = int(input("enter your choice: "))

    if user_choice == 1:
        add()
    elif user_choice == 2:
        remove()
    elif user_choice == 3:
        search()
    elif user_choice == 4:
        edit()
    elif user_choice == 5:
        show_list()
    elif user_choice == 6:
        buy()
    elif user_choice == 7:
        save_to_databas()
        exit(0)
    else:
        print("plz selcet another")
