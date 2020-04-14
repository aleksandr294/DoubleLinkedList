import random
import timeit


class Node():
    def __init__(self, previous=None, value=None, next=None):
        self.previous = previous
        self.value = value
        self.next = next


class DoubleLinkedList():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self) -> str:
        if self.first is not None:
            current = self.first
            out = 'DoubleLinkedList [' + str(current.value) + ', '
            while current.next is not None:
                current = current.next
                out += str(current.value) + ', '
            return out + ']'
        return '[]'

    def clear(self):
        self.__init__()

    def len(self) -> int:
        self.length = 0
        if self.first is not None:
            self.length += 1
            current = self.first
            while current.next is not None:
                current = current.next
                self.length += 1
        return self.length

    def add(self, x) -> None:
        self.length += 1
        if self.first is None:
            self.last = self.first = Node(None, x, None)
        else:
            self.last.next = self.last = Node(self.last, x, None)

    def push(self, x) -> None:
        self.length += 1
        if self.first is None:
            self.last = self.first = Node(x, None)
        else:
            self.first = Node(x, self.first)

    def max(self):
        node = self.first
        max = self.first.value
        while node.next is not None:
            if node.value > max:
                max = node.value
            node = node.next
        return max

    def max_element_in_end(self, max) -> None:
        node = self.first
        while node.next is not None:
            if node.value == max:
                while node.next is not None:
                    node.next.value, node.value = node.value, node.next.value
                    node = node.next
                break
            node = node.next

    def __getitem__(self, item):
        lenght = 0
        cur = None
        if self.first is not None:
            cur = self.first
            while cur is not None:
                if item == lenght:
                    return cur.value
                cur = cur.next
                lenght += 1


def generate(lst: DoubleLinkedList, size: int) -> None:
    for _ in range(size):
        lst.add(random.randint(0, 1000))


lst = DoubleLinkedList()
try:
    size = int(input('Введите размерность списка '))
    generate(lst, size)
    print(lst)
    lst.max_element_in_end(lst.max())
    print('Список с макс. элементом в конце', lst)
except ValueError:
    print('Вы ввели не число')
input()
