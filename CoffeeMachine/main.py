MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
def resource_calc(coffee_option):
    """Retorna uma lista com a quantidade de cada ingreditente"""
    if coffee_option == 'espresso':
        water = MENU[coffee_option]['ingredients']['water']
        milk = 0
        coffee = MENU[coffee_option]['ingredients']['coffee']
    elif coffee_option == 'latte' or coffee_option == 'cappuccino':
        water = MENU[coffee_option]['ingredients']['water']
        milk = MENU[coffee_option]['ingredients']['milk']
        coffee = MENU[coffee_option]['ingredients']['coffee']
    elif coffee_option == 'report':
        water = resource_storage[0]
        milk = resource_storage[1]
        coffee = resource_storage[2]
    return [water, milk, coffee]

def resource_deduction(resource, cup):
    """Retorna uma lista da quantidade de cada ingrediente após o preparo de um determinado café"""
    left = []
    for i in range(len(resource)):
        items = resource[i] - cup[i]
        left.append(items)
    return left

def check_amount(left, cup):
    """Checka se a quantidade que sobrou é suficiente para o próximo preparo."""
    if left[0] - cup[0] < 0:
        print("Sorry, there is no enough water")
        return False
    elif left[1] - cup[1] < 0:
        print("Sorry, there is no enough milk")
        return False
    elif left[2] - cup[2] < 0:
        print("Sorry, there is no enough coffee")
        return False
    else:
        return True

def check_money(quart, dim, nick, penn, cup):
    """Check se o cliente inseriu a quantidade de dinheiro suficiente."""
    cup_cost = MENU[cup]['cost']
    total = quarters*quart + dimes*dim + nickles*nick + pennies*penn
    price = round(total - cup_cost,2)
    if price < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif price == 0:
        print("No change")
        return True
    else:
        print(f"Here is ${price} in change.")
        print(f"Here is your {cup}. Enjoy!")
        return True

def earnings(cup, total_money):
    price_of_cup = MENU[cup]['cost']
    money = total_money + price_of_cup
    return money

#lista dos ingredientes inicais
resource_storage = [resources['water'], resources['milk'], resources['coffee']]
money = 0
supply = True
while supply == True:
    coffee_options = input("What would you like? espresso, latte or cappuccino?")
    if coffee_options == 'maintain':
        exit()
    elif coffee_options == 'report':
        a = resource_calc(coffee_options)
        print(f"water : {a[0]}ml")
        print(f"milk : {a[1]}ml")
        print(f"coffee : {a[2]}g")
        print(f"money: ${money}")
    else:
        # lista de cada ingrediente necessario
        cup_of_coffee = resource_calc(coffee_options)
        #check se a quantidade disponível é o suficiente
        enough_ingredients = check_amount(resource_storage, cup_of_coffee)
        if enough_ingredients == True:

            print("Please insert coins.")
            coin_quarters = int(input("How many quarters?"))
            coin_dimes = int(input("How many dimes?"))
            coin_nickles = int(input("How many nickles?"))
            coin_pennies = int(input("How many pennies?"))

            enough_money = check_money(coin_quarters, coin_dimes, coin_nickles, coin_pennies, coffee_options)
            if enough_money == True:
                # lista dos ingredientes restantes
                left_calculation = resource_deduction(resource_storage, cup_of_coffee)
                # atualiza a lista de ingredientes restantes
                resource_storage = left_calculation
                total_earnings = earnings(coffee_options, money)
                money = total_earnings


