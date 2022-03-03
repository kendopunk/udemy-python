travel_log = []
running = True


def add_to_travel_log(country, num_visits, cities):
    travel_log.append({
        "country": country,
        "num_visits": num_visits,
        "cities_visited": cities
    })


while running:
    country = input("$> Enter country or *q to quit: ")
    if (country == '*q'):
        running = False
        break
    num_visits = int(input("$> Number of times visited: "))
    cities = [item for item in input("$> Cities visited : ").split()]

    add_to_travel_log(country, num_visits, cities)


print(travel_log)
