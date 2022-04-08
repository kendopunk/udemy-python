from menu import MENU, STARTING_INVENTORY

ES = 'espresso'
LT = 'latte'
CA = 'cappuccino'
RPT = 'r'
QT = 'q'
WATER = 'water'
COFFEE = 'coffee'
MILK = 'milk'
MONEY = 'money'

# get the selection


def get_selection():
    sel = 'X'
    while not sel in [ES, LT, CA, RPT, QT]:
        print("What would you like? (espresso/latte/cappucino).")
        sel = input(f"Type \"{RPT}\" for report or \"{QT}\" to quit: ")

    return sel


# set up the initial resources
def initialize_resources():
    return STARTING_INVENTORY


def show_report(resources):
    """
    Show the resources report
    """
    print(30 * "=")
    print("MACHINE REPORT:")
    print(f"- Water: {resources[WATER]}mL")
    print(f"- Coffee: {resources[COFFEE]}g")
    print(f"- Milk: {resources[MILK]}mL")
    print("- Money: %s" % "${:,.2f}".format(resources[MONEY]))
    print(30 * "=")


def show_price(selection):
    match = MENU[selection]
    print("%s costs %s" % (selection, "${:,.2f}".format(match["cost"])))


def insufficient_resources(resources, selection):
    match = MENU[selection]["ingredients"]

    water_required = match[WATER]
    coffee_required = match[COFFEE]
    if MILK in match:
        milk_required = match[MILK]
    else:
        milk_required = 0

    if water_required <= resources[WATER] and coffee_required <= resources[COFFEE] and milk_required <= resources[MILK]:
        return False
    return True


def take_payment():
    print("Please insert coins.")
    quarters = input("How many quarters: ")
    dimes = input("How many dimes?: ")
    nickels = input("How many nickels?: ")
    pennies = input("How many pennies?: ")

    try:
        q = int(quarters)
    except ValueError:
        print("Invalid value for quarters...using 0.")
        q = 0

    try:
        d = int(dimes)
    except ValueError:
        print("Invalid value for dimes..using 0.")
        d = 0

    try:
        n = int(nickels)
    except ValueError:
        print("Invalid value for nickels...using 0.")
        n = 0

    try:
        p = int(pennies)
    except ValueError:
        print("Invalid value for quarters...using 0.")
        p = 0

    return q * .25 + d * .10 + n * 0.05 + p * 0.01


def serve_coffee(selection, payment, resources):
    match = MENU[selection]["ingredients"]
    cost = MENU[selection]["cost"]

    resources[WATER] -= match[WATER]
    resources[COFFEE] -= match[COFFEE]
    if MILK in match:
        resources[MILK] -= match[MILK]

    # calculate change
    change = 0
    if payment > cost:
        change = payment - cost

    resources[MONEY] += cost

    return (resources, change)


def coffee_machine():
    running = True
    resources = initialize_resources()
    while running:
        selection = get_selection()
        if selection == QT:
            running = False
            print("Simulation complete.")
        elif selection == RPT:
            show_report(resources)
        else:
            # resources check
            insufficient = insufficient_resources(resources, selection)

            if insufficient:
                print(f"Not enough ingredients for {selection}.")
            else:
                # show and get the cost
                show_price(selection)
                cost = MENU[selection]["cost"]

                # take the payment
                payment = 0
                while payment < cost:
                    payment = take_payment()
                    if payment < cost:
                        print("Sorry, not enough money.  Money refunded.")

                (resources, change) = serve_coffee(
                    selection, payment, resources)
                if change > 0:
                    print("Your change is %s" % "${:,.2f}".format(change))
                print("Enjoy your caw-fee.")


coffee_machine()
