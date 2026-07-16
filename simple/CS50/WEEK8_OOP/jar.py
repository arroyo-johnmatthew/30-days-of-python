class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Cant fit it all those cookies!")
        else:
            self.size += n

    def withdraw(self, n):  
        if n > self.size:
            raise ValueError("Not enough cookies to take!")
        else:
            self.size -= n

    # Capacity GETTER and SETTER
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    # Size GETTER and SETTER
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar1 = Jar()
    jar1.deposit(10)
    jar1.withdraw(5)
    print(jar1)

if __name__ == "__main__":
    main()