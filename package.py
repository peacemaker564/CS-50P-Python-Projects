class Package:
    def __init__(self, number, sender, receiver, weight):

        """
        Instance Variables

        """
        self.number=number
        self.sender=sender
        self.receiver=receiver
        self.weight = weight

    def __str__(self):
        return f"Package{self.number}: {self.sender} to {self.receiver}, {self.weight} kg."

    def calculate_costs(self, cost_per_kg):
        return self.weight * cost_per_kg

def main():
    packages = [
        Package(number=1, sender="Alice", receiver="Bob", weight=5),
        Package(number=2, sender="Bob", receiver="Alice", weight=10)
    ]

    for package in packages:
        print(f"{package} costs ${package.calculate_costs(cost_per_kg=2)}")

main()
