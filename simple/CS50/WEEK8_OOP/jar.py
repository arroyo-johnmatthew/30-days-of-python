class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self.size


    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Cant fit it all cuz")
        else:
            self.size += n

    def withdraw(self, n):  
        ...

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
    ...

if __name__ == "__main__":
    main()