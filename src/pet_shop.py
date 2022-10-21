# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, cash):
    shop["admin"]["total_cash"] += cash

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, num):
    shop["admin"]["pets_sold"] += num

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pets = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    return pets

def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
             return pet
    return None

def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, pet):
    shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    return pet["price"] <= customer["cash"]

def sell_pet_to_customer(shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        #move cash from customer to shop
        remove_customer_cash(customer, pet["price"])
        price = pet["price"]
        add_or_remove_cash(shop, price)
        print(shop)
        #move pet from shop to customer
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(shop, pet["name"])
        #increase pets sold for shop
        increase_pets_sold(shop, 1)

    
