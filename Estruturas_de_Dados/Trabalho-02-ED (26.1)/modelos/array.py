class Array:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items.clear()