# day16/coffee_maker.py
# class definition
import os
import string
from prettytable import PrettyTable

import constants as c
from menu import MENU, STARTING_INVENTORY


class CoffeeMaker:

    def __init__(self):
        self.inventory = STARTING_INVENTORY
        self.running = True
        self.selection = ""

    def _check_resources(self):
        '''
        This will verify there's enough ingredients left to make the drink
        '''
        match = MENU[self.selection]["ingredients"]
        water_required = match[c.WATER]
        coffee_required = match[c.COFFEE]
        if c.MILK in match:
            milk_required = match[c.MILK]
        else:
            milk_required = 0

        if water_required <= self.inventory[c.WATER] and coffee_required <= self.inventory[c.COFFEE] and milk_required <= self.inventory[c.MILK]:
            return True
        else:
            return False

    def _explain_insufficient_resources(self):
        '''
        This will print out reason(s) why there's not enough ingredients
        '''
        match = MENU[self.selection]["ingredients"]

        water_required = match[c.WATER]
        coffee_required = match[c.COFFEE]
        if c.MILK in match:
            milk_required = match[c.MILK]
        else:
            milk_required = 0

        reasons = []
        if water_required > self.inventory[c.WATER]:
            reasons.append(f"Not enough water left for {self.selection}.")
        if coffee_required > self.inventory[c.COFFEE]:
            reasons.append(
                f"Not enough coffee in the hopper for {self.selection}.")
        if milk_required > self.inventory[c.MILK]:
            reasons.append(f"Not enough milk left for {self.selection}.")

        for reason in reasons:
            print(reason)

    def _show_report(self):
        """
        Show the self.inventory report
        """
        table = PrettyTable()
        table.add_column(
            string.capwords(c.WATER), [format("%dmL" % self.inventory[c.WATER])])
        table.add_column(
            string.capwords(c.COFFEE), [format("%dg" % self.inventory[c.COFFEE])])
        table.add_column(
            string.capwords(c.MILK), [format("%dmL" % self.inventory[c.MILK])])
        table.add_column(
            string.capwords(c.MONEY), [format("%s" % "${:,.2f}".format(self.inventory[c.MONEY]))])
        print(table)

    def _show_price_of_selection(self, selection):
        match = MENU[selection]
        print("A(n) %s costs %s" %
              (selection, "${:,.2f}".format(match["cost"])))

    def _take_payment(self):
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

    def _serve_coffee(self, selection, payment):
        match = MENU[selection]["ingredients"]
        cost = MENU[selection]["cost"]

        self.inventory[c.WATER] -= match[c.WATER]
        self.inventory[c.COFFEE] -= match[c.COFFEE]
        if c.MILK in match:
            self.inventory[c.MILK] -= match[c.MILK]

        # calculate change
        change = 0
        if payment > cost:
            change = payment - cost
            self.inventory[c.MONEY] += cost

        return change

    def _show_menu(self):
        table = PrettyTable()
        menu_keys = list(MENU.keys())

        items = list(map(lambda x: string.capwords(x), menu_keys))
        prices = list(
            map(lambda x: "${:,.2f}".format(MENU[x]["cost"]), menu_keys))

        table.add_column("Item", items)
        table.add_column("Price", prices)
        print(table)

    def _get_selection(self):
        print("")
        while not self.selection in [c.ES, c.LT, c.CA, c.RPT, c.QT, c.MN]:
            print(f"What would you like? ({c.ES}/{c.LT}/{c.CA}).")
            self.selection = input(
                f"Type \"{c.RPT}\" for report, \"{c.MN}\" for menu, or \"{c.QT}\" to quit: ")

        # quit
        if self.selection == c.QT:
            self.running = False
            print("OK. Get back to work.")
        # report
        elif self.selection == c.RPT:
            self._show_report()
        # menu
        elif self.selection == c.MN:
            self._show_menu()
        # resource check / take an order
        else:
            os.system('clear')
            has_sufficient_resources = self._check_resources()
            if not has_sufficient_resources:
                self._explain_insufficient_resources()
            else:
                # show and get the cost
                self._show_price_of_selection(self.selection)
                cost = MENU[self.selection]["cost"]

                # take the payment
                payment = 0
                while payment < cost:
                    payment = self._take_payment()
                    if payment < cost:
                        print("Sorry, not enough money.  Money refunded.")

                change = self._serve_coffee(self.selection, payment)
                if change > 0:
                    print("Your change is %s" % "${:,.2f}".format(change))
                print(f"Enjoy your {self.selection}.")

        # reset
        self.selection = ''

    def run(self):
        while self.running:
            self._get_selection()
