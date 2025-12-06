from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Пример существующих базовых методов, реализованных ранее
    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            current.next = new_node
            new_node.prev = current
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
    
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            current.prev = new_node
            new_node.next = current
            self.head = new_node

    def delete_first(self):
        if not self.head:
            return
            
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
        del temp

    def delete_last(self):
        if not self.tail:
            return
            
        temp = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
        del temp


# Расширенный класс DoubleLinkedList, наследуемый от LinkedList
class DoubleLinkedList(LinkedList):
    def print_ll_from_tail(self):
        """ Печать элементов от хвоста к началу """
        node = self.tail
        while node is not None:
            print(node.data, end=" ")
            node = node.prev
        print()

    def insert_at_index(self, index: int, data):
        """ Добавляет элемент по указанному индексу (если индекс больше длины списка, добавляем в конец)."""
        if index <= 0 or not isinstance(index, int):   # вставляем в начало списка
            self.prepend(data)
            return
        
        new_node = Node(data)
        position = 0
        current = self.head
        
        while current and position < index - 1:
            current = current.next
            position += 1
        
        if current is None:  # Индекс превышает размер списка, добавляем в конец
            self.append(data)
        elif current.next is None:  # Последняя позиция перед концом списка
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
        else:                   # Вставка между двумя узлами
            next_node = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = next_node
            next_node.prev = new_node

    def remove_node_index(self, index: int):
        """ Удаление узла по индексу """
        if index < 0 or not isinstance(index, int):
            raise ValueError("Индекс должен быть неотрицательным целым числом")
        
        position = 0
        current = self.head
        
        while current and position != index:
            current = current.next
            position += 1
        
        if current is None:
            raise IndexError(f"Узел с указанным индексом {index} отсутствует.")
        
        prev_node = current.prev
        next_node = current.next
        
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node
        
        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node
        
        del current

    def remove_node_data(self, data):
        """ Удаляем первый узел с указанными данными """
        current = self.head
        
        while current:
            if current.data == data:
                prev_node = current.prev
                next_node = current.next
                
                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = next_node
                    
                if next_node:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node
                
                del current
                break
            
            current = current.next

    def len_ll(self):
        """ Возвращаем количество узлов в списке """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def contains_from_head(self, data):
        """ Проверяет наличие указанного значения начиная с головы списка """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def contains_from_tail(self, data):
        """ Проверяет наличие указанного значения начиная с хвоста списка """
        current = self.tail
        while current:
            if current.data == data:
                return True
            current = current.prev
        return False

    def contains_from(self, data, from_start=True):
        """ Поиск данных, начиная с выбранного направления (True - с головы, False - с хвоста) """
        if from_start:
            return self.contains_from_head(data)
        else:
            return self.contains_from_tail(data)