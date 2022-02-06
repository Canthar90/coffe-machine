
from resources import resources, MENU
import time
local_resources=resources
local_resources['Money']=0


def choices(choice):
    if choice == 'espresso':
        resource_flag = resources_check(chosen_one=MENU['espresso'])
        if resource_flag == False:
            coffe_selection()
        else:
            chosen_drink(chosen_one=MENU['espresso'], drink_name='espresso')
            coffe_selection()
    elif choice == 'latte':
        resource_flag = resources_check(chosen_one=MENU['latte'])
        if resource_flag == False:
            coffe_selection()
        else:
            chosen_drink(chosen_one=MENU['latte'], drink_name='latte')
            coffe_selection()
    elif choice == 'cappuccino':
        resource_flag = resources_check(chosen_one=MENU['cappuccino'])
        if resource_flag == False:
            coffe_selection()
        else:
            chosen_drink(chosen_one=MENU['cappuccino'], drink_name='cappuccino')
            coffe_selection()
    elif choice == 'report':
        print(f"Water: {local_resources['water']}")
        print(f"Milk: {local_resources['milk']}")
        print(f"Coffee: {local_resources['coffee']}")
        print(f"Money: ${local_resources['Money']}")
        coffe_selection()
    elif choice == 'off':
        print('Turning off the mashine see you later hon')
        time.sleep(6)
        return
    else:
        print('Your input is invalid')
        coffe_selection()


def chosen_drink(chosen_one, drink_name):
    print(f"You choose {drink_name} it cost {chosen_one['cost']}$ ")
    payments(chosen_one['cost'], drink_name=drink_name)


def payments(cost_of_drink, drink_name):
    print('Please insert coins')
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total_ammount = quarters + dimes + nickles + pennies
    if total_ammount == cost_of_drink:
        print(f"Here is your {drink_name}")
        resources_subbstraction(cost_of_drink=cost_of_drink, drink_name=drink_name)
        #print(local_resources)

    elif total_ammount > cost_of_drink:
        print(f"Here is ${round(total_ammount-cost_of_drink, 2)} in change.")
        print(f"Here is your {drink_name}")
        resources_subbstraction(cost_of_drink=cost_of_drink, drink_name=drink_name)
        #print(local_resources)

    else:
        print(" Sorry that's not enough money. Money refunded. ")


def resources_subbstraction(cost_of_drink, drink_name):
    local_resources['Money'] += cost_of_drink
    local_resources['water'] -= MENU[drink_name]["ingredients"]["water"]
    local_resources["milk"] -= MENU[drink_name]["ingredients"]["milk"]
    local_resources["coffee"] -= MENU[drink_name]["ingredients"]["coffee"]

def resources_check (chosen_one):
    for item in chosen_one['ingredients']:
        if chosen_one['ingredients'][item] > local_resources[item]:
            print(f"Sorry there is not enough {item}")
            return False






def coffe_selection():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    choices(choice=choice)



coffe_selection()