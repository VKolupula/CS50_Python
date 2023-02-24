class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0:
            self._capacity = capacity
            self.no_cookies = 0
        else:
            raise ValueError

    def __str__(self):
        return "🍪"*self.no_cookies

    def deposit(self, n):
        if n > self._capacity or self.no_cookies + n > self._capacity:
            raise ValueError
        self.no_cookies = self.no_cookies+n

    def withdraw(self, n):
        if n > self.no_cookies:
            raise ValueError
        self.no_cookies = self.no_cookies - n

    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self.no_cookies
