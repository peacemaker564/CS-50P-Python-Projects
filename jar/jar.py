class Jar:

    def __init__(self, capacity=12):
        if capacity < 0:
            raise(ValueError)
        self._capacity = capacity #Max Cap
        self._cookies = 0


    def __str__(self):
        return f"{self._cookies*'🍪'}"


    def deposit(self, n):
        #Check 1.
        if n < 0:
            raise ValueError("Negative values are not allowed.")
        #Check 2:
        total_future_cookies = n + self._cookies
        if total_future_cookies > self._capacity:
            raise ValueError

        self._cookies = total_future_cookies

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Negative values are not allowed.")

        if self._cookies < n:
            raise ValueError

        self._cookies -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

def main():
    jar = Jar(5, 1)
    print(f"Initially, the jar has: {jar} cookies.")

    jar.deposit(1)
    print(f"Updated number of cookies: {jar}")

    jar.withdraw(1)
    print(f"Leftover cookies: {jar}")

if __name__ == "__main__":
    main()
