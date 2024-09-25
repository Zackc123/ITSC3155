class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        return quarters + dimes + nickels + pennies

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, False if money is insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is your change: ${change}")
            return True
        else:
            print(f"Sorry, that's not enough money. You need ${cost - coins} more.")
            return False
