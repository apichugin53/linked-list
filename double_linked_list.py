class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head  # работа с текущей головой
            self.head.prev_node = new_node  # работа с текущей головой
        self.head = new_node
        print(f"Теперь в голове узел с данными {self.head.data}")

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        print(f"Теперь в хвосте узел с данными {self.tail.data}")

    def remove_from_head(self):
        removed_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        print(f"Были удалены данные {removed_node.data} из головы списка.\nТеперь голова списка {self.head.data}")
        return removed_node.data

    def remove_from_tail(self):
        removed_node = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        print(f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь хвост списка {self.tail.data}")
        return removed_node.data

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        print("Список выведен с начала")


class DerivedLinkedList(LinkedList):

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        print("Список выведен с конца")

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_head(data)
            return

        if self.head is None:
            raise IndexError(f"Выход индекса {index} за границу допустимого диапазона")

        current_node = self.head
        for i in range(index):
            current_node = current_node.next_node
            if current_node is None and i < index - 1:
                raise IndexError(f"Выход индекса {index} за границу допустимого диапазона")

        if current_node is None:
            self.insert_at_tail(data)
        else:
            new_node = Node(data)
            prev_node = current_node.prev_node
            new_node.next_node = current_node
            new_node.prev_node = prev_node
            prev_node.next_node = new_node
            current_node.prev_node = new_node
            print(f"Теперь в позиции {index} узел с данными {new_node.data}")

    def remove_node_index(self, index):
        if self.head is None:
            raise IndexError(f"Выход индекса {index} за границу допустимого диапазона")

        if index == 0:
            return self.remove_from_head()

        removed_node = self.head
        for i in range(index):
            removed_node = removed_node.next_node
            if removed_node is None:
                raise IndexError(f"Выход индекса {index} за границу допустимого диапазона")

        next_node = removed_node.next_node
        if next_node is None:
            return self.remove_from_tail()

        removed_node.prev_node.next_node = next_node
        next_node.prev_node = removed_node.prev_node
        removed_node.prev_node = removed_node.next_node = None
        print(f"Были удалены данные {removed_node.data} из позиции {index} списка.")
        print(f"Теперь в позиции {index} списка {next_node.data}")
        return removed_node.data

    def remove_node_data(self, data):
        removed_node = self.head
        index = 0  # для наглядности вывода позиции, где был найден искомый элемент
        while removed_node is not None:
            if removed_node.data == data:
                next_node = removed_node.next_node
                if next_node is None:
                    return self.remove_from_tail()
                prev_node = removed_node.prev_node
                if prev_node is None:
                    return self.remove_from_head()
                prev_node.next_node = next_node
                next_node.prev_node = prev_node
                removed_node.prev_node = removed_node.next_node = None
                print(f"Были удалены данные {removed_node.data} из позиции {index} списка.")
                return removed_node.data
            removed_node = removed_node.next_node
            index += 1
        return None

    def len_ll(self):
        current_node = self.head
        index = 0
        while current_node is not None:
            index += 1
            current_node = current_node.next_node
        return index

    def contains_from_head(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next_node
        return False

    def contains_from_tail(self, data):
        current_node = self.tail
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.prev_node
        return False

    def contains_from(self, data, from_head = True):
        if from_head:
            return self.contains_from_head(data)
        return self.contains_from_tail(data)
