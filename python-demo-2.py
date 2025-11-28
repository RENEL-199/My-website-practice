drink=["chocolate", "coffee", "decaf"]
flavor=["caramel", "vanilla", "pepperment", "rasberry", "plain"]
topping=["chocolate", "cinnamon", "caramel"]

print("Nel's Coffee Shop Drinks")
print("-----------------------")

i=1
for d in drink:
    print(i,d)
    i= i + 1
drinks= input("choose your drinks")

print("Nel's Coffee Shop flavors")
print("-----------------------")

i=1
for f in flavor:
    print (i,f)
    i= i + 1
flavors= input("choose your Flavor")

print("Nel's Coffee Shop toppings")
print("-----------------------")

i=1
for t in topping:
    print (i,t)
    i= i + 1
toppings= input("choose your toppings:")

print("here is your order:")
print("main product: ", drink [int(drinks)-1])
print("Flavor: ", flavor [int(flavors)-1])
print("topping: ", topping [int(toppings)-1])
print("Thank your for your order")
