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

report={'Water':300,'Milk':200,'Coffee':100,'Money':0}
espresso_required={'Water':50,'Milk':0,'Coffee':18,'Money':1.50}
latte_required={'Water':200,'Milk':150,'Coffee':24,'Money':2.50}
cappuccino_required={'Water':250,'Milk':100,'Coffee':24,'Money':3.00}

def check_resources(user_choice):
    flag=0
    if user_choice=='espresso':
        if espresso_required['Water']<=report['Water']:
            flag=0
            report['Water']-=espresso_required['Water']
        else:
            flag = 1
            insufficient_resource='Water'
            return False,insufficient_resource
        if espresso_required['Coffee']<=report['Coffee']:
            flag=0
            report['Coffee']-=espresso_required['Coffee']
        else:
            flag=1
            insufficient_resource = 'Coffee'
            return False,insufficient_resource

    elif user_choice=='latte':
        if latte_required['Water']<=report['Water'] :
            flag = 0
            report['Water']-=latte_required['Water']
        else:
            flag=1
            insufficient_resource = 'Water'
            return False,insufficient_resource
        if latte_required['Milk']<=report['Milk'] :
            flag = 0
            report['Milk']-=latte_required['Milk']
        else:
            flag=1
            insufficient_resource = 'Milk'
            return False,insufficient_resource
        if latte_required['Coffee']<=report['Coffee'] :
            flag = 0
            report['Coffee']-=latte_required['Coffee']
        else:
            flag = 1
            insufficient_resource = 'Coffee'
            return False, insufficient_resource

    elif user_choice=='cappuccino':
        if cappuccino_required['Water']<=report['Water']:
            flag = 0
            report['Water']-=cappuccino_required['Water']
        else:
            flag=1
            insufficient_resource = 'Water'
            return False,insufficient_resource
        if cappuccino_required['Milk']<=report['Milk'] :
            flag = 0
            report['Milk']-=cappuccino_required['Milk']
        else:
            flag=1
            insufficient_resource = 'Milk'
            return False,insufficient_resource
        if cappuccino_required['Coffee']<=report['Coffee']:
            flag = 0
            report['Coffee']-=cappuccino_required['Coffee']
        else:
            flag = 1
            insufficient_resource = 'Coffee'
            return False, insufficient_resource
    if flag == 0:
        return True,0
def check_money(user_choice,money_inserted):
    if user_choice=='cappuccino' and cappuccino_required['Money'] <=money_inserted:
        report['Money'] += 1.5
        change = money_inserted - 1.5
        return True, round(change,2)
    elif user_choice=='latte' and latte_required['Money'] <=money_inserted:
        report['Money']+=2.5
        change = money_inserted - 2.5
        return True, round(change,2)
    elif user_choice=='espresso' and espresso_required['Money'] <=money_inserted:
        report['Money'] += 3.0
        change=money_inserted-3.0
        return True,round(change,2)
    else:
        return False,0
while True:
    user_choice=input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice=='report':
        print("Water:",report['Water'])
        print("Milk:", report['Milk'])
        print("Coffee:", report['Coffee'])
        print("Money:", report['Money'])
        continue
    if user_choice=='off':
        break
    required_resources=check_resources(user_choice)
    if required_resources[0]:
        print("Please insert coins.")
        quaters=int(input("How many quaters?"))
        dimes=int(input("How many dimes?"))
        nickles=int(input("How many nickles?"))
        pinnies=int(input("How many pinnies?"))
        money_cal=(quaters*25)/100+(dimes*10)/100+(nickles*5)/100+pinnies/100
        print(money_cal)
        required_money=check_money(user_choice,money_cal)
        if required_money[0]:
            if required_money[1]>0:
                print(f"Here is your change {required_money[1]}.")
            print(f"Here is your {user_choice}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Sorry there is not enough {required_resources[1]}.")
