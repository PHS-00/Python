class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

    def size(self):
        return len(self)

    def clear(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        data = self.head.data
        self.head = self.head.next
        return data

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        if self.head.next is None:
            data = self.head.data
            self.head = None
            return data
        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        return data

    def get(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Índice fora do intervalo")
            current = current.next
        if current is None:
            raise IndexError("Índice fora do intervalo")
        return current.data

    def insert_at(self, index, data):
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            if current is None:
                raise IndexError("Índice fora do intervalo")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def remove(self, data):
        if self.is_empty():
            raise ValueError("Lista vazia")
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError(f"Elemento {data} não encontrado")
