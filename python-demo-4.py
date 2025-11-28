def main_menu():
    while True:
        order = get_order()
        print("check your order")
        print_order(order)
        confirm = input("confirm? press Y to confirm, N to cancel")
        if confirm == "Y" or confirm=="y":
            save_order(order)
            print("thanks for your order:")
            print_order(order)
        else:
            continue


def menu(choices, title ="nel menu", prompt="choose your item:"):
    print(title)
    print(len(title) * "-")
    i=1
    for c in choices:
            print(i,c)
            i=i+1
    while True:
        choice=input(prompt)
        allowed_answers =[]
        for a in range(1, len(choices) + 1):
                allowed_answers.append(str(a))

        allowed_answers.append("X")
        allowed_answers.append("x")

        if choice in allowed_answers:
            if choice == "X" or choice =="x":
                break
            else:
                answer = choices[int(choice) - 1]
                break
        else:
            print("Enter number from 1 to ", len(choices))
            answer=""

    return answer


def read_menu(filename):
    f=open(filename)
    temp= f.readlines()
    result=[]
    for item in temp:
        new_item = item.strip()
        result.append(new_item)

    return result


def get_order():
    order ={}
    order["name"] = input ("please enter your name: ")
    drinks = read_menu("drinks.txt")
    flavors = read_menu("flavors.txt")
    toppings = read_menu("toppings.txt")
    order["drink"]= menu(drinks,"nesl drinks", "choose your drink: ")
    order["flavor"]= menu(flavors,"nel's flavors", "choose your flavor: ")
    order["topping"]= menu(toppings,"Nel's toppings", "Choose your toppings: ")
    return order

def print_order(order):
    print("here is your order: ", order["name"])
    print("main product: ",order["drink"])
    print("Flavor: ", order["flavor"])
    print("topping: ", order["topping"])
    print("Thank your for your order")
    return

def save_order(order):
    print("saving order...")
    return

main_menu()
