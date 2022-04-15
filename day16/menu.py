# day16/menu.py
import constants as c

MENU = {
    c.ES: {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    c.LT: {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5
    },
    c.CA: {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3
    },
}

STARTING_INVENTORY = {
    c.WATER: 300,
    c.MILK: 200,
    c.COFFEE: 100,
    c.MONEY: 0
}
