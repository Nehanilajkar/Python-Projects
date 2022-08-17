import logo
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
print(logo.art)

report={'water':300,'milk':200,'coffee':100,'cost':0}

def check_resources(user_choice):
    items=MENU[user_choice]["ingredients"]
    for item in items:
        if items[item]<=report[item]:
            report[item] -= items[item]
        else:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def check_money(user_choice,money_inserted):
    money=MENU[user_choice]['cost']
    if money<=money_inserted:
        report['cost'] += money
        change=round(money_inserted-money,2)
        print(f"Here is your change ${change}.")
        return True
    else:
        return False

while True:
    user_choice=input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice=='report':
        print(f"Water: {report['water']}ml")
        print(f"Milk: {report['milk']}ml")
        print(f"Coffee: {report['coffee']}g")
        print(f"Money: ${report['cost']}")
        continue
    if user_choice=='off':
        break
    if user_choice=='refill':
        report = {'water': 300, 'milk': 200, 'coffee': 100, 'cost': 0}
        continue
    required_resources=check_resources(user_choice)
    if required_resources:
        print("Please insert coins.")
        quaters=int(input("How many quaters?"))
        dimes=int(input("How many dimes?"))
        nickles=int(input("How many nickles?"))
        pinnies=int(input("How many pinnies?"))
        money_cal=quaters*0.25+dimes*0.10+nickles*0.05+pinnies*0.001
        required_money=check_money(user_choice,money_cal)
        if required_money:
            print(f"Here is your {user_choice} ☕. Enjoy!")
        else:
            for item in MENU[user_choice]['ingredients']:
                    report[item] += MENU[user_choice]['ingredients'][item]
            print("Sorry that's not enough money. Money refunded.")
