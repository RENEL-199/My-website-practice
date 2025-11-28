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


def get_order():
    return{}

def print_order(order):
    print(order)
    return

def save_order(order):
    print("saving order...")
    return

main_menu()
