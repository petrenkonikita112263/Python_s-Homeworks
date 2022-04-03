class Category:
    def __init__(self, category_name: str) -> None:
        self.category_name = category_name
        self.ledger = []
        self.category_balance = 0.0

    def deposit(self, amount: float, description: str = "") -> None:
        new_operation = {"amount": amount, "description": description}
        self.ledger.append(new_operation)
        self.category_balance += amount

    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        return False

    def get_balance(self) -> float:
        return self.category_balance

    def transfer(self, amount, transferee: "Category") -> bool:
        if self.withdraw(amount, f"Transfer to {transferee.category_name}"):
            transferee.deposit(amount, f"Transfer from {self.category_name}")
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        return self.category_balance >= amount

    def __str__(self) -> str:
        result_string = "{:*^30}".format(self.category_name) + "\n"
        for product in self.ledger:
            content_string = "{:23.23}".format(product['description']) + "{:7.2f}".format(product['amount']) + "\n"
            result_string += content_string
        result_string += f"Total: {self.category_balance:.2f}"
        return result_string


def create_spend_chart(categories: list) -> str:
    all_spent = [sum([-state["amount"] for state in category.ledger if state["amount"] < 0])
                 for category in categories]
    total = sum(all_spent)
    max_len = max(len(category.category_name) for category in categories)
    category_strings = [f"{'o' * (1 + int(spent // (total / 10))):>11s}-{category.category_name:<{max_len}}"
                        for spent, category in zip(all_spent, categories)]
    space = f"{' ' * 11}-{' ' * max_len}"
    labels = [f"{'1':<{12 + max_len}}",
              f"{'0987654321':<{12 + max_len}}",
              f"{'00000000000':<{12 + max_len}}",
              f"{'|||||||||||':<{12 + max_len}}"]
    columns = [*labels, *(elem for category_string in category_strings for elem in (space, category_string, space)),
               space]
    return "\n".join(
        ("Percentage spent by category",
         *["".join(row) for row in zip(*columns)])
    )
