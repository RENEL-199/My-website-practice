def menu(choices, title ="nel menu", prompt="choose your item:"):
    print(title)
    print(len(title) * "-")
    i=1
    for c in choices:
            print(i,c)
            i=i+1
    choice = input (prompt)
    answer = choices[int(choice)-1]

    return answer

drinks=["chocolate", "coffee", "decaf"]
flavors=["caramel", "vanilla", "pepperment", "rasberry", "plain"]
toppings=["chocolate", "cinnamon", "caramel"]


drink= menu(drinks, "nesl drinks", "choose your drink: ")
flavor= menu(flavors,"nel's flavors", "choose your flavor: ")
topping= menu(toppings,"Nel's toppings", "Choose your toppings: ")

print("here is your order: ")
print("main product: ", drink)
print("Flavor: ", flavor)
print("topping: ", topping)
print("Thank your for your order")




