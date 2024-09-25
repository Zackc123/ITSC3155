import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        order_size = input("What size sandwich would you like (small, medium, large)?: ").lower()
        if order_size not in recipes:
            print("Sorry, we don't have that size.")
            continue

        order_ingredients = recipes[order_size]['ingredients']
        order_cost = recipes[order_size]['cost']

        if sandwich_maker_instance.check_resources(order_ingredients):
            coins_inserted = cashier_instance.process_coins()
            if cashier_instance.transaction_result(coins_inserted, order_cost):
                sandwich_maker_instance.make_sandwich(order_size, order_ingredients)
                print(f"Enjoy your {order_size} sandwich!")
            else:
                print("Sorry, that's not enough money.")
        else:
            print("Sorry, we don't have enough ingredients to make that sandwich.")
        cont = input("Would you like to order another sandwich? (yes/no): ").lower()
        if cont != "yes":
            break

if __name__=="__main__":
    main()
