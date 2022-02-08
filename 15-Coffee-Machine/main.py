# Dictionaries
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

def checkEspressoIngredients():
    if

while True:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        break
    if choice == 'report':
        print(f'''Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${''}''')
    if choice == 'espresso':
        if checkEspressoIngredients():
            makeEspressoCoffee();
        else:
            print(f'Sorry, there is not enough {resource}')
    if choice == 'latte':
        checkLatteIngredients()
    if choice == 'cappuccino':
        checkCappuccinoIngredients()



